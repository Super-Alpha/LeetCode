# Time：2020/3/2415:50

def twoSum(nums,target):
    numhash = dict()
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in numhash:
            return [i,numhash[diff]]
        numhash.update({nums[i]:i})
def firstUniqueChar(s):
    d = dict()
    l =[]
    for i in s:
        count = 1
        if i in d.keys():
            count += 1
            d.update({i:count})
        d.update({i:count})
    for key,value in d.items():
        if value == 1:
            l.append(s.index(key))
    l.sort()
    if l:
        return l[0]
    return -1

if __name__ == '__main__':
    """nums = [2,7,11,15]
    target=9
    print(twoSum(nums,target))"""
    #s="leetcode"
    #print(firstUniqueChar(s))
    s=list("eat")
    print(s)
    s="".join(sorted(s))
    print(s)