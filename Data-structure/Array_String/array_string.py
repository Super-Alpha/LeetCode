# Time：2020/3/1619:46
class Solution:

    def __init__(self):
        self.inputarray = [1,7,3,6,5,6,4,7]
        self.index = None

    def pivotIndex(self):
        for i in range(len(self.inputarray)):
            sumleft  = 0
            sumright = 0
            for k in range(i):
                sumleft = sumleft + self.inputarray[k]
            for j in range(i+1,len(self.inputarray)):
                sumright = sumright + self.inputarray[j]
            #print("sumleft={}".format(sumleft))
            #print("sumright={}".format(sumright))
            if sumleft == sumright:
                self.index = i
                return self.index
    def spiralOrder(self,matrix):
        result = []
        for i in range(len(matrix)):
            if i == 0:
                for j in matrix[i]:
                    result.append(j)
            elif i == len(matrix)-1:
                for k in range(-1,-(len(matrix[i])+1),-1):
                    result.append(matrix[i][k])
                for l in range(-2,-i,-1):
                    result.append(matrix[l][0])
            else:
                result.append(matrix[i][len(matrix[i])-1])
        return result

    def addBinary(self,a="",b=""):
        if a == "0":
            return b
        if b == "0":
            return a
        result = ""
        for i in range(0,-len(a),-1):
            for j in range(i,-len(b),-1):
                if a[i] != "0" and b[j] != "0":
                    b[j] = "0"


if __name__ == '__main__':
    solution = Solution()
    #a=solution.pivotIndex()
    #print(a)
    s = 7
    nums = [2,3,1,2,4,3]
    temp = []
    for i in range(len(nums)):
        if nums[i] == s:
            print(1)





















