class Empty(Exception):
    pass
# List实现双向队列
class Deque:
    def __init__(self):
        self.items=[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        if Deque.isEmpty():
            raise Empty("Deque is empty")
        return self.items.pop()
    def removeRear(self):
        if Deque.isEmpty():
            raise Empty("Deque is empty")
        return self.items.pop(0)
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)
# Example One：
def palchecker(string):
    deque=Deque()
    for i in string:
        deque.addRear(i)
    bool=True
    while deque.size()>1 and bool:
        first=deque.removeFront()
        last=deque.removeRear()
        if first!=last:
            bool=False
    return bool

#循环双向队列的实现
class ArrayDeque:
    DEFAULT_CAPACITY=10
    def __init__(self):
        """初始化大小和队列中元素的数量以及第一个元素的索引"""
        self._data=[None]*ArrayDeque.DEFAULT_CAPACITY
        self._size=0
        self._front=0
    def len(self):
        """存储元素的数量"""
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        """返回第一个元素值"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        Last = (self._front + self._size - 1) % len(self._data)
        return self._data[Last]
    def delete_first(self):
        """从队列中取出元素，并更新首元素索引值，以及队列的大小减一"""
        if self.is_empty():
            raise Empty("Queue is empty")
        answer=self._data[self._front]
        self._data[self._front]=None      # help garbage collection
        self._front=(self._front+1)%len(self._data)
        self._size-=1
        #二倍缩减底层数组大小
        if 0<self._size<len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        Last = (self._front + self._size - 1) % len(self._data)
        answer=self._data[Last]
        self._data[Last] = None
        self._size -= 1
        if 0<self._size<len(self._data)//4:
            self._resize(len(self._data)//2)
        return answer
    def add_first(self,e):
        """添加元素到队列中，若所含元素数量等于队列容量，则对队列二倍扩容，队列大小加一"""
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front - 1) % len(self._data)
        self._data[avail]=e
        self._front=avail
        self._size+=1
    def add_last(self,e):
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        Last=(self._front+self._size)%len(self._data)
        self._data[Last]=e
        self._size+=1
    def _resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0
#D=ArrayDeque()
#D.add_first(3)
#print(D.first())
print(-2%2)