from collections import deque
class Graph:
     def __init__(self,edges,n):
         self.adjList = [[]for _ in range(n)]
         for(src,dest) in edges:
             self.adjList[src].append(dest)
             self.adjList[dest].append(src)

def bfs(graph,q,visited):
    if not q:
        return
    v=q.popleft()
    print(v,end=' ')
    for u in graph.adjList[v]:
        if not visited[u]:
            visited[u]=True
            q.append(u)
    bfs(graph,q,visited)

if __name__ == '__main__':
    vx = int(input('Enter vertices :'))
    edge = int(input('\nEnter no of edges :'))
    edges = list(tuple(map(int,input().split()))for r in range(edge))
    visited = [False]*vx
    graph = Graph(edges,vx)
    loopvar = True
    while(loopvar!= False):
        print('\n1. BFS \n2. Exit')
        ch = int(input('\nEnter choice:'))
        if(ch==1):
            q=deque()
            visited=[False]* vx
            for i in range(vx):
                if not visited[i]:
                    visited[i]=True
                    q.append(i)
                    bfs(graph,q,visited)

        elif(ch==2):
            loopvar= False
            print('thanks')

        else:
            print('enter valid input')
