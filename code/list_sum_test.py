from unittest import TestCase, main
from list_sum import list_sum


class ListSumTest(TestCase):

    def test_list_sum(self):
        self.assertEqual(list_sum([1, 2], 1, 2), [])
        self.assertEqual(list_sum([1, 2], 3, 2), [[1, 2]])
        self.assertEqual(list_sum([1, 2, 3], 3, 2), [[1, 2]])
        self.assertEqual(list_sum([1, 2, 3], 3, 3), [])
        self.assertEqual(list_sum([1, 2, 3, 4], 6, 2), [[2, 4]])
        self.assertEqual(list_sum([1, 2, 3, 4], 6, 3), [[1, 2, 3]])
        self.assertEqual(list_sum([1, 2, 3, 4, 5, 6], 7, 2), [[1, 6], [2, 5], [3, 4]])
        self.assertEqual(list_sum([1, 2, 3, 4, 5, 6], 7, 3), [[1, 2, 4]])
        self.assertEqual(list_sum([1, 2, 3, 4, 5, 6], 8, 2), [[2, 6], [3, 5]])
        self.assertEqual(list_sum([1, 2, 3, 4, 5, 6], 8, 3), [[1, 2, 5], [1, 3, 4]])
        self.assertEqual(list_sum([1, 2, 3, 4, 5, 6], 10, 4), [[1, 2, 3, 4]])


if __name__ == '__main__':
    main()
