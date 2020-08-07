# Time：2020/3/1720:29
class test:
    def __init__(self):
        pass
    def test_rep(self):
        newlist=[1,2,3]
        s = set()
        for i in newlist:
            if i in s:
                return True
            s.add(i)
        return False
class list_test:
    def __init__(self,nums,target):
        self.list = []
        self.nums = nums
        self.target = target
    def list_dict(self):
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if self.nums[i]+self.nums[j]==self.target:
                    print([i,j])

class Solution:
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_hash = {}
        nums_len = len(nums)
        for i in range(nums_len):
            dif = target - nums[i]
            if dif in nums_hash:
                return [nums_hash[dif],i]
            nums_hash[nums[i]] = i
        return []

class string_test:
    def __init__(self,string):
        self.string = string
    def test(self):
        new_dict = dict.fromkeys(self.string,0)
        for i in self.string:
            if i in new_dict.keys():
                new_dict[i]+=1
        for i in self.string:
            if new_dict[i]==1:
                print(list(self.string).index(i))
                break
class word_test:
    def __init__(self,newlist):
        self.newlist = newlist
    def strsort(self,sigstr):
        sigstr = list(sigstr)
        sigstr = "".join(sorted(sigstr))
        return sigstr
    def test(self):
        dic = {}
        for i in self.newlist:
            secondlist = self.strsort(i)
            if secondlist in dic.keys():
                dic[secondlist].append(i)
            else:
                dic[secondlist]=[i]
        print(dic)
        print(list(dic.values()))

if __name__ == '__main__':
    w = word_test(["eat", "tea", "tan", "ate", "nat", "bat"])
    w.test()
    """
    nums = [1,2,3]
    target = 3
    print(Solution().twoSum(nums,target))

    t=test()
    print(t.test_rep())
    d=list_test([2,7,11,15],9)
    d.list_dict()
    s=string_test("loveleetcode")
    s.test()"""









