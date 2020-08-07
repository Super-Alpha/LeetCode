"""单向链表实现栈"""
class Empty(Exception):
    pass
class LinkedStack:
    #定义类内部节点类
    class _Node:
        """__slots__定义的属性仅对当前类的实例起作用，对继承的子类是不起作用的"""
        __slots__ = "_element","_next" # __slots__用于限定实例可添加的属性
        def __init__(self,element,next):
            self._element=element #单下划线前置私有化属性
            self._next=next
    def __init__(self):
        self._head=None
        self._size=0
    def len(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,e):
        self._head=self._Node(e,self._head)
        self._size+=1
    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element
    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        answer=self._head._element #若不为空，此时self._head也是_Node()的实例化对象
        self._head=self._head._next
        self._size-=1
        return answer
stack=LinkedStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.len())