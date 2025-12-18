def task_4():
    data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
    print("Исходные данные:", data)

    result = sorted(data, key=abs, reverse=True)
    print("Сортировка без lambda:", result)

    result_with_lambda = sorted(data, key=lambda x: abs(x), reverse=True)
    print("Сортировка с lambda:", result_with_lambda)
