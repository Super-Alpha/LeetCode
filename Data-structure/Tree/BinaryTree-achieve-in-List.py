"""
insertLeft/insertRight #将新节点插入树中作为其直接的左/右子节点
getRootVal/setRootVal #取得或设置根节点
getLeftChild/getRightChild #返回左/右子树
"""
BinaryTree=["a",["b",["d",[],[]],["e",[],[]]],["c",["f",[],[]],[]]]
def BinaryTree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t = root.pop(1)  # pop(1)返回该节点处的元素root[1]给t后，并删除root[1]
    if len(t)>1:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>1:
        root.insert(2,[newBranch,[],t])
    else:
        root.insert(2,[newBranch,[],[]])
    return root
def getRootVal(root):
    return root[0]
def setRootVal(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    r=BinaryTree(3)
    insertLeft(r,4)
    insertLeft(r,5)
    print(getLeftChild(r))
    insertRight(r,6)
    insertRight(r,7)
    print(getRightChild(r))
    print(len(r))

