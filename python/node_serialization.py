from collections.abc import Iterator
NODE_END_MARKER = '-'


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root: Node) -> list:
    node_list = []

    def encode(node):
        if node is None:
            node_list.append(NODE_END_MARKER)
        else:
            node_list.append(node.val)
            encode(node.left)
            encode(node.right)

    encode(root)
    return ' '.join(node_list)


def deserialize(node_values: str) -> Node:
    def decode(node_values_iterator: Iterator) -> Node:
        node_value = next(node_values_iterator)
        if node_value == NODE_END_MARKER:
            return None
        node = Node(node_value)
        node.left = decode(node_values_iterator)
        node.right = decode(node_values_iterator)
        return node

    node_values_iterator = iter(node_values.split())
    return decode(node_values_iterator)


node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_node = serialize(node)
print(serialized_node)

deserialized_node = deserialize(serialized_node)

assert deserialize(serialize(node)).left.left.val == 'left.left'
