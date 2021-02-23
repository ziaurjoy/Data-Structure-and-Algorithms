


# Binary Search Tree(BST)

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return repr(self.data)

    def add_left(self, node):
        self.left = node
        if node is not None:
            node.parent = self

    def add_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self

def bst_insert(root, node):
    last_node = None
    current_node = root
    while current_node is not None:
        last_node = current_node
        if node.data < current_node.data:
            current_node = current_node.left
        else:
            current_node = current_node.right
    if last_node is None:
        root = node
    elif node.data < last_node.data:
        last_node.add_left(node)
    else:
        last_node.add_right(node)
    return root

def create_bst():
    root = TreeNode(10)
    for item in [5, 17, 3, 7, 12, 19, 1, 4]:
        node = TreeNode(item)
        root = bst_insert(root, node)
    return root

if __name__ == '__main__':
    root = create_bst()
    print(root)


def search_bst(node, key):
    while node is not None:
        if node.data == key:
            return node
        if key < node.data:
            node = node.left
        else:
            node = node.right

if __name__ == '__main__':
    root = create_bst()
    for key in [7, 8]:
        print('searching key', key)
        result = search_bst(root, key)
        print(result)
