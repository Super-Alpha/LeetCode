class Empty(Exception):
    pass
class LinkedQueue:
    """链式队列的实现"""
    #定义类内部节点类
    class _Node:
        __slots__ = "_element","_next"  # __slots__用于限定实例可添加的属性
        def __init__(self,element,next):
            self._element=element  # 单下划线前置包内私有化属性
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

class Tree:
    """定义树的抽象数据结构"""
    class Position:
        def element(self):
            """Return the element stored in this Position"""
            raise NotImplementedError("must be implemented by subclass")
        def __eq__(self, other):
            """Return True if other Position represents the same location"""
            raise NotImplementedError("must be implemented by subclass")
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self==other)
    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")
    def parent(self,p):
        """Return Position representing the p's parent (or None if p is empty)."""
        raise NotImplementedError("must be implemented by subclass")
    def num_children(self,p):
        """Return the number of children that Position p has"""
        raise NotImplementedError("must be implemented by subclass")
    def children(self,p):
        """Generate an iteration of Positions representing p's children"""
        raise NotImplementedError("must be implemented by subclass")
    def _len__(self):
        """Return the total number of elements in the tree"""
        raise NotImplementedError("must be implemented by subclass")
    def is_root(self,p):
        """Return True if Position p represents the root of Tree"""
        return self.root()==p
    def is_leaf(self,p):
        """Return True if Position p does not have any children"""
        return self.num_children(p)==0
    def is_empty(self):
        """Return True if the tree is empty"""
        return len(self)==0
    def depth(self,p):
        """Return the number of levels separating Position p from the root"""
        if self.is_root(p):
            return 0
        else:
            return 1+self.depth(self.parent(p))
    def Tree_Height(self):
        """Return the height of the tree"""
        """一个非空树T的高度等于其所有叶子节点深度的最大值"""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))#positions()尚未定义
    def SubTree_Height(self,p):
        """Return the height of the subtree rooted at Position p"""
        if self.is_leaf(p):
            return 0
        else:
            return 1+max(self.SubTree_Height(c) for c in self.children(p))
    def P_Height(self,p=None):
        """Return the height of the subtree rooted at Position p.
           if p is None,return the height of the entire tree"""
        if p is None:
            p=self.root()
        return self.SubTree_Height(p)
    def __iter__(self):
        """Generate an iteration of the tree's elements"""
        for p in self.positions():
            yield p.element
    """前序遍历的实现(root->left->right)"""
    def preorder(self):
        """Generate a preorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p
    def _subtree_preorder(self,p):
        """Generate a preorder iteration of position in subtree rooted at p"""
        yield p                        #(先生成根位置)遇到叶子节点时，直接生成叶子节点位置，visit p before its subtrees
        for c in self.children(p):                  # for each child c
            for other in self._subtree_preorder(c): # do preorder of c's subtree
                yield other                         # (再生成子节点位置)yielding each to our caller
    """后序遍历的实现(left->right->root)"""
    def postorder(self):
        """Generate a postorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    def _subtree_postorder(self,p):
        """Generate a postorder iteration of positions in subtree rooted at p"""
        for c in self.children(p):              # 遇到叶子节点时，直接跳到 yield p
            for other in self._subtree_postorder(c):
                yield other
        yield p
    """广度优先遍历实现(在访问深度d+1的位置之前先访问深度d的位置)"""
    def breadthfirst(self):
        """Generate a breath-first iteration of the positions of the tree"""
        if not self.is_empty():
            fringe=LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p=fringe.dequeue()
                yield p
                for c in self.children(p):
                    fringe.enqueue(c)

class BinaryTree(Tree):
    """定义二叉树的抽象数据结构"""
    def left(self,p):
        """Return a position representing p's left child.
           Return None if p does not have a left child"""
        raise NotImplementedError("must be implemented by subclass")
    def right(self,p):
        """Return a position representing p's right child.
           Return None if p does not have a right child"""
        raise NotImplementedError("must be implemented by subclass")
    def sibling(self,p):
        """返回位置p节点的兄弟节点的位置,'sibling'='兄、弟、姐、妹'"""
        parent=self.parent(p)
        if parent is None:
            return None
        else:
            if p==self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    def children(self,p):
        """Generate an iteration of Position representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    """二叉树中序遍历的实现(left->root->right)"""
    def inorder(self):
        """Generate an inorder iteration of positions in the tree"""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    def _subtree_inorder(self,p):
        """Generate an inorder iteration of positions in subtree rooted at p"""
        if self.left(p) is not None: # 碰到叶子节点时，直接跳到yield p
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self.right(self.right(p)):
                yield other

class LinkedBinaryTree(BinaryTree):
    """二叉树的链式ADT实现"""
    class _Node:
        __slots__ = "_element","_parent","_left","_right"
        def __init__(self,element,parent=None,left=None,right=None):
            self._element=element
            self._parent=parent
            self._left=left
            self._right=right
    class Position(BinaryTree.Position):
        """用于封装节点"""
        def __init__(self,container,node):
            self._container=container  #容器
            self._node=node
        def element(self):
            return self._node._element
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
    def _validate(self,p):
        """Return associated node,if position is valid.
           在所给的实例未封装之前，验证实例的有效性"""
        if not isinstance(p,self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:
            raise ValueError("p is no longer valid")
        return p._node
    def _make_position(self,node):
        """Return Position instance for given node(or None if no node)
           把节点封装进position实例，并返回给调用者"""
        return self.Position(self,node) if node is not None else "UNLL"
    def __init__(self):
        """Create an initially empty binary tree"""
        self._root=None
        self._size=0
    def __len__(self):
        """Return the total number of elements in the tree"""
        return self._size
    def root(self):
        """Return the root Position of the tree"""
        return self._make_position(self._root)
    def parent(self,p):
        """Return the Position of p's parent"""
        node=self._validate(p)
        return self._make_position(node._parent)
    def left(self,p):
        """Return the Position of p's left child"""
        node=self._validate(p)
        return self._make_position(node._left)
    def right(self,p):
        """Return the Position of p's right child"""
        node=self._validate(p)
        return self._make_position(node._right)
    def num_children(self,p):
        """Return the number of children of Position p"""
        node=self._validate(p)
        count=0
        if node._left is not None:
            count+=1
        if node._right is not None:
            count+=1
        return count
    def _add_root(self,e):
        """Place element e at the root if an empty tree and return new Position.
           if tree nonempty,Raise ValueError"""
        if self._root is not None:
            raise ValueError("Root is exists")
        self._size=1
        self._root=self._Node(e)
        return self._make_position(self._root)
    def _add_left(self,p,e):
        """Create a new left child for Position p,storing element e.
           Return the Position of new node.
           Raise ValueError if Position p is invalid or p already has a left child."""
        node=self._validate(p)
        if node._left is not None:raise ValueError("Left child exists")
        self._size+=1
        node._left=self._Node(e,node)
        return self._make_position(node._left)
    def _add_right(self,p,e):
        """Create a new right child for Position p,storing element e.
                   Return the Position of new node.
                   Raise ValueError if Position p is invalid or p already has a right child."""
        node=self._validate(p)
        if node._right is not None:raise ValueError("Right child exists")
        self._size+=1
        node._right=self._Node(e,node)
        return self._make_position(node._right)
    def _replace(self,p,e):
        """Replace the element at position p with e,and return old element"""
        node=self._validate(p)
        old=node._element
        node._element=e
        return old
    def _delete(self,p):
        """Delete the node at Position p,and replace it with its child,if have(=if any).
           Return the element that had been stored at Position p.
           Raise ValueError if Position p is invalid or p has two child"""
        node=self._validate(p)
        if self.num_children(p)==2:raise ValueError("p has two children")
        child=node._left if node._left else node._right
        if child is not None:
            child._parent=node._parent
        if node is self._root:
            self._root=child
        else:
            parent=node._parent
            if node is parent._left:
                parent._left=child
            else:
                parent._right=child
        self._size-=1
        node._parent=node
        return node._element
    def _attach(self,p,t1,t2):
        """Attach trees t1 and t2 as left and right subtrees of external p"""
        node=self._validate(p)
        if not self.is_leaf(p):raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")
        self._size+=len(t1)+len(t2)
        if not t1.is_empty():
            t1._root._parent=node
            node._left=t1._root
            t1._root=None
            t1._size=0
        if not t2.is_empty():
            t2._root._parent=node
            node._right=t2._root
            t2._root=None
            t2._size=0

if __name__ == '__main__':
    linklisttree=LinkedBinaryTree()

    root=linklisttree._add_root(1)
    linklisttree._add_left(root,2)
    linklisttree._add_right(root,3)

    print(linklisttree.root().element())