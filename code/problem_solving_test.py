from unittest import TestCase, main
from problem_solving import time_angle, binary_search


class ProblemSolvingTest(TestCase):

    def test_time_angle(self):
        self.assertEqual(time_angle(12, 0, 0), 0.0)
        self.assertEqual(time_angle(1, 0, 0), 360 * 1 / 12)
        self.assertEqual(time_angle(13, 0, 0), 360 * 1 / 12)
        self.assertEqual(time_angle(1, 30, 30), 134.75)

    def test_binary_search(self):
        self.assertEqual(binary_search([]), 0)
        self.assertEqual(binary_search([1]), 0)
        self.assertEqual(binary_search([1, 2]), 1)
        self.assertEqual(binary_search([2, 1]), 0)
        self.assertEqual(binary_search([1, 2, 3]), 2)
        self.assertEqual(binary_search([3, 1, 2]), 0)
        self.assertEqual(binary_search([2, 3, 1]), 1)
        self.assertEqual(binary_search([1, 2, 3, 4]), 3)
        self.assertEqual(binary_search([4, 1, 2, 3]), 0)
        self.assertEqual(binary_search([3, 4, 1, 2]), 1)
        self.assertEqual(binary_search([2, 3, 4, 1]), 2)


if __name__ == '__main__':
    main()
