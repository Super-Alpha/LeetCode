"""小二叉堆的实现，'小二叉堆'，'大二叉堆' """
class BinHeap:
    def __init__(self):
        self.heapList=["x"]  # 零下标位被x占用
        self.currentSize=0
    def percUp(self,i):
        """沿着路径向上浮动"""
        while i//2>0:   # 1//2+0, 3//2=1
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i] = tmp
            i=i//2
    def insert(self,k):
        self.heapList.append(k) #将元素添加的末尾
        self.currentSize+=1
        self.percUp(self.currentSize) #新的key上浮
    def percDown(self,i):
        """沿着路径交换下沉"""
        while (i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc #沿路径向下
    def minChild(self,i):
        """返回值较小的节点坐标"""
        if i*2+1>self.currentSize:
            return i*2  #唯一子节点
        else:
            if self.heapList[i*2]<self.heapList[i*2+1]:
                return i*2
            else:              #返回较小的
                return i*2+1
    def delMin(self): #移走堆顶，即最小的key
        retval=self.heapList[1] #堆顶值
        self.heapList[1]=self.heapList[self.currentSize]
        self.currentSize-=1
        self.heapList.pop()
        self.percDown(1)  #新堆顶下沉
        return retval
    def buildHeap(self,alist):
        """从无序表生成堆"""
        i=len(alist)//2  #从最后节点的父节点开始，因为叶节点无需下沉
        self.currentSize=len(alist)
        self.heapList=[0]+alist[:]
        print(len(self.heapList),i)
        while (i>0):
            print(self.heapList,i)
            self.percDown(i)
            i-=1
        print(self.heapList,i)

import heapq

def Heapq_Use_Demo():
    heap=[6,7,9,4,3,5,8,10,1]
    iter1=[1,2,3,4,5,6]

    heapq.heapify(heap)  # 将列表转换成小顶堆
    print(heap)

    heapq.heappush(heap,2)  # 将2压入堆heap中
    print(heap)

    min_val_1=heapq.heappop(heap)  # 从堆中弹出最小的元素,并删除
    print(min_val_1)

    min_val_2 = heapq.heapreplace(heap,11) # 弹出最小的元素，并删除，后将11压入堆中
    print(min_val_2)
    print(heap)

    three_largest_val = heapq.nlargest(3,iter1)  # 返回iter1中3个最大的元素
    print(three_largest_val)

    three_smallest_val = heapq.nsmallest(3,iter1)  # 返回iter1中3个最小的元素
    print(three_smallest_val)



if __name__ == '__main__':
    # binheap=BinHeap()
    # binheap.insert(2)
    # binheap.insert(3)
    # binheap.insert(1)
    # binheap.insert(4)
    # binheap.delMin()
    # list=[9,6,5,2,3]
    # binheap.buildHeap(list)
    # print(binheap.heapList)
    Heapq_Use_Demo()









