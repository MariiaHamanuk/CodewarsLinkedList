class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    def __str__(self):
        return f'{self.data}'

def stringify(node):
    '''
    makes string out of nodes 
    '''
    string = ''
    while node.data is not None:
        if node.data is None:
            break
        string += f'{node.data} -> '
        print(node.data)
        if node.next is not None:
            node.data = node.next.data
            node.next = node.next.next
        else:
            return string + 'None'
print(stringify(Node(1, Node(2, Node(3)))))
