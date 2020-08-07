
"""
class student:
    def __init__(self,name):
        self.name=name
    def __eq__(self, other):
        return self.__dict__==other.__dict__
    def __ne__(self, other):
        raise NotImplementedError("error")
class xiaoming (student):
    def __init__(self,age,sex):
        super(xiaoming,self).__init__("xiao hong")
        self.age=age
        self.sex=sex
def test():
    Stu=student("xiao ming")
    ming=xiaoming(18,"man")
def max1():
    for i in range(10):
        yield i
def exam():
    for i in max1():
        print(i)

class TreeNode:
    def __init__(self,val=-1):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = TreeNode()
    def add(self,data):
        pass"""
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    while n>1:
        return fib(n-1)+fib(n-2)
print(fib(6))







