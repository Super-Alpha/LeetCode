# Time：2020/5/412:11
import random
class Solution:
    def __init__(self,nums):
        self.nums = nums
    def reset(self):
        return self.nums
    def shuffle(self):
        a=self.nums.copy()
        random.shuffle(a)
        return a
solution = Solution([1,2,3,4])
print(solution.shuffle())
print(solution.reset())