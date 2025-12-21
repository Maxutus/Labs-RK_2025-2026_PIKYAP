import unittest
from refactored_browsers import (
    task1_filter_computers_starting_with_a,
    task2_max_memory_per_computer,
    task3_all_connections_sorted
)


class TestBrowserSystem(unittest.TestCase):

    def test_task1_filter_computers_starting_with_a(self):
        """Тест для задания 1: фильтрация компьютеров на букву 'A'"""
        test_data = [
            ('Chrome', 512, 'Asus ROG'),
            ('Firefox', 256, 'Apple MacBook Pro'),
            ('Safari', 384, 'Acer Predator'),
            ('Edge', 320, 'Dell XPS'),
            ('Opera', 192, 'Asus ZenBook'),
        ]

        result = task1_filter_computers_starting_with_a(test_data)

        self.assertIsInstance(result, dict)

        self.assertIn('Asus ROG', result)
        self.assertIn('Apple MacBook Pro', result)
        self.assertIn('Acer Predator', result)
        self.assertIn('Asus ZenBook', result)
        self.assertNotIn('Dell XPS', result)

        self.assertIn('Chrome', result['Asus ROG'])

        test_data_with_duplicates = [
            ('Chrome', 512, 'Asus ROG'),
            ('Chrome', 512, 'Asus ROG'),
            ('Firefox', 256, 'Asus ROG'),
        ]
        result2 = task1_filter_computers_starting_with_a(test_data_with_duplicates)
        self.assertEqual(len(result2['Asus ROG']), 2)

    def test_task2_max_memory_per_computer(self):
        """Тест для задания 2: максимальная память на каждом компьютере"""
        from refactored_browsers import Computer

        test_data = [
            ('Chrome', 512, 'Asus ROG'),
            ('Firefox', 256, 'Asus ROG'),
            ('Safari', 384, 'Apple MacBook Pro'),
            ('Edge', 320, 'Apple MacBook Pro'),
            ('Opera', 192, 'Dell XPS'),
        ]

        computers_list = [
            Computer(1, 'Asus ROG'),
            Computer(2, 'Apple MacBook Pro'),
            Computer(3, 'Dell XPS'),
            Computer(4, 'Empty Computer'),
        ]

        result = task2_max_memory_per_computer(computers_list, test_data)

        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)

        self.assertEqual(result[0][0], 'Asus ROG')
        self.assertEqual(result[1][0], 'Apple MacBook Pro')
        self.assertEqual(result[2][0], 'Dell XPS')
        self.assertEqual(result[3][0], 'Empty Computer')

        result_dict = dict(result)
        self.assertEqual(result_dict['Asus ROG'], 512)
        self.assertEqual(result_dict['Apple MacBook Pro'], 384)
        self.assertEqual(result_dict['Dell XPS'], 192)
        self.assertEqual(result_dict['Empty Computer'], 0)

    def test_task3_all_connections_sorted(self):
        """Тест для задания 3: сортировка всех связей по компьютерам"""
        test_data = [
            ('Firefox', 256, 'Apple MacBook Pro'),
            ('Chrome', 512, 'Asus ROG'),
            ('Safari', 384, 'Apple MacBook Pro'),
            ('Edge', 320, 'Asus ROG'),
            ('Opera', 192, 'Dell XPS'),
        ]

        result = task3_all_connections_sorted(test_data)

        self.assertIsInstance(result, dict)

        keys = list(result.keys())
        self.assertEqual(keys, ['Apple MacBook Pro', 'Asus ROG', 'Dell XPS'])

        self.assertIn('Chrome (512 МБ)', result['Asus ROG'])
        self.assertIn('Edge (320 МБ)', result['Asus ROG'])
        self.assertIn('Firefox (256 МБ)', result['Apple MacBook Pro'])
        self.assertIn('Safari (384 МБ)', result['Apple MacBook Pro'])
        self.assertIn('Opera (192 МБ)', result['Dell XPS'])

        self.assertEqual(len(result['Apple MacBook Pro']), 2)
        self.assertEqual(len(result['Asus ROG']), 2)
        self.assertEqual(len(result['Dell XPS']), 1)


if __name__ == '__main__':
    unittest.main()
