class Queue:
    def __init__(self):
        self.item = []
    def enqueue(self,key):
        self.item.append(key)
    def dequeue(self):
        a=self.item.pop(0)
        return a
class CirQueue:
    def __init__(self,Length):
        self.item = [Length]
        self.length = Length
    def Front(self):
        return self.item[0]
    def Rear(self):
        return self.item[self.length-1]
class Stack:
    def __init__(self):
        self.stack = []
    def push(self,key):
        self.stack.append(key)
    def pop(self):
        a=self.stack.pop()
        return a
    def top(self):
        if len(self.stack)==0:
            return
        else:
            return self.stack[len(self.stack)-1]
    def getMin(self):
        self.stack.sort()
        return self.stack[0]
if __name__ == '__main__':
    """queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.item)
    print(queue.dequeue())
    print(queue.dequeue())
    """
    s = Stack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())

