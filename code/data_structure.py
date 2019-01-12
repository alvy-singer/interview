class Node:
    """字典树trie的节点
    """
    def __init__(self, value=None):
        self.value = value
        self.children = []

    def __str__(self):
        return 'Node:value is {}'.format(self.value)

    def __repr__(self):
        return str(self.value)

    def add_child(self, node):
        children = self.children
        children.append(node)
        self.children = children


class Trie:
    """字典树
    """

    def __init__(self):
        self.root = Node()

    def add(self, words):
        """增加单词
        """
        current_node = self.root
        for i, v in enumerate(words):
            in_current_node_children = False
            for node in current_node.children:
                if node.value == v:
                    in_current_node_children = True
                    current_node = node
                    break
            if in_current_node_children:
                continue
            else:
                for_add_node = current_node
                for w in words[i:]:
                    new_node = Node(w)
                    for_add_node.add_child(new_node)
                    for_add_node = new_node
                break


class Stack:
    """栈
    """
    def __init__(self, *args):
        self.items = list(args)

    def __repr__(self):
        return 'Stack {}'.format(str(self.items))

    def __getitem__(self, index):
        return self.items[index]

    def push(self, value):
        self.items.append(value)

    def pop(self):
        self.items.pop()
