# A unival tree (which stands for "universal value")
# is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
UNIVAL_SUBTREES_COUNT = 0


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def num_unival_subtrees(root: Node) -> int:
    global UNIVAL_SUBTREES_COUNT
    UNIVAL_SUBTREES_COUNT = 0

    def encode(node):
        global UNIVAL_SUBTREES_COUNT
        if node:
            nodes_exist = node.left and node.right
            if nodes_exist and node.val == node.left.val and node.val == node.right.val:
                UNIVAL_SUBTREES_COUNT += 1
            # last node
            if not nodes_exist:
                UNIVAL_SUBTREES_COUNT += 1
            encode(node.left)
            encode(node.right)

    encode(root)
    return UNIVAL_SUBTREES_COUNT


node = Node(
    '0',
    left=Node('1'),
    right=Node(
        '0',
        left=Node(
            '1',
            left=Node('1'),
            right=Node('1')
        ),
        right=Node('0')
    )
)
print(num_unival_subtrees(node))
