import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)


def task_2():
    num_count = int(input("Сколько чисел сгенерировать: "))
    begin = int(input("Начало диапазона: "))
    end = int(input("Конец диапазона: "))
    result = list(gen_random(num_count, begin, end))
    print([num for num in result])
