from push_and_build_one_two_three import build_one_two_three, push 

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    new = source 
    source = source.next
    new.next = dest
    dest = new
    return Context(source, dest)
# print(move_node(build_one_two_three(), build_one_two_three()))
