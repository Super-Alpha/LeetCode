
"""二叉树的前序、中序、后序遍历"""


class Node:
    def __init__(self,root="NIL"):
        self.root = root
        self.left = None
        self.right = None
        self.out_list_temp =[]
        self.answer = 0


class Tree(Node):
    answer = 0
    def build(self,tree,node_list,i):
        if i<len(node_list):
            if node_list[i] == "NIL":
                return None
            else:
                tree = Node(node_list[i])
                tree.left = self.build(tree.left,node_list,i*2+1)
                tree.right = self.build(tree.right,node_list,i*2+2)
            return tree
        return tree
    def preorder_traversal(self,tree):
        """
        前序遍历
        :param tree:
        :return:
        """
        if tree.root != None:
            self.out_list_temp.append(tree.root)
        if tree.left != None:
            self.preorder_traversal(tree.left)
        if tree.right != None:
            self.preorder_traversal(tree.right)
        return self.out_list_temp
    def preorder_traversal_print(self,tree):
        print(self.preorder_traversal(tree))
        self.out_list_temp=[]
    def inorder_traversal(self,tree):
        """
        中序遍历
        :param tree:
        :return:
        """
        if tree.left != None:
            self.inorder_traversal(tree.left)
        if tree.root != None:
            self.out_list_temp.append(tree.root)
        if tree.right != None:
            self.inorder_traversal(tree.right)
        return self.out_list_temp
    def inorder_traversal_print(self,tree):
        print(self.inorder_traversal(tree))
        self.out_list_temp=[]
    def postorder_traversal(self,tree):
        """
        后序遍历
        :param tree:
        :return:
        """
        if tree.left != None:
            self.postorder_traversal(tree.left)
        if tree.right != None:
            self.postorder_traversal(tree.right)
        if tree.root != None:
            self.out_list_temp.append(tree.root)
        return self.out_list_temp
    def postorder_traversal_print(self,tree):
        print(self.postorder_traversal(tree))
        self.out_list_temp=[]
    def DFS(self,rootNode):
        """
        深度优先遍历，迭代实现
        :param rootNode:
        :return:
        """
        if rootNode:
            res = []
            stack = [rootNode]
            while stack:
                currentNode = stack.pop()
                res.append(currentNode.val)
                if currentNode.right:
                    stack.append(currentNode.right)
                if currentNode.left:
                    stack.append(currentNode.left)
        return res
    def BFS(self,rootNode):
        """
        广度优先遍历，迭代实现
        :param rootNode: 根节点
        :return: [[],....]
        """
        if rootNode == "NIL":
            return []
        queue = [rootNode]  # 在队列中传入的是结点
        result = []
        while queue:
            temp = [] #保存结点的值
            for i in range(len(queue)):
                tempNode = queue.pop(0)
                temp.append(tempNode.root)
                if tempNode.left != None:
                    queue.append(tempNode.left)
                if tempNode.right != None:
                    queue.append(tempNode.right)
            result.append(temp)
        return result

    def MaximumDepth(self,rootNode,depth):
        """
        :param rootNode: 根节点
        :param depth: 0 或 1
        :return:
        """
        if rootNode == None:
            return 0
        if rootNode.left == None and rootNode.right == None:
            self.answer = max(self.answer,depth)
        self.MaximumDepth(rootNode.left,depth+1)
        self.MaximumDepth(rootNode.right,depth+1)
        return self.answer

    def MaximumHigh(self,rootNode):
        """
        :param rootNode: 根节点
        :return:
        """
        if rootNode == None:
            return 0
        else:
            return max(self.MaximumHigh(rootNode.left),self.MaximumHigh(rootNode.right))+1

    def demo(self,node,target,path,res,finish):
        if finish==1 or node=="NIL":
            return
        path.append(node.root)
        if node==target:
            finish=1
            res.extend(path)
        self.demo(node.left,target,path,res,finish)
        self.demo(node.right,target,path,res,finish)
        path.pop()


def preorder_traversal_find_nodeval(tree, val):
    """
    前序遍历判断给定节点值是否存在
    :param tree:
    :return:
    """
    if tree:
        if tree.root == val:
            return True
    if tree.left:
        left=preorder_traversal_find_nodeval(tree.left, val)
        if left:
            return True
    if tree.right:
        right=preorder_traversal_find_nodeval(tree.right, val)
        if right:
            return True
    return False


if __name__ == '__main__':
    node_list = [3,5,1,6,2,0,8,'NIL','NIL',7,4]
    tree = Tree()
    my_tree = tree.build(None,node_list,0)
    tree.preorder_traversal_print(my_tree)
    tree.inorder_traversal_print(my_tree)
    tree.postorder_traversal_print(my_tree)
    print(tree.BFS(my_tree))
    print(tree.MaximumDepth(my_tree,1))
    print(tree.MaximumHigh(my_tree))
    print(preorder_traversal_find_nodeval(my_tree,1))











