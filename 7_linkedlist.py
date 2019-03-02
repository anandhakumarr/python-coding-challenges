""" Linked list with Append, Length, Remove, Get and Display operations """

class Node(object):
    """node class"""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedListClass(object):
    """Manipulating linked list"""
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        start = 0
        while cur_node.next != None:
            start+=1
            cur_node = cur_node.next
        return start

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        return elems

    def get(self,index):
        if index >= self.length(): return "Data out of range"
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            if index == cur_index: return cur_node.data
            cur_index += 1

    def erase(self,index):
        if index >= self.length(): return "Data out of range"
        cur_index = 0
        cur_node = self.head
        while cur_node.next != None:
            previous_node = cur_node
            cur_node = cur_node.next
            if index == cur_index:
                previous_node.next = cur_node.next
            cur_index += 1


mylist = LinkedListClass()

print "Length " + str(mylist.length())
print mylist.display()

mylist.append(0)
mylist.append(1)
mylist.append(2)
mylist.append(3)

print "Length " + str(mylist.length())
print mylist.display()

print mylist.get(3)
print mylist.erase(2)
print mylist.display()
