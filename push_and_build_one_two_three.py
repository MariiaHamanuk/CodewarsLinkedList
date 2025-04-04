
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    # def __str__(self):
    #     return f'{self.data}'
def push(head, data):
    if not head:
        if not data:
            return None
        return Node(data)

    # cur = head.next
    head.next = Node(head.data)
    head.data = data
    # cur.data = data
    return head

    # return Node(None)

def build_one_two_three():
    lst = None

    for el in [3, 2, 1]:

            # print(lst.data)
            # print(lst.next)
        lst = push(lst, el)
        # print(lst.data)
        # print(lst.next)
    return lst
    # return Node(None)
# print(build_one_two_three().next.next)
