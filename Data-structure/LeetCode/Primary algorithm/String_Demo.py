# Time：2020/4/1916:16
def reverse(self,x: int) -> int:
    if x >= 0:
        x = list(str(x))
        x.reverse()
        if -2 ** 31 <= int("".join(x)) <= 2 ** 31 - 1:
            return int("".join(x))
        else:
            return 0
    else:
        x = list(str(abs(x)))
        x.reverse()
        if -2 ** 31 <= -int("".join(x)) <= 2 ** 31 - 1:
            return -int("".join(x))
        else:
            return 0
def isAnagram(s="anagram",t="nagaram"):
    s=list(s)
    t=list(t)
    d=dict()
    d1=dict()
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    for j in t:
        if j not in d1:
            d1[j]=1
        else:
            d1[j]+=1
    if d==d1:
        print(True)
    else:
        print(False)
def isPalindrome(s="q man, a plan, a canal: Panama"):
    """
    0-9:48-57
    a-z:97-122
    A-Z:65-90
    :param s:
    :return:"""
    s=list(filter(helper,s.lower()))
    if s==s[::-1]:
        print(True)
    else:
        print(False)
def helper(ch):
    if 'a'<=ch<="z" or 'A'<=ch<='Z'or '0'<=ch<='9':
        return ch
def myAtoi(str="   -42"):
    """
    int()强制转换，其中的数值只能全部为数字
    :param str:
    :return:
    """
    result = ""
    str = str.lstrip()
    if len(str)==0:
        print(0)
    if str[0]!="-"and str[0]!="+" and not str[0].isdigit():
        print(0)
    else:
        for i in str[1:]:
            if "0" <= i <="9":
                result+=i
            else:
                break
        if str[0]!="-" and str[0]!="+":
            result=str[0]+result
            temp = int(result)
        elif str[0]=="-":
            temp=-1*int(result)
        else:
            temp=+int(result)

        if temp<-2**31:
            print(-2**31)
        elif temp>2**31-1:
            print(2**31-1)
        else:
            print(temp)
class Solution:
    def countAndSay(self,n=3):
        if n<=1:
            return '1'
        prestr  = self.countAndSay(n-1)
        result=""
        count = 1
        for ids in range(len(prestr)):
            if ids == 0:
                count = 1
            elif prestr[ids] != prestr[ids-1]:
                temp = str(count)+prestr[ids-1]
                result += temp
                count = 1
            elif prestr[ids] == prestr[ids-1]:
                count+=1
            if ids == len(prestr)-1:
                temp = str(count)+prestr[ids]
                result+=temp
        return result
if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay())


