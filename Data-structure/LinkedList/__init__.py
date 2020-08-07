class A:
    def __init__(self,name,school):
        self.name=name
        self.school=school
    def __repr__(self):
        str=""
        for key in self.__dict__:
            str += "%s:%s\n"%(key,self.__dict__[key])
        return str
class Node:
    def __init__(self,new_val):
        self.val = new_val
        self.next = None
class Linked_List:
    def __init__(self):
        self.head = None
    def addAtHead(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
    def addAtTail(self,val):
        node = Node(val)
        curnode = self.head
        while curnode.next is not None:
            curnode = curnode.next
        curnode.next = node
