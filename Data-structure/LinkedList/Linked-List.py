class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None #存储下一个节点的地址
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext
    def __repr__(self):
        return "{}==>{}".format(self.data,self.next)
class UnorderLinkedList:
    def __init__(self):
        self.head=None
    #表尾为最先加入的元素，表头为最后加入的元素
    def add(self,e):
        node=Node(e)
        node.setNext(self.head)
        self.head=node
    def size(self):
        current=self.head #指向第一个节点的指针，其实值为Node(data)
        count=0
        while current!=None:
            count+=1
            current=current.getNext() #self本身就是对象的传递
        return count
    def is_Empty(self):
        return self.head is None
    def search(self,item):
        found=False
        current=self.head
        while current!=None and not found:
            if current.getData()==item:
                found=True
            else:
                current=current.getNext()
        return found
    def append(self,newdata):
        node=Node(newdata) #node为指向下一个节点的指针
        if self.is_Empty():
            self.head=node
        else:
            current=self.head
            while current.getNext() is not None:
                current=current.getNext()
            current.setNext(node)
    def insert(self,index,item):
        """
        :param index: item插入位置index之后
        :param item:
        :return:
        """
        if index<=0:
            self.add(item)   #放在链表开头
        elif index>self.size()-1:
            self.append(item) #放在链表末尾
        else:
            node=Node(item)  #创建节点
            current=self.head
            count=0
            #找到位置index处
            while count<index-1:
                count+=1
                current=current.getNext()
            node.next=current.getNext()
            current.setNext(node)
    def remove(self,item):
        current=self.head
        previous=None
        found=False
        #寻找要删除的元素item
        while not found:
            if current.getData()==item:
                found=True
            else:
                previous=current
                current=current.getNext()
        #找到item之后，对其进行删除
        if previous==None: #
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
class OrderLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        return self.head==None
    def size(self):
        current=self.head
        count=0
        while current!=None:
            count+=1
            current=current.getNext()
        return count
    def remove(self,index,item):
        current=self.head
        found=False
        previous=None
        while not found:
            if current.getData()==item:
                found=True
            else:
                current=self.head
                previous=current.getNext()
        if previous==None:
            self.head=current.getNext()
        else:
            previous.setNext(current.getNext())
    def rearch(self,item):
        current=self.head
        found=False
        stop=False
        while current!=None and not found and not stop:
            if current.getData()==item:
                found=True
            else:
                if current.getData()>item:
                    stop = True
                else:
                    current = current.getNext()
        return found
    def add(self,item):
        current=self.head
        previous=None
        stop=False
        #发现插入的位置
        while current!=None and not stop:
            if current.getData>item:
                stop=True
            else:
                previous=current
                current=current.getNext()
        temp=Node(item)#创建节点
        #插入在表头
        if previous==None:
            temp.setNext(self.head)
            self.head=temp
        #插入在表中
        else:
            previous.setNext(temp)
            temp.setNext(current)




