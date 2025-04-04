class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if not head or not head.next:
        return head
    cur = Node()
    cur.next = head
    prev = cur

    while prev.next and prev.next.next:
        f = prev.next
        s = f.next

        f.next = s.next
        s.next = f
        prev.next = s
        prev = f 
    return cur.next
