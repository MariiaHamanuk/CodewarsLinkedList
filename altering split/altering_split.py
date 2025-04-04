class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if not head or not head.next:
        raise ValueError
#     if head.next.next:
    f = head
    s = head.next

    first_current = f
    second_current = s

    head = head.next.next
    flag = True
    
    while head:
        
        if flag:
            first_current.next = head
            first_current = first_current.next
        else:
            second_current.next = head
            

            second_current = second_current.next
        
        head = head.next
        flag = not flag
    
    first_current.next = None
    second_current.next = None

    return Context(f, s)
    # Your code goes here.
    # Remember to return the context.
