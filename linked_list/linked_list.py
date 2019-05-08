class Node:
    """双向列表的节点
    """
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return 'Node: {}'.format(self.value)


class DoubleLinkedList:
    """双向列表
    """
    def __init__(self, *args):
        """初始化双向列表
        """
        if len(args) == 0:
            self.head = self.tail = None
        elif len(args) == 1:
            self.head = self.tail = Node(args[0])
        else:
            # 定义头部节点和尾部节点
            head_node = Node(args[0])
            head_node.prev = None
            tail_node = Node(args[-1])
            tail_node.next = None
            # 增加中部节点
            current_node = head_node
            for i in args[1:-1]:
                new_node = Node(i)
                new_node.prev = current_node
                current_node.next = new_node
                current_node = new_node
            current_node.next = tail_node
            tail_node.prev = current_node
            self.head = head_node
            self.tail = tail_node
        return

    def __repr__(self):
        current_node = self.head
        node_value_list = []
        while current_node:
            node_value_list.append(current_node.value)
            current_node = current_node.next
        return 'DoubleLinkedList: {}'.format(node_value_list)

    def search(self, x):
        """通过值搜索出节点
        """
        current_node = self.head
        while current_node:
            if current_node.value == x:
                return current_node
            current_node = current_node.next
        return

    def remove_node(self, node):
        """删除节点
        """
        prev_node = node.prev
        next_node = node.next
        if prev_node is None:
            next_node.prev = None
            self.head = next_node
        elif next_node is None:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = next_node
            next_node.prev = prev_node
        del node
        return

    def remove_value(self, x):
        """删除第一个值等于x的节点

        Args:
            x: 节点Node的值value
        Return:
            DolubleLinkedList的头部节点
        """
        node = self.search(x)
        if node:
            self.remove_node(node)
            return self.head
        else:
            raise Exception('x not in linked list')
