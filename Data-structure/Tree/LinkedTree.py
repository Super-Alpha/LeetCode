class BinaryTree:
    """链式实现二叉树"""
    def __init__(self,rootObj):
        """
        设置节点
        :param rootObj: 根节点数据项
        """
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
    def insertLeft(self,newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.leftChild=self.leftChild
            self.leftChild=t
    def insertRight(self,newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            t=BinaryTree(newNode)
            t.rightChild=self.rightChild
            self.rightChild=t
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setRootVal(self,obj):
        self.key=obj
    def getRootVal(self):
        return self.key
    def preorder(self):
        """前序遍历"""
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()
    def inorder(self):
        """中序遍历"""
        if self.leftChild:
            self.leftChild.inorder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inorder()
    def lastorder(self):
        """后序遍历"""
        if self.leftChild:
            self.leftChild.lastorder()
        if self.rightChild:
            self.rightChild.lastorder()
        print(self.key)

if __name__ == '__main__':
    mytree=BinaryTree(1)
    mytree.insertLeft(2)
    mytree.insertRight(3)
    """mytree.getLeftChild().setRootVal("hello")
    l=mytree.getLeftChild()
    r=mytree.getRightChild()
    print(l.getRootVal())"""
    print(mytree.preorder())
    print(mytree.inorder())
    print(mytree.lastorder())