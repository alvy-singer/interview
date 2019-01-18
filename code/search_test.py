from unittest import TestCase, main
from search import Search


class SearchTest(TestCase):
    def test_binary_search(self):
        my_list = [1]
        self.assertEqual(Search.binary_search(my_list, 1), 0)
        self.assertEqual(Search.binary_search(my_list, 2), False)
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(Search.binary_search(my_list, 1), 0)
        self.assertEqual(Search.binary_search(my_list, 2), 1)
        self.assertEqual(Search.binary_search(my_list, 3), 2)
        self.assertEqual(Search.binary_search(my_list, 4), 3)
        self.assertEqual(Search.binary_search(my_list, 5), 4)
        self.assertEqual(Search.binary_search(my_list, 6), 5)
        self.assertEqual(Search.binary_search(my_list, 7), 6)
        self.assertEqual(Search.binary_search(my_list, 8), 7)
        self.assertEqual(Search.binary_search(my_list, 9), 8)
        self.assertEqual(Search.binary_search(my_list, 10), 9)
        self.assertEqual(Search.binary_search(my_list, 11), False)


if __name__ == '__main__':
    main()
