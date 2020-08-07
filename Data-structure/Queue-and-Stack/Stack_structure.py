"""
算法+数据结构=程序j
通过python中的list结构来实现Stack
"""
class Empty(Exception):
    pass
#Stack
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def top(self):
        if self.isEmpty():
            raise Empty("Stack is empty")
        return self.items[-1]
    def pop(self):
        try:
            return self.items[-1]
        except BaseException:
            print("delete fail!")
        finally:
            del self.items[-1]
    def popplus(self):
        if self.isEmpty():
            raise Empty("Stack is empty")
        return self.items.pop()
    def size(self):
        return len(self.items)
def is_matched(expr):
    lefty="({["
    righty=")}]"
    S=Stack()
    for c in expr:
        if c in lefty:
            S.push(c)
        elif c in righty:
            if S.isEmpty():
                return False
            if righty.index(c)!=lefty.index(S.pop()):
                return False
    return S.isEmpty()
string ="[(5+x)-(y+z)]]"
print(is_matched(string))