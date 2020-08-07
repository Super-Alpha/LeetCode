# Time：2020/6/2411:24


class Tree:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.num = 1


class Solution:

    def count_right_smaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def insert(root,val,temp):
            if root.val < val:
                temp += root.num
                if root.right is not None:
                    root.right,temp = insert(root.right,val,temp)
                else:
                    root.right = Tree(val)
            else:
                root.num += 1
                if root.left is not None:
                    root.left,temp = insert(root.left,val,temp)
                else:
                    root.left = Tree(val)
            return root,temp

        n = len(nums)
        if n == 0:
            return []
        root = Tree(nums[-1])
        ret = [0]
        for i in range(n - 2,-1,-1):
            root,num = insert(root,nums[i],0)
            ret.append(num)
        return ret[::-1]


s = Solution()
print(s.count_right_smaller(nums=[5,2,6,1]))
