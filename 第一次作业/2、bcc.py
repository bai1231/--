from flask import g


class Vertex():  
    #顶点表结点
    def __init__(self,data):
        self.data = data
        self.firstEdge = None
class Edge():  
    #边表结点
    def __init__(self,vertex):
        self.vertex = vertex
        self.nextEdge = None
class Graph():
    def __init__(self):
        self.vertexList = [] #顶点列表
        self.vertexNum = 0 #顶点数
        self.edgeNum = 0 #边数
        self.visited=None
    def addVertex(self,data):
        self.vertexList.append(Vertex(data))
        self.vertexNum += 1
    def addEdge(self,vertex1,vertex2):
        edge=Edge(vertex2)
        edge.nextEdge=vertex1.firstEdge #l连接之前的边表结点
        vertex1.firstEdge=edge
        self.edgeNum += 1
    def printGraph(self):
        for vertex in self.vertexList:
            print(vertex.data,end='->')
            edge=vertex.firstEdge
            while edge:
                print(edge.vertex.data,end='')
                edge=edge.nextEdge
                if edge!=None:
                    print('->',end='')
            print()
            
    def DFS(self,vertex):
        if self.visited==None:
            self.visited=dict([(vex.data,False) for vex in self.vertexList])
        print(vertex.data,end=' ')
        self.visited[vertex.data]=True
        edge=vertex.firstEdge
        while edge:
            if self.visited[edge.vertex.data]==False:
                self.DFS(edge.vertex)
            edge=edge.nextEdge

    def Dfsbcc(self,vertex):
        if self.visited==None:
            self.visited=dict([(vex.data,False) for vex in self.vertexList])
            self.t=-1
            self.d={}
            self.low={}
            self.par={}
            self.stack=[]
            self.bcc_list=[] #双连通分量list
        c=0
        self.t=self.t+1
        self.d[vertex.data]=self.t
        self.low[vertex.data]=self.d[vertex.data]

        edge=vertex.firstEdge
        while edge:  #遍历这个结点的所有边vw
            if self.d.get(edge.vertex.data)==None:  #w未被访问过
                self.par[edge.vertex.data]=vertex  #w的父结点是v
                c=c+1
                self.stack.insert(0,(vertex.data,edge.vertex.data))
                self.Dfsbcc(edge.vertex)
                self.low[vertex.data]=min(self.low[vertex.data],self.low[edge.vertex.data])
                if self.d[vertex.data]==0 and c>1 or self.d[vertex.data]>0 and self.low[edge.vertex.data]>=self.d[vertex.data]: #是割点
                    bcc=[]
                    while self.stack[0]!=(vertex.data,edge.vertex.data):
                        bcc.append(self.stack.pop(0))
                    bcc.append(self.stack.pop(0))
                    print(bcc)
                    self.bcc_list.append(bcc)
            else: #w已被访问过
                if self.par.get(vertex.data)!=edge.vertex: #w不是v的父结点
                    self.low[vertex.data]=min(self.low[vertex.data],self.d[edge.vertex.data])
                    if self.d[edge.vertex.data]<self.d[vertex.data]:
                        self.stack.insert(0,(vertex.data,edge.vertex.data))
            edge=edge.nextEdge
        return self.bcc_list


def creat_graph(edge_lst):
    graph=Graph()
    vex_s=vex_s=list(set([i for turple in edge_lst for i in turple ])) #顶点集合
    vex_s.sort()

    #添加顶点
    for vex in vex_s:
        graph.addVertex(vex)

    
    #无向图，则需变为双向图储存。
    edge1=[]
    for i,j in edge_lst:
        edge1.append((j,i))
    edge_lst=edge_lst+edge1

    #添加边 :确保序号小的排在前面
    revex_s=vex_s[::-1]
    for vex in vex_s:
        for j in revex_s:
            if (vex,j) in edge_lst:
                graph.addEdge(graph.vertexList[vex_s.index(vex)],graph.vertexList[vex_s.index(j)])
    graph.printGraph()
    return graph

def test(edge_lst):
    graph=creat_graph(edge_lst)
    bcc_list= graph.Dfsbcc(graph.vertexList[0])
    print(bcc_list)
    print(len(bcc_list))
if __name__ == '__main__':
    edge_lst=[('a','b'),('b','c'),('c','a'),('b','d'),('b','e'),('d','e')]
    test(edge_lst)