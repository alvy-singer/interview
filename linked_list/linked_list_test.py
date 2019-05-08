from unittest import TestCase, main
from linked_list import DoubleLinkedList, LinkedList


class DoubleLinkedListTest(TestCase):
    def test_remove_value(self):
        linked_list = DoubleLinkedList(1, 2, 3, 1, 4)
        rv = linked_list.remove_value(1)
        self.assertEqual(rv, linked_list.head)
        self.assertEqual(rv.value, 2)

class LinkedListTest(TestCase):
    """测试链表
    """

    def test_add(self):
        pass

    def test_delete(self):
        pass

    def test_find(self):
        pass


if __name__ == '__main__':
    main()
