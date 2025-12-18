import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time: {time.time() - self.start_time:.3f} sec")


@contextmanager
def cm_timer_2():
    start = time.time()
    try:
        yield
    finally:
        print(f"time: {time.time() - start:.3f} sec")


def task_6():

    from time import sleep


    print("Демонстрация cm_timer_1 (ожидание 5 с):")
    with cm_timer_1():
        sleep(5)

    print("\nДемонстрация cm_timer_2 (ожидание 5 с):")
    with cm_timer_2():
        sleep(5)
