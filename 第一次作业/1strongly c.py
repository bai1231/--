import sys
sys.setrecursionlimit(1000000) 
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
    def DFS(self,vertex,visited):
        visited[vertex.data]=1
        print(vertex.data,end=' ')
        edge=vertex.firstEdge
        while edge:
            if visited[edge.vertex.data]==0:
                self.DFS(edge.vertex,visited)
            edge=edge.nextEdge
    def TopoSort(self):
        visited=[0]*self.vertexNum
        for vertex in self.vertexList:
            if visited[vertex.data]==0:
                self.DFS(vertex,visited)
    def Toposort_f(self):
        #return : a list (vertex,f_value) sort by f_value
        f_val=[(i,0) for i in range(1,self.vertexNum+1)]
        visited=[False]*self.vertexNum
        curLabel=self.vertexNum
        
        def explore(vertex):  #explore (G,v)
            nonlocal curLabel,visited
            visited[vertex.data-1]=True
            edge=vertex.firstEdge
            while edge:
                if visited[edge.vertex.data-1]==False:
                    explore(edge.vertex)
                edge=edge.nextEdge
            f_val[vertex.data-1]=(vertex.data,curLabel)
            curLabel-=1

        for vertex in self.vertexList:
            if visited[vertex.data-1]==False:
                explore(vertex)
        return sorted(f_val,key=lambda x:x[1],reverse=False)
    def SCC_sizes(self,f_val):
        #return : a list of list (strongly connected components) [(1,numscc),(2,numscc),...]
        visited=[False]*self.vertexNum
        numSCC=0
        SCC=[(i,0) for i in range(1,self.vertexNum+1)]

        def explore(vertex,visited):
            nonlocal numSCC
            visited[vertex.data-1]=True
            SCC[vertex.data-1]=(vertex.data,numSCC)
            edge=vertex.firstEdge
            while edge:
                if visited[edge.vertex.data-1]==False:
                    explore(edge.vertex,visited)
                edge=edge.nextEdge
        
        for vertex,_ in f_val:
            vertex=self.vertexList[vertex-1]
            if visited[vertex.data-1]==False:
                numSCC+=1
                explore(vertex,visited)
        SCC.sort(key=lambda x:x[1])
        # print(SCC)

        SCC_sizes=[0 for i in range(self.vertexNum)] #统计每个SCC的大小
        for i,j in SCC:
            SCC_sizes[j-1]+=1
        SCC_sizes.sort(reverse=True)
        return SCC_sizes[:5]




def get_biggest_five_SCC(max_vex,edge_lst):
    #return : a list of biggest five SCC
    graph=Graph()
    #添加顶点
    for i in range(1,max_vex+1):
        graph.addVertex(i)
    #添加边
    edge_lst=edge_lst
    for v1,v2 in edge_lst:
        graph.addEdge(graph.vertexList[v1-1],graph.vertexList[v2-1])
    # graph.printGraph()


    graph_reverse=Graph()
    #添加顶点
    for i in range(1,max_vex+1):
        graph_reverse.addVertex(i)
    #添加边
    edge_lst_res=[(v2,v1) for v1,v2 in edge_lst]
    for v1,v2 in edge_lst_res:
        graph_reverse.addEdge(graph_reverse.vertexList[v1-1],graph_reverse.vertexList[v2-1])    
    Gr_f_val=graph_reverse.Toposort_f()
    print(Gr_f_val)
    SCC_sizes=graph.SCC_sizes(Gr_f_val)
    return SCC_sizes


def test_case(edge_lst):
    max_vex=max([max(i,j) for i,j in edge_lst])
    SCC_sizes=get_biggest_five_SCC(max_vex,edge_lst)
    print(SCC_sizes)
if __name__=='__main__':
    edge_lst1=[(1,4),(2,8),(3,6),(4,7),(5,2),(6,9),(7,1),(8,5),(8,6),(9,7),(9,3)]
    test_case(edge_lst1)
    # edge_lst2=[(1,2),(2,6),(2,3),(2,4),(3,1),(4,5),(5,4),(6,5),(6,7),(7,6),(7,8),(8,5),(8,7)]
    # test_case(edge_lst2)
    # edge_lst3=[(1,2),(2,3),(3,1),(3,4),(5,4),(6,4),(8,6),(6,7),(7,8)]
    # test_case(edge_lst3)
    # edge_lst4=[(1,2),(2,3),(3,1),(3,4),(5,4),(6,4),(8,6),(6,7),(7,8),(4,3),(4,6)]
    # test_case(edge_lst4)
    # edge_lst5=[(1,2),(2,3),(2,4),(2,5),(3,6),(4,5),(4,7),(5,2),(5,6),(5,7),(6,3),(6,8),(7,8),(7,10),(8,7),(9,7),(10,9),(10,11),(11,12),(12,10)]
    # test_case(edge_lst5)
    # f=open('problem8.10.txt','r')
    # flie=f.read()
    # list_line=flie.split('\n')  #'1 1 '
    # list_line1=[i.split(' ') for i in list_line if len(i)>0]   #[['1','1'],['2','2']]
    # edge_lst=[(int(i[0]),int(i[1])) for i in list_line1]  #[(1,1),(2,2)]
    # test_case(edge_lst)
    # print('finished')
    

