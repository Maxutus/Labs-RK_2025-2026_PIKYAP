def field(items, *args):
    assert len(args) > 0

    one_key = (len(args) == 1)
    if one_key:
        key = args[0]
        for item in items:
            val = item.get(key)
            if val is not None:
                yield val
    else:
        for item in items:
            chunk = {k: item.get(k) for k in args if item.get(k) is not None}
            if chunk:
                yield chunk


def task_1():

    goods = [
        {"title": "Ковер", "price": 2000, "color": "green"},
        {"title": "Диван для отдыха", "color": "black"},
        {"title": None, "price": 3500},
    ]

    raw = input("Ключ(и) через запятую: ").strip()
    keys = [k.strip() for k in raw.split(",") if k.strip()]

    if not keys:
        print("Ключи не заданы")
        return

    result = list(field(goods, *keys))
    print("Результат:", result)
