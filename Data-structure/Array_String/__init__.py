# Time：2020/3/1711:17
import numpy as np

def findDiagonalOreder(newarray):
    if newarray==[]:
        return []
    target=[[] for i in range(len(newarray)+len(newarray[0])-1)]
    for x,i in enumerate(newarray): #x为索引值，i为元素
        for y,j in enumerate(i):
            if(x+y)%2 == 0:
                target[x+y].insert(0,j)
            else:
                target[x+y].append(j)
    result=[]
    for i in target:
        for j in i:
            result.append(j)
    return result


def test():
    array1=np.arange(9).reshape(3,3)
    array2=np.arange(12).reshape(3,4)
    array3=np.arange(16).reshape(4,4)
    print(array1)
    print(array2)
    print(array3)
def plusone(digits):
    for i in range(digits,-1,-1):
        print(i)

if __name__ == '__main__':
    new_array = [[1,2,3],[4,5,6],[7,8,9]]
    a=findDiagonalOreder(new_array)
    print(a)
    #plusone(10)
    #test()