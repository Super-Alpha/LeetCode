# Time：2020/3/2912:47
class Recursion:
    def __init__(self):
        pass
    def printReverse(self,i,s):
        if (s == None or i >= len(s)):
            return
        self.printReverse(i+1,s)
        print(s[i],end="")
    def reverseString(self,s):
        def helper(i,s):
            if (i >= len(s) or s == None):
                return
            helper(i + 1,s)
            s.append(s.pop(i))
        helper(0,s)
        return s
    def generate(self,n):
        if n == 0:
            return [1]
        else:
            return [([0]+self.generate(n-1))[i]+(self.generate(n-1)+[0])[i] for i in range(n+1)]
class Solution:
    def generate(self, numRows):
        result = []
        def helper(i,j):
            if j==0 or i==j:
                return 1
            else:
                return helper(i-1,j)+helper(i-1,j-1)
        for i in range(0,numRows):
            temp = []
            for j in range(0,i+1):
                temp.append(helper(i,j))
            result.append(temp)
        return result

    def Generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:return []
        if numRows == 1:return [[1]]
        if numRows == 2: return [[1],[1,1]]
        res = [[1],[1,1]]
        if numRows > 2:
            for i in range(2,numRows):
                cr = [1,1]
                for j in range(1,i):
                    cr.insert(j,res[i-1][j-1]+res[i-1][j])
                res.append(cr)
        return res
    def fibonacci(self,n):
        if n<2:
            return n
        else:
            return self.fibonacci(n-1)+self.fibonacci(n-2)
    def fib(self,N):
        """
        将重复数据保存在缓存当中，节约计算时间
        :param N:
        :return:
        """
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = recur_fib(N-1)+recur_fib(N-2)
            cache[N] = result
            return result
        return recur_fib(N)
    def myPow(self,x,n):
        """
        x的n次方
        :param x:
        :param n:
        :return:
        """
        if not n:
            return 1
        if n < 0:
            n = abs(n)
            x = 1/x
        if n & 1:
            return x * self.myPow(x,n-1)
        return self.myPow(x**2,n//2)


if __name__ == '__main__':
    #recursion = Recursion()
    #print(recursion.reverseString(['a','b','c','d']))
    #print(recursion.generate(2))
    solution = Solution()
    print(solution.fib(4))

