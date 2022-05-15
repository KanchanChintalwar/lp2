class Graph:
    def __init__(self,edges,n):
        self.adjList = [[] for _ in range(n)]
        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def dfs(graph,v,visited):
    visited[v] = True
    print(v, end= ' ')
    for u in graph.adjList[v]:
        if not visited[u]:
            dfs(graph,u,visited)

if __name__ == '__main__':
    vx = int(input('ENTER VERTICES :'))
    edge = int(input('\nENTER NO. OF EDGES : '))
    print('\nEnter vertices of edges :')
    edges = list(tuple(map(int,input().split()))for r in range(edge))
    graph = Graph(edges,vx)
    visited= [False]*vx
    loopvar = True
    while(loopvar != False):
        print('\n1. DFS ,\n2. Exit')
        ch = int(input('\nEnter choice :'))
        if (ch==1):
            for i in range(vx):
                if not visited[i]:
                    dfs(graph,i,visited)
        
        elif (ch==2):
            loopvar= False
            print('Thankyou')

        else:
            print('enter valid input')