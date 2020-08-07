# @Time：2020/7/189:29

graph = {"A":["B","C"],
         "B":["A","C","D"],
         "C":["A","B","D","E"],
         "D":["B","C","E","F"],
         "E":["C","D"],
         "F":["D"]}

def BFS(graph,s):
    """
    广度优先搜索
    :param graph:定义好的图
    :param s: 首先开始搜索的节点
    :return:
    """
    res = []
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    while queue:
        vertex = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        res.append(vertex)
    print(res)
def DFS(graph,s):
    """
    深度优先搜索
    :param graph:定义好的图
    :param s: 首先开始搜索的节点
    :return:
    """
    res = []
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    while stack:
        vertex = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        res.append(vertex)
    print(res)
def demo(p,q):
    if p == None and q==None:
        return
    return True

if __name__ == '__main__':

    # BFS(graph,"A")
    # DFS(graph,"A")
    print(demo(None,None))