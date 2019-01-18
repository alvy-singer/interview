from unittest import TestCase, main
from sort import Sort


class SortTest(TestCase):
    def test_second_largest(self):
        self.assertEqual(Sort.second_largest([1, 1]), 'no second')
        self.assertEqual(Sort.second_largest([1, 2]), 1)
        self.assertEqual(Sort.second_largest([3, 1, 2]), 2)
        self.assertEqual(Sort.second_largest([3, 1, 2, 3]), 2)
        self.assertEqual(Sort.second_largest([4, 3, 1, 2, 3]), 3)


if __name__ == '__main__':
    main()
