# Time：2020/6/211:36
import heapq

def heap_demo():
    heap = []
    data = [1,3,5,7,9,2,4,6,8,0]
    for i in data:
        heapq.heappush(heap,i) #将元素添加进堆
    print("这是将元素添加进堆：{}".format(heap))

    heapq.heapify(data) # 将列表转换为堆的形式
    print("这是将列表转换为堆的形式：{}".format(data))

    list_1 = []
    while heap:
        list_1.append(heapq.heappop(heap)) # 将堆中的元素按从小到大的顺序弹出
    print("这是从小到大弹出的元素：{}".format(list_1))

    print("这是堆中最大的5个元素：{}".format(heapq.nlargest(5,data)))
    print("这是堆中最小的5个元素：{}".format(heapq.nsmallest(5,data)))

heap_demo()