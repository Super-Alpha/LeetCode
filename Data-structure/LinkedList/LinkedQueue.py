"""单向链表实现队列，
链表头作为出队列，链表尾作为进队列"""
class Empty(Exception):
    pass
class LinkedQueue:
    #定义类内部节点类
    class _Node:
        __slots__ = "_element","_next"  # __slots__用于限定实例可添加的属性
        def __init__(self,element,next):
            self._element=element  # 单下划线前置私有化属性
            self._next=next
    def __init__(self):
        self._head=None #定义的头节点指针
        self._tail=None #定义的尾节点指针，指向最后一个节点
        self._size=0
    def len(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element
    def dequeue(self):
        """:return:出队列，从链表头出队列
        """
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size-=1
        if self.is_empty():
            self._tail=None
        return answer
    def enqueue(self,e):
        """
         :param e:进队列元素，从链表尾进队列
        :return:null
        """
        newest=self._Node(e,None)
        if self.is_empty():
            self._head=newest
        else:
            self._tail._next=newest
        self._tail=newest
        self._size+=1
queue=LinkedQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())