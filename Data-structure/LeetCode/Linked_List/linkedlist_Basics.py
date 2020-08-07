# Time：2020/5/2310:39
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def add(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1
    def output(self):
        for i in range(self.size):
            print(self.head.val)
            self.head = self.head.next
class Solution:
    def __init__(self):
        self.linklist = LinkedList()
        self.prev = None
        self.add_val()
    def add_val(self):
        for i in range(5):
            self.linklist.add(i)
        self.reverse(self.linklist.head)
    def reverse(self,head):
        while head:
            temp = head.next
            head.next = self.prev
            self.prev = head
            head = temp
        #return prev
    def test(self):
        for i in range(5):
            print(self.prev.val)
            self.prev = self.prev.next
solution = Solution()
solution.test()
