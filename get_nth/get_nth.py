class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return f'{self.data}'
def get_nth(node, index):
    lst = []
    lst.append(node.data)
    for i in range(index):
        lst.append(node.data)
        if not node.next:
            break
        node.data = node.next
        node.next = node.next.next
        while isinstance(node.data, Node):
            node.data = node.data.data

    if (len(lst)-1) < index or index<0:
        raise ValueError
    return Node(node.data, node.next)
