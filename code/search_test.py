from unittest import TestCase, main
from search import Search


class SearchTest(TestCase):
    def test_binary_search(self):
        my_list = [1]
        self.assertEqual(Search.binary_search(my_list, 1), True)
        self.assertEqual(Search.binary_search(my_list, 2), False)
        my_list = [1, 2, 3, 4, 5, 6]
        self.assertEqual(Search.binary_search(my_list, 1), True)
        self.assertEqual(Search.binary_search(my_list, 2), True)
        self.assertEqual(Search.binary_search(my_list, 3), True)
        self.assertEqual(Search.binary_search(my_list, 4), True)
        self.assertEqual(Search.binary_search(my_list, 5), True)
        self.assertEqual(Search.binary_search(my_list, 6), True)
        self.assertEqual(Search.binary_search(my_list, 7), False)


if __name__ == '__main__':
    main()
