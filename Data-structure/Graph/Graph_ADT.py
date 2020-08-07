class Vertex:
    """设置Graph的顶点(vertex)类"""
    def __init__(self,key):
        """
        :param key:该顶点的key
        """
        self.id=key
        self.connectedTo = {}  # 存储与该顶点连接的邻近顶点

    def addNeighbor(self,nbr,weight=0):
        """
        添加该顶点的邻近顶点以及所连接边的权值
        :param nbr:所添加邻近顶点的key
        :param weight:
        :return:
        """
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id)+" connectTo: "+str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        获得与该顶点邻接的点
        :return:
        """
        return self.connectedTo.keys() # 输出字典的关键字

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        """输入邻近点的key，得到连接边的权值"""
        return self.connectedTo[nbr]


class Graph:
    """设置图"""
    def __init__(self):
        self.vertList={}  # 存储所添加的顶点
        self.numVertices=0  # 图中所有顶点的数目
    def addVertex(self,key):
        """添加顶点"""
        self.numVertices=self.numVertices+1
        newVertex = Vertex(key)
        self.vertList[key]=newVertex
        return newVertex
    def getVertex(self,n):
        """
        通过key查找顶点
        :param n:
        :return:
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    def __contains__(self, item):
        return item in self.vertList
    def addEdge(self,f,t,cost=0):
        #不存在的顶点先添加
        if f not in self.vertList:
            nv=self.addVertex(f)
        if t not in self.vertList:
            nv=self.addVertex(t)
        #调用起始顶点的方法添加邻接边
        self.vertList[f].addNeighbor(self.vertList[t],cost)
    def getVertices(self):
        return self.vertList.keys()
    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == '__main__':
    g=Graph()
    #添加图的6个顶点
    for i in ["A","B","C","D","E","F"]:
         print(g.addVertex(i))
    #print(g.getVertices())
    #print(g.vertList)
    #添加图的8条边
    g.addEdge("A","B")
    g.addEdge("A","C")
    g.addEdge("B","C")
    g.addEdge("B","D")
    g.addEdge("C","D")
    g.addEdge("C","E")
    g.addEdge("D","E")
    g.addEdge("D","F")
    for v in g:
        for w in v.getConnections():
            print("(%s,%s)"%(v.getId(),w.getId()))
    g.BFS(g.vertList,"A")


