from unittest import TestCase, main
from linked_list import DoubleLinkedList


class DoubleLinkedListTest(TestCase):
    def test_remove_value(self):
        linked_list = DoubleLinkedList(1, 2, 3, 1, 4)
        self.assertEqual(linked_list.remove_value(1), linked_list.head)
        self.assertEqual(linked_list.remove_value(1).value, 2)


if __name__ == '__main__':
    main()
