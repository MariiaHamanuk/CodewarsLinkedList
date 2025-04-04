class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
# def push(head, data):
#     if not head:
#         if not data:
#             return None
#         return Node(data)

#     # cur = head.next
#     head.next = Node(head.data)
#     head.data = data
#     # cur.data = data
#     return head

#     # return Node(None)

# def build_one_two_three():
#     lst = None

#     for el in [3, 2, 1]:

#             # print(lst.data)
#             # print(lst.next)
#         lst = push(lst, el)
#         # print(lst.data)
#         # print(lst.next)
#     return lst
    # return Node(None)
def remove_duplicates(head):
    if not head:
        return None
    cur = head
    while cur and cur.next:
#         if cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
    # Your code goes here.
    # Remember to return the head of the list.
