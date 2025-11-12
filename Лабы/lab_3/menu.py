from lab_3.lab_python_fp.field import task_1
from lab_3.lab_python_fp.gen_random import task_2
from lab_3.lab_python_fp.unique import task_3
from lab_3.lab_python_fp.sort import task_4
from lab_3.lab_python_fp.print_result import task_5
from lab_3.lab_python_fp.cm_timer import task_6
from lab_3.lab_python_fp.process_data import task_7

def run_menu():
    MENU = """
    ================ Меню =================
    1) Задача 1
    2) Задача 2
    3) Задача 3
    4) Задача 4
    5) Задача 5
    6) Задача 6
    7) Задача 7
    0) Выход
    --------------------------------------
    Выберите задачу:
    """

    actions = {
        "1": task_1, "2": task_2, "3": task_3, "4": task_4,
        "5": task_5, "6": task_6, "7": task_7,
    }

    while True:
        choice = input(MENU).strip()
        if choice == "0":
            print("Выход.")
            break
        action = actions.get(choice)
        if action:
            print("\n--- Старт задачи ---")
            action()
            print("--- Конец задачи ---\n")
        else:
            print("Неизвестный пункт. Попробуй ещё раз.\n")
