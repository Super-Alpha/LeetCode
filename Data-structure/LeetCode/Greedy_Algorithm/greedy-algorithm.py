# Time：2020/6/211:38
# 摇摆序列
def wiggleMaxLength(nums=[1,17,5,10,13,15,10,5,16,8]):
    if len(nums) <= 2:
        return len(nums)
    maxLength = 1
    result = [nums[0]]
    begin = 1
    STATE= begin
    up = 2
    down =3
    temp = nums[0]
    for i in range(1,len(nums)):
        if STATE == 1:
            if nums[i]>nums[i-1] and nums[i]!=temp:
                STATE = up
                maxLength += 1
                result.append(nums[i])
                temp = nums[i]
            elif nums[i]<nums[i-1] and nums[i]!=temp:
                STATE = down
                maxLength +=1
                result.append(nums[i])
                temp = nums[i]
            continue
        elif STATE == 2:
            if nums[i]<nums[i-1] and nums[i]!=temp:
                STATE = down
                maxLength += 1
                result.append(nums[i])
                temp = nums[i]
            continue
        elif STATE == 3:
            if nums[i]>nums[i-1] and nums[i]!=temp:
                STATE = up
                maxLength += 1
                result.append(nums[i])
                temp = nums[i]
            continue
    print(maxLength)
    print(result)
#wiggleMaxLength()

#移掉k位数字
def removeKdigits(num="10",k=2):
    stack = []  # 栈初始化
    for i in num:
        while k and stack and stack[-1] > i:
            stack.pop()
            k -= 1
        stack.append(i)
    if k:
        finalstr="".join(stack[:-k]) # 移除递增序列的后k位
    else:
        finalstr="".join(stack)
    return finalstr.lstrip("0") or "0"  # 移除左边的“0”
#a=removeKdigits()
#print(a)

def canJump(nums=[1,2,1,1,4]):
    length = len(nums)
    maxdis = 0 #最远可到达的位置
    if length<=1:
        return True
    for i in range(length):
        if i <= maxdis:
            maxdis = max(maxdis,nums[i]+i)
            if maxdis >= length-1:
                return True
    return False
#print(canJump())
def canJump2(nums=[1,2,1,1,4]):
    max_dis=0
    count=0
    end =0
    for i in range(len(nums)-1):
        if i <= max_dis:
            max_dis=max(max_dis,nums[i]+i)
            if i==end:
                end=max_dis
                count+=1
    return count
#print(canJump2())
def findMinArrowShots(points=[[10,16],[2,8],[1,6],[7,12]]):
    if points is None:
        return 0
    points.sort(key= lambda x:x[0]) #降序排列
    shot_num=1
    shot_end = points[0][1]
    for i_start,i_end in points:
        if shot_end<i_start: #说明不相交
            shot_num+=1
            shot_end=i_end
    return shot_num

print(findMinArrowShots())
