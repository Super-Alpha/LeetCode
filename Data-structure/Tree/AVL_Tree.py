"""AVL树的python实现"""

class TreeNode:
    """
    创建树节点
    """
    def __init__(self,key,val,left=None,right=None,parent=None,balanceFactor=0):
        """
        :param key:键值
        :param val: 数据项
        :param left: 左子节点
        :param right: 右子节点
        :param parent: 父节点
        :param balanceFactor: 平衡因子
        """
        self.key=key
        self.payload=val
        self.leftChild=left
        self.rightChild=right
        self.parent=parent
        self.balanceFactor=balanceFactor

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        """判断该节点是不是左子节点"""
        return self.parent and self.parent.leftChild==self

    def isRightChild(self):
        """判断该节点是不是右子节点"""
        return self.parent and self.parent.rightChild==self

    def isRoot(self):
        """判断该节点是不是根节点"""
        return not self.parent

    def isLeaf(self):
        """判断该节点是不是叶子节点,a or b， a b均为假则返回假，a b有一个为真则返回真"""
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        """判断该节点是否有子节点"""
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        """判断该节点是否有左、右子节点"""
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        """替换根节点,即二叉搜索树的唯一根节点"""
        self.key=key
        self.payload=value
        self.leftChild=lc
        self.rightChild=rc
        if self.hasLeftChild():
            self.leftChild.parent=self
        if self.hasRightChild():
            self.rightChild.parent=self

    def findSuccessor(self):
        """
        寻找后继节点
        :return:
        """
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ=self.parent
                else:
                    self.parent.rightChild=None
                    succ=self.parent.findSuccessor()
                    self.parent.rightChild=self
        return succ

    def findMin(self):
        current=self
        while current.hasLeftChild():
            #到左下角
            current=current.leftChild
        return current

    def spliceOut(self):
        """
        摘出节点
        :return:
        """
        if self.isLeaf():
            #摘出叶节点
            if self.isLeftChild():
                self.parent.leftChild=None
            else:
                self.parent.rightChild=None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild=self.leftChild
                else:
                    self.parent.rightChild=self.leftChild
                self.leftChild.parent=self.parent
            else:
                #摘出带右子节点的节点
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChild:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem


class AVLTree:
    """构建"""
    def __init__(self):
        self.root=None #root成员引用根节点TreeNode
        self.size=0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__() #引用TreeNode中定义的迭代器

    def put(self,key,val):
        """
        插入key，构造AVL树
        :param key:
        :param val:
        :return:
        """
        if self.root:
            self._put(key,val,self.root) # 从树根开始，搜索二叉树
        else:
            self.root=TreeNode(key,val)
        self.size=self.size+1

    def _put(self,key,val,currentNode):
        """
        搜索树
        :param key:
        :param val:
        :param currentNode:
        :return:
        """
        if key<currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.leftChild) #调整因子
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild=TreeNode(key,val,parent=currentNode)
                self.updateBalance(currentNode.rightChild) #调整因子
    #更新平衡因子
    def updateBalance(self,node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node) #重新平衡
            return
        if node.parent!=None:
            if node.isLeftChild():
                node.parent.balanceFactor+=1
            elif node.isRightChild():
                node.parent.balanceFactor-=1
            if node.parent.balanceFactor!=0:
                self.updateBalance(node.parent)#调整父节点因子

    def rebalance(self,node):
        #右重需左旋
        if node.balanceFactor < 0:                 # 若该节点的平衡因子<0，则
            if node.rightChild.balanceFactor > 0:  # 若该节点的右子节点的平衡因子>0，则
                self.rotateRight(node.rightChild)  # 右旋转该节点的右子节点
                self.rotateLeft(node)                  # 左旋转该节点
            else:
                self.rotateLeft(node)
        #左重需右旋
        elif node.balanceFactor > 0:               # 若该节点的平衡因子>0，则
            if node.leftChild.balanceFactor < 0:   # 若该节点的左子节点的平衡因子<0，则
                self.rotateLeft(node.leftChild)    # 左旋转该节点的左子节点
                self.rotateRight(node)
            else:
                self.rotateRight(node)

    def rotateLeft(self,rotRoot):
        """
        左旋（右重的树要左旋转才平衡）
        :param rotRoot:
        :return:
        """
        newRoot = rotRoot.rightChild                # 待旋转节点的右子节点设为新的根节点
        rotRoot.rightChild = newRoot.leftChild      # 新根的原左子节点作为原根的新右子节点
        if newRoot.leftChild != None:              # 若新根原来有左子节点，则
            newRoot.leftChild.parent = rotRoot      # 将新根的原左子节点的父节点指向原根
        newRoot.parent = rotRoot.parent             # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():                        # 若原根是树的根节点，则
            self.root = newRoot                     # 将新根设为树的根节点
        else:                                       # 若原根不是树的根节点，则
            if rotRoot.isLeftChild():               # 若原根是左子树，则
                rotRoot.parent.leftChild = newRoot   # 将原根的父节点的左子节点指向新根
            else:                                    # 若原根是右子树，则
                rotRoot.parent.rightChild = newRoot  # 将原根的父节点的右子节点指向新根
        newRoot.leftChild = rotRoot                  # 将新根的左子节点指向原根
        rotRoot.parent = newRoot                     # 将原根的父节点指向新根

        # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor,0)

        # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor,0)

    def rotateRight(self,rotRoot):
        """
        右旋（左重的树要右旋转才平衡）
        :param rotRoot:
        :return:
        """
        newRoot = rotRoot.leftChild                # 待旋转节点的左子节点设为新的根节点
        rotRoot.leftChild = newRoot.rightChild     # 新根的原右子节点作为原根的新左子节点
        if newRoot.rightChild != None:             # 若新根原来有右子节点，则
            newRoot.rightChild.parent = rotRoot     # 将新根的原右子节点的父节点指向原根
        newRoot.parent = rotRoot.parent              # 新根的父节点指向原根的父节点
        if rotRoot.isRoot():                         # 若原根是树的根节点，则
            self.root = newRoot                      # 将新根设为树的根节点
        else:                                        # 若原根不是树的根节点，则
            if rotRoot.isLeftChild():                # 若原根是左子树，则
                rotRoot.parent.leftChild = newRoot    # 将原根的父节点的左子节点指向新根
            else:                                     # 若原根是右子树，则
                rotRoot.parent.rightChild = newRoot    # 将原根的父节点的右子节点指向新根
        newRoot.rightChild = rotRoot                   # 将新根的右子节点指向原根
        rotRoot.parent = newRoot                       # 将原根的父节点指向新根

        # 更新原根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor,0)

        # 更新新根节点的平衡因子，被移动的子树内的节点的平衡因子不受旋转影响，计算方法见上方注释
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(0,rotRoot.balanceFactor)

    def __setitem__(self, key, value):
        """索引赋值,例如：test[key]=value"""
        self.put(key,value)

    def get(self,key):
        """
        在树中找到key所在的节点取到payload
        :param key:
        :return: payload
        """
        if self.root:
            res=self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self,key,currentNode):
        """
        找到键为key的节点
        :param key:
        :param currentNode:
        :return:
        """
        if not currentNode:
            return None
        elif currentNode.key==key:
            return currentNode
        elif key<currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self, item):
        """
        索引取值，例如：得到test[item]
        :param item:
        :return:
        """
        return self.get(item)

    def __contains__(self, item):
        """
        归属判断,例如：item in test
        :param item:
        :return:
        """
        if self._get(item,self.root):
            return True
        else:
            return False

    def delete(self,key):
        """
        用_get找到要删除的节点，然后调用remove来删除，找不到则提示错误
        :param key:
        :return:
        """
        if self.size>1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size=self.size-1
            else:
                raise KeyError("Error.key not in tree")
        elif self.size==1 and self.root.key==key:
            self.root=None
            self.size=self.size-1
        else:
            raise KeyError("Error,key not in tree")

    def __delitem__(self, key):
        """
        例如：del test[key]
        :param key:
        :return:
        """
        self.delete(key)

    @staticmethod
    def remove(currentNode):
        if currentNode.isLeaf():# leaf
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild=None
            else:
                currentNode.parent.rightChild=None

        elif currentNode.hasBothChildren():
            # this node has two child
            succ=currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key=succ.key
            currentNode.payload=succ.payload

        else:# this node has one child
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    #左子节点删除
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.leftChild
                elif currentNode.isRightChild():
                    #右子节点删除
                    currentNode.leftChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.leftChild
                else:
                    #根节点删除
                    currentNode.replaceNodeData(currentNode.leftChild.key,
                                                currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,
                                                currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    #左子节点删除
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.leftChild=currentNode.rightChild
                elif currentNode.isRightChild():
                    #右子节点删除
                    currentNode.rightChild.parent=currentNode.parent
                    currentNode.parent.rightChild=currentNode.rightChild
                else:
                    #根节点删除
                    currentNode.replaceNodeData(currentNode.rightChild.key,
                                                currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild,
                                                currentNode.rightChild.rightChild)


if __name__ == '__main__':
    mytree=AVLTree()
    mytree[3]="red"
    mytree[4]="blue"
    mytree[6]="yellow"
    mytree[2]="at"
    mytree[2]="at"
    print(len(mytree))
    print(3 in mytree)
    print(mytree[6])
    del mytree[3]
    for key in mytree:
        print(key,mytree[key])