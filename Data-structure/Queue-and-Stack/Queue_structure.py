"""
Achieve Queue by List
"""
class Empty(Exception):
    pass
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
class ArrayQueue:
    DEFAULT_CAPACITY=10
    def __init__(self):
        """初始化大小和队列中元素的数量以及第一个元素的索引"""
        self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
        self._size=0
        self._front=0
    def __len__(self):
        """存储元素的数量"""
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        """返回第一个元素值"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._data[self._front]
    def dequeue(self):
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
    def enqueue(self,e):
        """添加元素到队列中，若所含元素数量等于队列容量，则对队列二倍扩容，队列大小加一"""
        if self._size==len(self._data):
            self._resize(2*len(self._data))
        avail=(self._front+self._size)%len(self._data)
        self._data[avail]=e
        self._size+=1
    def _resize(self,cap):
        old=self._data
        self._data=[None]*cap
        walk=self._front
        for k in range(self._size):
            self._data[k]=old[walk]
            walk=(1+walk)%len(old)
        self._front=0
#Example One:
def hotpotato(namelist,num):
    simqueue=ArrayQueue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

