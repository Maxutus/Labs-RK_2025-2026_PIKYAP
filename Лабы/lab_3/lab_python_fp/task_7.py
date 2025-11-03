import json
import os
from .task_5 import print_result
from .task_6 import cm_timer_1
from .task_2 import gen_random
from .task_3 import Unique

_JOB_KEYS = ('name', 'job-name', 'job', 'profession', 'title')

def Get_title(d):
    for k in _JOB_KEYS:
        if k in d and d[k]:
            return d[k]
    return None


@print_result
def f1(data):
    titles = filter(None, map(Get_title, data))
    return sorted(Unique(titles, ignore_case=True), key=lambda s: s.casefold())


@print_result
def f2(professions):
    return list(filter(lambda s: s.lower().startswith('программист'), professions))


@print_result
def f3(professions):
    return [f"{s} с опытом Python" for s in professions]


@print_result
def f4(professions):
    salaries = list(gen_random(len(professions), 100_000, 200_000))
    return [f"{title}, зарплата {salary} руб." for title, salary in zip(professions, salaries)]


def task_7():
    print("Задача 7: обработка данных (f1 → f2 → f3 → f4)\n")

    path = input("Путь к data_light.json (Enter — использовать пример): ").strip()
    if not path:
        path = os.path.join(os.path.dirname(__file__), "data_light.json")

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файл не найден.")
        return

    with cm_timer_1():
        f4(f3(f2(f1(data))))
