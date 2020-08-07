# Time：2020/3/1821:18
"""二分查找模板"""

def BinarySearch_one(nums,target):
    """
    二分查找模板一:查找条件可以在不与元素的两侧进行比较的情况下确定（或使用它周围的特定元素）
    :param nums:
    :param target:
    :return:
    """
    length = len(nums)
    if length == 0:
        return -1
    left,right = 0,length-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif target < nums[mid]:
            right = mid - 1 #向左查找
        else:
            left = mid + 1 #向右查找
    return -1

def BinarySearch_two(nums,target):
    """
    二分查找模板二：用于查找需要访问数组中当前索引及其直接右邻居索引的元素或条件
    :param nums:
    :param target:
    :return:
    """
    length = len(nums)
    if length == 0:
        return -1
    left,right = 0,length
    while left < right: # 查找空间至少两个元素，则进行while循环
       mid = (left+right)//2  # 向下取整
       if nums[mid] == target:
            return mid
       elif nums[mid]<target:
            left = mid + 1
       else:
            right = mid
    if left != len(nums) and nums[left] == target: # 当查找空间中只有一个元素时，即left==right，则执行该if语句
       return left
    return -1
def BinarySearch_Min(nums):
    length = len(nums)
    if length == 0:
        return -1
    left,right = 0,length-1
    while left < right:
        mid = (left + right)//2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]
def BinarySearch_Peak(nums):
    length = len(nums)
    if length == 0:
        return -1
    left,right = 0,length-1
    while left <= right:
        mid = left+(right-left)//2
        if left == right:
            return left
        elif nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid

def BinarySearch_three(nums,target):
    """
    二分查找模板三：用于搜索需要访问当前索引及其在数组中的直接左右邻居索引的元素或条件
    :param nums:
    :param target:
    :return:
    """
    length = len(nums)
    if length == 0:
        return -1
    left,right = 0,length-1
    while left+1<right: #查找空间至少三个元素，则进行while循环
        mid = (left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=mid
        else:
            right=mid
    # 当查找空间中两个元素时，则进行以下if语句
    if nums[left]==target:return left
    if nums[right]==target:return right
    return -1
def searchRange(nums,target):
    """
    在排序数组中查找元素的第一个和最后一个位置
    先寻找target，找到之后再判断其周围元素是否与其相等
    :param nums:
    :param target:
    :return:
    """
    l,r = 0,len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        n = nums[mid]
        if n == target:
            tmp = mid
            while tmp > 0 and nums[tmp - 1] == target:
                tmp -= 1
            while mid < len(nums) - 1 and nums[mid + 1] == target:
                mid += 1
            return [tmp,mid]
        elif n < target:
            l = mid + 1
        else:
            r = mid - 1
    return [-1,-1]

#print(BinarySearch_Min([4,5,6,7,0,1,2]))
#print(BinarySearch_Peak([1,2,3,1]))
#print(BinarySearch_three([1,2,3,4,5,6],3))
print(searchRange([0],3))