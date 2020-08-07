# @Time：2020/7/1617:03
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class TREE_DEMO:
    def build(self,tree,node_list,i):
        if i < len(node_list):
            if node_list[i] == None:
                return None
            else:
                tree = Node(node_list[i])
                tree.left = self.build(tree.left,node_list,i * 2 + 1)
                tree.right = self.build(tree.right,node_list,i * 2 + 2)
            return tree
        return tree

    def BFS(self,root):
        queue = [root]
        res = []
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res

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
    def rightSideView(self, root):
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

if __name__ == '__main__':
    node_list=[1,2,3,None,5,None,4]
    tree_demo = TREE_DEMO()
    root = tree_demo.build(None,node_list,0)
    print(tree_demo.rightSideView(root))