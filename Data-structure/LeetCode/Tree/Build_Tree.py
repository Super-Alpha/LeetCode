# @Time：2020/7/1910:59
"""
将二叉树进行宽度优先遍历，可得到顺序存储二叉树列表

顺序存储二叉树(即将二叉树元素存储到列表)的特点：
1、顺序二叉树通常只考虑完全二叉树
2、第n个元素的左子节点为2*n+1
3、第n个元素的右子节点为2*n+2
4、第n个元素的父节点为(n-1)/2
5、n表示二叉树中的第几个元素(在列表中从0开始)
"""
# 实现顺序存储二叉树的遍历
class ArrBinaryTree:
    def __init__(self,arr):
        self.arr=arr # [1,2,3,4,5,6,7]

    def __preorder(self,index):
        """
        前序遍历
        :param index:数组下标
        :return:
        """
        if self.arr is None or len(self.arr) == 0:
            print("Array is null,not output with preorder of BinaryTree")
        print(self.arr[index])
        if (index*2+1) < len(self.arr):
            self.__preOrder(index*2+1)
        if (index*2+2) < len(self.arr):
            self.__preOrder(index*2+2)

    def outside_preOrder_API(self,index):
        """
        重载，为了外部调用简洁
        :param index:
        :return:
        """
        self.__preOrder(index)


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left = None
        self.right = None

class BuildTree:
    def __init__(self):
        self.temp=[1,2,3,4]
        pass

    def buildBST(self,l,r):
        """
        依据升序列表，创建二叉搜索树
        :param l: 0
        :param r: len(self.temp)
        :return: node
        """
        mid = (l + r) // 2  # 向下取整
        root = TreeNode(self.temp[mid])
        if l <= mid - 1:
            root.left = self.buildBST(l,mid - 1)
        if mid + 1 <= r:
            root.right = self.buildBST(mid + 1,r)
        return root

    def reConstructBinaryTree(self,preorder,inorder):
        """
        通过前序遍历列表和中序遍历列表构建二叉树
        :param preorderlist: 前序遍历列表
        :param inorderlist: 中序遍历列表
        :return: 树的根节点
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
            # preorder = [8,5,1,7,10,12]
            # inorder = [1,5,7,8,10,12]
        root_index = inorder.index(preorder[0])  # 在中序遍历列表中获得根节点索引
        left_list = inorder[0:root_index]  # 在中序遍历列表中获得左子树节点的列表
        right_list = inorder[root_index + 1:]  # 在中序遍历列表中获得右子树节点的列表

        root_node = TreeNode(inorder[root_index])
        root_node.left = self.reConstructBinaryTree(preorder[1:root_index + 1],left_list)
        root_node.right = self.reConstructBinaryTree(preorder[root_index + 1:],right_list)
        return root_node



if __name__ == '__main__':
    arrbinarytree = ArrBinaryTree(arr=[1,2,3,4,5,6,7])
    arrbinarytree.outside_preOrder_API(0)
