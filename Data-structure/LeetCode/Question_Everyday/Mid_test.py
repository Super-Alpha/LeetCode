# Time：2020/5/1518:44
def subarraySum(nums=[1,1,1],k=2):
    count= 0
    sum = 0
    d={}
    for i in nums:
        sum+=i
        if sum==k:
            count+=1
        if sum-k in d:
            count+=d[sum-k]
        if sum in d:
            d[sum]+=1
        else:
            d[sum]=1
    return count
def test(nums1=[1,3],nums2=[2]):
    nums1.extend(nums2)
    nums1.sort()
    length = len(nums1)
    temp = length//2
    if length % 2==0:
        print((nums1[temp-1]+nums1[temp])/2)
    else:
        print(nums1[temp])
from heapq import *
class Solution:
    def __init__(self):
        self.max_h = []
        self.min_h = []
        heapify(self.max_h)
        heapify(self.min_h)

    def addNum(self,num):
        heappush(self.min_h,num)
        heappush(self.max_h,-heappop(self.min_h))
        if len(self.max_h) > len(self.min_h):
            heappush(self.min_h,-heappop(self.max_h))

    def findMedian(self):
        max_len = len(self.max_h)
        min_len = len(self.min_h)
        if max_len == min_len:  # 有两个候选中位数
            return (self.min_h[0] + -self.max_h[0]) / 2.0
        else:  # 小顶堆的size 一定 >= 大顶堆的size，所以答案就是小顶堆的堆顶
            return self.min_h[0] / 1.0
#
# solution = Solution()
# solution.addNum(1)
# solution.addNum(2)
# print(solution.findMedian())
# solution.addNum(3)
# print(solution.findMedian())

def ThreeSumClosest(nums=[-1,2,1,-4],target=1):
    stack = nums[0:3]  # save three parameter
    temp_val = sum(stack) - target
    for i in range(3,len(nums)):
        if temp_val == 0:
            return sum(stack)
        for j in range(3):
            temp = stack.copy()
            temp.pop(j)
            temp.append(nums[i])
            temp_val_1 = sum(temp) - target
            if abs(temp_val)>abs(temp_val_1):
                stack.remove(temp[j])
                stack.append(nums[i])
    return sum(stack)
print(ThreeSumClosest(nums=[0,2,1,-3],target=1))





























