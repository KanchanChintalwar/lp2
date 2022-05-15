from collections import deque
class Graph:
    def __init__(self,edges,n):
        self.adjList=[[]for _ in range(n)]
        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for u in graph.adjList[v]:
        if not visited[u]:
            DFS(graph,u,visited)

def recursiveBFS(graph,q,visited):
    if not q:
        return
    v=q.popleft()
    print(v,end=' ')
    for u in graph.adjList[v]:
        if not visited[u]:
            visited[u]=True
            q.append(u)
    recursiveBFS(graph,q,visited)

if __name__=='__main__':
    vx=int(input("Enter no of vertices> "))
    edge=int(input("enter no of edges> "))
    print("\nenter vertices of edges> ")
    edges=list(tuple(map(int,input().split()))for r in range(edge))
    graph=Graph(edges,vx)
    visited=[False]* vx
    loopVar=True
    while(loopVar!=False):
        print("\nMenu")
        print("\n1.DFS\n2.BFS\n3.Exit")
        ch=int(input("enter your choice>"))
        if(ch==1):
            for i in range(vx):
                if not visited[i]:
                    DFS(graph,i,visited)
        elif(ch==2):
            q=deque()
            visited=[False]* vx
            for i in range(vx):
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
                    recursiveBFS(graph,q,visited)
        elif(ch==3):
            loopVar=False
            print("End")
        else:
            print("\nEnter valid choice")



