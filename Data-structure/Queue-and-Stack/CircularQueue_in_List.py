# Time：2020/3/1611:19

class CirQueue:
    def __init__(self,maxsize):
        self.queue = [None]*maxsize #提前给maxsize个元素赋值None
        #self.queue = [maxsize]
        self.maxsize = maxsize
        self.front = 0 #队头指针
        self.rear = 0  #队尾指针
    def CurQueueLength(self):
        """
        :return:返回队列的实际长度
        """
        return (self.rear-self.front+self.maxsize) % self.maxsize
    def EnQueue(self,item):
        if (self.rear + 1) % self.maxsize == self.maxsize:
            print("The queue is full!")
        else:
            self.queue[self.rear] = item
            #self.queue.insert(self.rear,item)
            self.rear = (self.rear + 1) % self.maxsize # 更新尾指针
    def DeQueue(self):
        if self.rear == self.front:
            print("The is empty!")
        else:
            data = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1)% self.maxsize # 更新头指针
            return data
    def ShowQueue(self):
        for i in range(self.maxsize):
            print(self.queue[i],end=" ")
        print(" ")
    def CurFront(self):
        return self.queue[self.front]
    def CurRear(self):
        return self.queue[self.rear]

if __name__ == '__main__':
    queue = CirQueue(15)
    for i in range(10):
        queue.EnQueue(i)
    queue.ShowQueue()
    for i in range(5):
        queue.DeQueue()
    queue.ShowQueue()
    for i in range(9):
        queue.EnQueue(i)
    queue.ShowQueue()
    print(queue.CurFront())
    print(queue.CurRear())