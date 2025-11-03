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

def main():
    one_to_many = [(b.name, b.memory_usage, c.model)
                   for c in computers
                   for b in browsers
                   if b.computer_id == c.id]

    many_to_many_temp = [(c.model, bc.computer_id, bc.browser_id)
                         for c in computers
                         for bc in browsers_computers
                         if c.id == bc.computer_id]

    many_to_many = [(b.name, b.memory_usage, comp_model)
                    for comp_model, comp_id, browser_id in many_to_many_temp
                    for b in browsers if b.id == browser_id]

    print('Задание Г1')
    print('Список всех компьютеров, у которых модель начинается с буквы "A", и список браузеров на них:')
    comps_with_a = list(filter(lambda i: i[2].startswith('A'), many_to_many))

    res_1 = {}
    for browser_name, memory, comp_model in comps_with_a:
        if comp_model not in res_1:
            res_1[comp_model] = []
        if browser_name not in res_1[comp_model]:
            res_1[comp_model].append(browser_name)

    for comp, browsers_list in sorted(res_1.items()):
        print(f'{comp}: {browsers_list}')

    print('\nЗадание Г2')
    print('Список компьютеров с максимальным использованием памяти браузеров на каждом компьютере, отсортированный по максимальному использованию памяти:')
    res_2_unsorted = []

    for c in computers:
        c_browsers = list(filter(lambda i: i[2] == c.model, many_to_many))
        if len(c_browsers) > 0:
            c_memory = [memory for _, memory, _ in c_browsers]
            c_memory_max = max(c_memory)
            res_2_unsorted.append((c.model, c_memory_max))
        else:
            res_2_unsorted.append((c.model, 0))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    for comp, max_memory in res_2:
        print(f'{comp}: {max_memory} МБ')

    print('\nЗадание Г3')
    print('Список всех связанных браузеров и компьютеров, отсортированный по компьютерам:')

    res_3 = sorted(many_to_many, key=itemgetter(2))
    grouped_result = {}
    for browser_name, memory, comp_model in res_3:
        if comp_model not in grouped_result:
            grouped_result[comp_model] = []
        grouped_result[comp_model].append(f"{browser_name} ({memory} МБ)")

    for comp_model, browsers_list in sorted(grouped_result.items()):
        print(f'{comp_model}: {browsers_list}')

if __name__ == '__main__':
    main()
