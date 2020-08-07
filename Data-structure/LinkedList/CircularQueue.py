"""循环队列"""
class Empty(Exception):
    pass
class CircularQueue:
    #定义类内部节点类
    class _Node:
        __slots__ = "_element","_next"  # __slots__用于限定实例可添加的属性
        def __init__(self,element,next):
            self._element=element        #单下划线前置私有化属性
            self._next=next
    def __init__(self):
        self._tail=None                  #定义的尾节点指针，指向最后一个节点
        self._size=0
    def len(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            raise Empty("CircularQueue is empty")
        head=self._tail._next
        return head._element
    def dequeue(self):
        if self.is_empty():
            raise Empty("CircularQueue is empty")
        head = self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next = head._next   #令尾节点指向第二节点
        self._size-=1
        return head._element
    def enqueue(self,e):
        newest=self._Node(e,None)
        if self.is_empty():
            newest._next=newest           #节点指向本身
        else:
            newest._next = self._tail._next #令新节点指向首节点
            self._tail._next=newest       #令前一节点指向后一节点
        self._tail=newest                 #令尾指针_tail指向新加入的节点
        self._size+=1
circilar=CircularQueue()
circilar.enqueue(1)
circilar.enqueue(2)
print(circilar.dequeue())
print(circilar.dequeue())
print(circilar.is_empty())