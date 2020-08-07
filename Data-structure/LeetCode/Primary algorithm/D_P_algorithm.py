# Time：2020/4/299:19
import numpy as np

arr = [1,2,4,1,7,8,3]
def rec_opt(arr,i):
    """
    递归实现
    :param arr: 数组
    :param i: 索引
    :return: 前i+1个元素中不相邻元素的最大和
    """
    if i == 0:
        return arr[0]
    elif i == 1:
        return max(arr[0],arr[1])
    else:
        A = rec_opt(arr,i-2) + arr[i]
        B = rec_opt(arr,i-1)
        return max(A,B)
#print(rec_opt(arr,4))
def dp_opt(arr):
    """
    动态规划实现
    :param arr:
    :return:
    """
    opt = np.zeros(len(arr))
    opt[0] = arr[0]
    opt[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        A = opt[i-2]+arr[i]
        B = opt[i-1]
        opt[i] = max(A,B)
    return opt
#print(dp_opt(arr))

arr1 = [3,34,4,12,5,2]
def rec_subset(arr,i,s):
    """
    数组中是否存在和为S的元素
    “递归实现”
    :param arr:
    :param i: 索引
    :param s: 目标值
    :return:
    """
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr,i-1,s)
    else:
        A = rec_subset(arr,i-1,s-arr[i])
        B = rec_subset(arr,i-1,s)
        return A or B  # 或运算
#print(rec_subset(arr1,5,9))
def climbStairs(n):
    if n == 1:
        return 1
    result = np.zeros(n+1) # 初始化数组，用于保存中间值
    result[1] = 1 # 有一阶台阶时
    result[2] = 2 # 有两阶台阶时
    for i in range(3,n+1):
        result[i] = result[i-1] + result[i-2]
    return result[n]
#print(climbStairs(5))
def maxProfit(prices=[7,1,5,3,9,4]):
    """
    动态规划实现"股票最大利润"只能买一次，然后卖一次
    :param prices:
    :return:
    """
    n= len(prices)
    if n==0:
        return 0
    dp = [0]*n
    minprice = prices[0]
    for i in range(1,n):
        minprice=min(minprice,prices[i])
        dp[i] = max(dp[i-1],prices[i]-minprice)
    return dp
#print(maxProfit())
def maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]):
    n=len(nums)
    if n == 0:
        return 0
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1,n):
        dp[i] = max(nums[i],nums[i]+dp[i-1])
    return dp
#print(maxSubArray())
def fib(n):
    prev=1
    cur =1
    for i in range(3,n+1):
        s=prev+cur
        prev = cur
        cur = s
    return cur
print(fib(5))