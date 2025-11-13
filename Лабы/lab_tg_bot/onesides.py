import os
import logging
import random

from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
log = logging.getLogger(__name__)


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


PLAYER = "❌"
BOT = "⭕"
EMPTY = " "

reply_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton("🎮 Новая игра")],
        [KeyboardButton("ℹ️ Помощь")],
    ],
    resize_keyboard=True
)



WIN_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def check_winner(board, symbol):
    """Проверяем, есть ли выигрыш у symbol (PLAYER или BOT)."""
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c] == symbol:
            return True
    return False


def is_draw(board):
    """Ничья: нет пустых клеток и нет победителя."""
    return all(cell != EMPTY for cell in board)


def ai_move(board):
    """
    Простой «умный» ход бота:
    1) Если есть победный ход — сделать его.
    2) Если игрок может выиграть следующим ходом — заблокировать.
    3) Занять центр, если свободен.
    4) Занять угол, если есть.
    5) Иначе любой свободный ход.
    """
    for i in range(9):
        if board[i] == EMPTY:
            board_copy = board.copy()
            board_copy[i] = BOT
            if check_winner(board_copy, BOT):
                return i

    for i in range(9):
        if board[i] == EMPTY:
            board_copy = board.copy()
            board_copy[i] = PLAYER
            if check_winner(board_copy, PLAYER):
                return i

    move = [i for i in (0, 2, 6, 8, 4) if board[i] == EMPTY]
    if move:
        return random.choice(move)

    free_cells = [i for i in range(9) if board[i] == EMPTY]
    if free_cells:
        return random.choice(free_cells)

    return None


def board_to_keyboard(board):
    """Преобразуем массив board (9 элементов) в InlineKeyboardMarkup 3x3."""
    buttons = []
    for row in range(3):
        row_buttons = []
        for col in range(3):
            idx = row * 3 + col
            cell = board[idx]
            text = cell if cell != EMPTY else "⬜"
            row_buttons.append(
                InlineKeyboardButton(text=text, callback_data=str(idx))
            )
        buttons.append(row_buttons)
    return InlineKeyboardMarkup(buttons)


def reset_game(context: ContextTypes.DEFAULT_TYPE):
    """Начать новую игру в user_data."""
    context.user_data["board"] = [EMPTY] * 9
    context.user_data["game_active"] = True
    context.user_data["player_turn"] = True


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name or "игрок"
    text = (
        f"Привет, {user}! 👋\n\n"
        "Это бот с игрой «Крестики-нолики».\n"
        "Ты играешь за ❌, бот — за ⭕.\n\n"
        "Нажми «🎮 Новая игра», чтобы начать."
    )
    await update.message.reply_text(text, reply_markup=reply_kb)


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Правила игры:\n\n"
        "• Ты играешь за ❌, бот — за ⭕.\n"
        "• Сначала ходишь ты, потом бот.\n"
        "• Нажимай на клетки на поле, чтобы сделать ход.\n"
        "• Бот пытается выигрывать или блокировать твои ходы.\n\n"
        "Нажми «🎮 Новая игра», чтобы начать новую партию."
    )
    await update.message.reply_text(text, reply_markup=reply_kb)


async def new_game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reset_game(context)
    board = context.user_data["board"]
    text = "Новая игра! Ты ходишь первым (❌).\nВыбери клетку:"
    await update.message.reply_text(
        text,
        reply_markup=board_to_keyboard(board)
    )


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").strip().lower()

    if text == "🎮 новая игра".lower():
        await new_game(update, context)
        return

    if text in ("ℹ️ помощь".lower(), "/help"):
        await help_cmd(update, context)
        return

    await update.message.reply_text(
        "Чтобы начать, нажми «🎮 Новая игра».\n"
        "Для справки — «ℹ️ Помощь».",
        reply_markup=reply_kb
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if not context.user_data.get("game_active"):
        await query.edit_message_text(
            "Игра уже закончена.\n"
            "Нажми «🎮 Новая игра», чтобы сыграть ещё раз.",
            reply_markup=reply_kb
        )
        return

    board = context.user_data.get("board")
    if board is None:
        reset_game(context)
        board = context.user_data["board"]

    player_turn = context.user_data.get("player_turn", True)

    try:
        cell_index = int(query.data)
    except (ValueError, TypeError):
        return

    if not player_turn:
        await query.answer("Сейчас ход бота, подожди 🙂", show_alert=False)
        return

    if board[cell_index] != EMPTY:
        await query.answer("Эта клетка уже занята.", show_alert=False)
        return

    board[cell_index] = PLAYER

    if check_winner(board, PLAYER):
        context.user_data["game_active"] = False
        text = "Ты победил! 🎉\n\nНажми «🎮 Новая игра», чтобы сыграть ещё раз."
        await query.edit_message_text(
            text,
            reply_markup=board_to_keyboard(board)
        )
        return

    if is_draw(board):
        context.user_data["game_active"] = False
        text = "Ничья 🤝\n\nНажми «🎮 Новая игра», чтобы попробовать ещё раз."
        await query.edit_message_text(
            text,
            reply_markup=board_to_keyboard(board)
        )
        return

    context.user_data["player_turn"] = False
    bot_index = ai_move(board)
    if bot_index is not None:
        board[bot_index] = BOT

    if check_winner(board, BOT):
        context.user_data["game_active"] = False
        text = "Я победил 😎\n\nНажми «🎮 Новая игра», чтобы сыграть ещё."
        await query.edit_message_text(
            text,
            reply_markup=board_to_keyboard(board)
        )
        return

    if is_draw(board):
        context.user_data["game_active"] = False
        text = "Ничья 🤝\n\nНажми «🎮 Новая игра», чтобы попробовать ещё раз."
        await query.edit_message_text(
            text,
            reply_markup=board_to_keyboard(board)
        )
        return

    context.user_data["player_turn"] = True
    text = "Твой ход (❌). Выбери клетку:"
    await query.edit_message_text(
        text,
        reply_markup=board_to_keyboard(board)
    )


def main():
    if not BOT_TOKEN:
        raise SystemExit("Не задан BOT_TOKEN в файле .env")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))
    app.add_handler(CallbackQueryHandler(button_handler))

    log.info("Бот запущен (крестики-нолики)")
    app.run_polling()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        log.info("Бот остановлен.")
