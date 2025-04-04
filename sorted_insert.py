""" For your information:

"""
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
def sorted_insert(head, data):
    new = Node(data)
    if not head or data < head.data:
        new.next = head
        return new
    cur = head
    while cur.next and cur.next.data < data:
        cur = cur.next

    new.next = cur.next
    cur.next = new
    return head
    # Your code goes here.
    # Make sure to return the head of the list.
