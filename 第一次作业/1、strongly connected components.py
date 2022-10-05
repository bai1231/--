import sys
sys.setrecursionlimit(100000)
global graph,graph_r
graph=[[] for i in range(900000)]
graph_r=[[] for i in range(900000)]
def create_graph(path,if_reverse=False):
    global graph #第一层每个位置代表结点，里面每个list存储邻接边指向的邻接点。
    global graph_r
    visited_no=set()              #在visited_no中的结点代表未访问                    
    f=open(path,'r')
    flie=f.readlines()
    for i in flie:
        i=i.split(" ")
        if if_reverse==False:  #不需要反转
            a,b=int(i[0]),int(i[1])
        else:                   #需要反转
            b,a=int(i[0]),int(i[1])
        if a not in visited_no:
            visited_no.add(a)
        if b not in visited_no:
            visited_no.add(b)
        if if_reverse==False:
            graph[a].append(b)
        else:
            graph_r[a].append(b)
    return visited_no

def Toposort(graph,visited_no):
    #计算f-value
    curlabel=len(visited_no)
    def explore(graph,v):
        global f
        nonlocal curlabel
        visited_no.remove(v) #从未访问列表中删除
        for u in graph[v]:
            if u in visited_no: #如果u在未访问
                explore(graph,u)
        f[v]=curlabel
        curlabel-=1
    # for i in visited_no:  #explore,未访问过的结点  #这种会跳过一些结点
        # explore(graph,i)
    for v in visited_no.copy(): #explore,未访问过的结点
        if v in visited_no: #如果v在未访问
            explore(graph,v)

def Kasaraju(path):
    if_reverse=True
    visited_no=create_graph(path,if_reverse) #反转图
    print('create g_r finished')
    global f
    global graph,graph_r
    f={}  #每个结点的f值
    Toposort(graph_r,visited_no)   #计算反转图的 f
    print('toposort finished')
    del graph_r
    
    SCC=[0 for i in range(800000)] #每个强连通分量个数
    def explore(graph,v):
        nonlocal numscc
        nonlocal visited_no
        nonlocal SCC
        visited_no.remove(v) #从未访问列表中删除
        SCC[numscc]+=1
        for u in graph[v]:
            if u in visited_no: #如果u在未访问
                explore(graph,u)
   
    visited_no=create_graph(path,False) #正常图
    print('create graph finished;')
    numscc=0
    f_list=sorted(f.items(),key=lambda x:x[1],reverse=False)  #按f值从小到大排序
    for v,_ in f_list: #遍历结点
        if v in visited_no: #如果v在未访问
            numscc+=1
            explore(graph,v)
    return SCC


def test(path):
    SCC=Kasaraju(path)
    print('scc finished')
    #print(SCC) #[0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # scc_values=list(SCC.values())
    # scc_values_size=[scc_values.count(i) for i in set(scc_values)]
    SCC.sort(reverse=True)
    # answer=[0 for i in range(5)]
    # for index,i in enumerate(scc_values_size[:5]):
    #     answer[index]=i #前五个强连通分量的大小,不足补0
    print(SCC[:5])
if __name__=='__main__':
    # test("problem8.10.test1.txt")
    # test('./第一次作业/problem8.10test2.txt')
    # test('./第一次作业/problem8.10test3.txt')
    # test('./第一次作业/problem8.10test4.txt')
    # test('./第一次作业/problem8.10test5.txt')
    # test('./第一次作业/problem8.10test6.txt')
    test('problem8.10.txt')
