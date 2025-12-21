from operator import itemgetter


class Browser:
    def __init__(self, id, name, memory_usage, computer_id):
        self.id = id
        self.name = name
        self.memory_usage = memory_usage
        self.computer_id = computer_id


class Computer:
    def __init__(self, id, model):
        self.id = id
        self.model = model


class BrowserComputer:
    def __init__(self, computer_id, browser_id):
        self.computer_id = computer_id
        self.browser_id = browser_id


computers = [
    Computer(1, 'Asus ROG'),
    Computer(2, 'Apple MacBook Pro'),
    Computer(3, 'Dell XPS'),
    Computer(11, 'Acer Predator'),
    Computer(22, 'Apple iMac'),
    Computer(33, 'Asus ZenBook'),
]

browsers = [
    Browser(1, 'Chrome', 512, 1),
    Browser(2, 'Firefox', 256, 2),
    Browser(3, 'Safari', 384, 3),
    Browser(4, 'Edge', 320, 3),
    Browser(5, 'Opera', 192, 3),
]

browsers_computers = [
    BrowserComputer(1, 1),
    BrowserComputer(2, 2),
    BrowserComputer(3, 3),
    BrowserComputer(3, 4),
    BrowserComputer(3, 5),
    BrowserComputer(11, 1),
    BrowserComputer(22, 2),
    BrowserComputer(33, 3),
    BrowserComputer(33, 4),
    BrowserComputer(33, 5),
]


def create_one_to_many(computers, browsers):
    return [(b.name, b.memory_usage, c.model)
            for c in computers
            for b in browsers
            if b.computer_id == c.id]


def create_many_to_many(computers, browsers, browsers_computers):
    many_to_many_temp = [(c.model, bc.computer_id, bc.browser_id)
                         for c in computers
                         for bc in browsers_computers
                         if c.id == bc.computer_id]

    return [(b.name, b.memory_usage, comp_model)
            for comp_model, comp_id, browser_id in many_to_many_temp
            for b in browsers if b.id == browser_id]


def task1_filter_computers_starting_with_a(many_to_many):
    comps_with_a = list(filter(lambda i: i[2].startswith('A'), many_to_many))

    result = {}
    for browser_name, memory, comp_model in comps_with_a:
        if comp_model not in result:
            result[comp_model] = []
        if browser_name not in result[comp_model]:
            result[comp_model].append(browser_name)

    return result


def task2_max_memory_per_computer(computers, many_to_many):
    result_unsorted = []

    for c in computers:
        c_browsers = list(filter(lambda i: i[2] == c.model, many_to_many))
        if len(c_browsers) > 0:
            c_memory = [memory for _, memory, _ in c_browsers]
            c_memory_max = max(c_memory)
            result_unsorted.append((c.model, c_memory_max))
        else:
            result_unsorted.append((c.model, 0))

    return sorted(result_unsorted, key=itemgetter(1), reverse=True)


def task3_all_connections_sorted(many_to_many):
    sorted_connections = sorted(many_to_many, key=itemgetter(2))

    grouped_result = {}
    for browser_name, memory, comp_model in sorted_connections:
        if comp_model not in grouped_result:
            grouped_result[comp_model] = []
        grouped_result[comp_model].append(f"{browser_name} ({memory} МБ)")

    return grouped_result


def print_task1(result):
    print('Задание Г1')
    print('Список всех компьютеров, у которых модель начинается с буквы "A", и список браузеров на них:')
    for comp, browsers_list in sorted(result.items()):
        print(f'{comp}: {browsers_list}')


def print_task2(result):
    print('\nЗадание Г2')
    print('Список компьютеров с максимальным использованием памяти браузеров на каждом компьютере, отсортированный по максимальному использованию памяти:')
    for comp, max_memory in result:
        print(f'{comp}: {max_memory} МБ')


def print_task3(result):
    print('\nЗадание Г3')
    print('Список всех связанных браузеров и компьютеров, отсортированный по компьютерам:')
    for comp_model, browsers_list in sorted(result.items()):
        print(f'{comp_model}: {browsers_list}')


def main():
    one_to_many = create_one_to_many(computers, browsers)
    many_to_many = create_many_to_many(computers, browsers, browsers_computers)

    task1_result = task1_filter_computers_starting_with_a(many_to_many)
    print_task1(task1_result)

    task2_result = task2_max_memory_per_computer(computers, many_to_many)
    print_task2(task2_result)

    task3_result = task3_all_connections_sorted(many_to_many)
    print_task3(task3_result)


if __name__ == '__main__':
    main()
