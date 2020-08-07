# Time：2020/4/1317:10
def removeDuplicates(nums=[1,1,2]):
    i=0
    j=1
    while j<len(nums):
        if nums[i]==nums[j]:
            nums.remove(nums[j])
            j=i+1
        else:
            i+=1
            j+=1
    print(len(nums))
def rotate(nums=[1,2,3,4,5,6,7],k=3):
    """nums[0:len(nums)-k] = reversed(nums[0:len(nums)-k])
    nums[len(nums)-k:len(nums)] = reversed(nums[len(nums)-k:len(nums)])
    nums.reverse()
    print(nums)"""
    if nums:
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
    print(nums)
def containsDuplicate(nums=[1,2,3,4]):
    temp = set(nums)
    if len(nums)==len(temp):
        print(False)
    else:
        print(True)
def singleNumber(nums=[4,1,2,1,2]):
    Dict = dict()
    for i in nums:
        if i not in Dict:
            Dict[i] = 1
        else:
            Dict[i]+= 1
    for j,k in Dict.items():
        if k==1:
            print(j)
def intersect(nums1=[1,2,2,1],nums2=[2,2]):
    result = []
    if nums1 == nums2:
        print(nums1)
    elif len(nums1)>=len(nums2):
        for i in nums2:
            if i in nums1:
                index = nums1.index(i)
                temp = nums1.pop(index)
                result.append(temp)
    else:
        for j in nums1:
            if j in nums2:
                index_ = nums2.index(j)
                temp_ = nums2.pop(index_)
                result.append(temp_)
    print(result)
def moveZeroes(nums=[0,0,1,0,0,0,2,3]):
    i=0
    while i < len(nums):
       for j in range(len(nums)):
           if nums[j]==0:
               nums.append(nums.pop(j))
       i+=1
    print(nums)
def rotate(matrix=[[1,2,3],[4,5,6],[7,8,9]]):
    length=len(matrix)
    for i in range(length):
        for j in range(length):
            temp = matrix[i].pop(0)
            matrix[j].append(temp)
    for i in matrix:
        i.reverse()
    print(matrix)
def isValidSudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]!=".":
                for column in range(9):
                    if column != j and board[i][j] == board[i][column]:#column!=j是排除找到相同位置的数字
                        return False
                for row in range(9):
                    if row != i and board[i][j] == board[row][j]:
                        return False
                for line in range((i//3)*3,(i//3)*3+3):       #寻找在同一3*3的方块内是否有相同的数字
                    for col in range((j//3)*3,(j//3)*3+3):    #//是整除，如5//3、4//3都等于1
                        if line != i and col != j and board[i][j] == board[line][col]:
                            return False
    return True
def maxProfit(prices=[7,5,4,3,1,2,6,2,1,9]):
    profit_sum = 0
    if prices == None:
        return 0
    else:
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit_sum+=prices[i]-prices[i-1]
        print(profit_sum)

if __name__ == '__main__':
    board=[
          ["5","3",".",".","7",".",".",".","."],
          ["6",".",".","1","9","5",".",".","."],
          [".","9","8",".",".",".",".","6","."],
          ["8",".",".",".","6",".",".",".","3"],
          ["4",".",".","8",".","3",".",".","1"],
          ["7",".",".",".","2",".",".",".","6"],
          [".","6",".",".",".",".","2","8","."],
          [".",".",".","4","1","9",".",".","5"],
          [".",".",".",".","8",".",".","7","9"]
          ]
    #print(isValidSudoku(board))
    maxProfit()