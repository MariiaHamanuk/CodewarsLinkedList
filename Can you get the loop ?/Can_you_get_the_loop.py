# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
def loop_size(node):
    '''
    detects the loop size (I used Floid`s algo with fast (second - s)  and slow (first - f) nodes ) 
    '''
    f = s = node
    while True:

        f = f.next
        s = s.next.next

        if f == s:
        
            counter = 0
            cur = f.next
            while cur != f:

                cur = cur.next
                counter += 1
            return counter + 1
