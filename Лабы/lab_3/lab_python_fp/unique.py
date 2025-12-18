class Unique:

    def __init__(self, items, **kwargs):
        self._iter = iter(items)
        self._ignore_case = bool(kwargs.get('ignore_case', False))
        self._seen = set()

    def _key(self, value):
        if isinstance(value, str) and self._ignore_case:
            return value.lower()
        return value

    def __iter__(self):
        return self

    def __next__(self):
        for item in self._iter:
            key = self._key(item)
            try:
                if key in self._seen:
                    continue
                self._seen.add(key)
                return item
            except TypeError:
                key = repr(key)
                if key in self._seen:
                    continue
                self._seen.add(key)
                return item
        raise StopIteration


def task_3():

    numbers = [1, 1, 1, 2, 2, 3, 3, 3]
    print("\nЧисла:", numbers)
    print("Результат:", list(Unique(numbers)))

    words = ["a", "A", "b", "B", "a", "b"]
    print("\nСтроки (без учёта регистра):", words)
    print("Результат:", list(Unique(words)))

    print("\nСтроки (с учётом регистра):", words)
    print("Результат:", list(Unique(words, ignore_case=True)))
