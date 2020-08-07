# Time：2020/3/2410:54
class Node:
    def __init__(self,val=None,children=None):
        self.val = val
        self.children = children
class Solution:
    def __init__(self):
        self.result = []
    def preorder(self,root):
        if root == None:
            return
        self.result.append(root.val)
        for i in root.children:
            self.preorder(i)
        return self.result
    def postorder(self,root):
        if root == None:
            return
        for i in root.children:
            self.postorder(i)
        self.result.append(root.val)