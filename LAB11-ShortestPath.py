def min_dist(Q,dist):
    m = float('inf')
    i=0
    for x in range(len(Q)):
        node = Q[x]
        if(dist[node][1]<m):
            m = dist[node][1]
            i = x
    return i 
    


def dijkstra(graph,source):
    inf = float('inf')
    dist={
        source:(source,0)
    }
    Q= [source]
    visited=[]
    lst=[]
    for node in graph:
        if(node!=source):
            dist[node]=(source,inf)
    while(len(Q)>0):
        i  =min_dist(Q,dist)
        v = Q.pop(i)
        if(v not in visited):
            for neighbour in graph[v]:
                Q.append(neighbour[0])
                alt = neighbour[1]+dist[v][1]
                if(alt<dist[neighbour[0]][1]):
                    s,t,d = v,neighbour[0],alt
                    dist[t]=(s,d)
            visited.append(v)
    return dist
G = { 
        'A': [('B', 5), ('E', 6), ('D', 3)], 
        'B': [('A', 5), ('C', 6)], 
        'C': [('B', 6), ('D', 10), ('G', 2)], 
        'D': [('A', 2), ('C', 10), ('F', 8)], 
        'E': [('A', 6), ('F', 9)], 
        'F': [('D', 8), ('E', 9), ('G', 10)], 
        'G': [('C', 2), ('F', 10)] 
    } 
print(dijkstra(G,'A'))

def getShortestPath(graph,source,target):
    inf = float('inf')
    dist={
        source:(source,0)
    }
    Q= [source]
    visited=[]
    lst=[]
    for node in graph:
        if(node!=source):
            dist[node]=(source,inf)
    while(len(Q)>0):
        i  =min_dist(Q,dist)
        v = Q.pop(i)
        if(v not in visited):
            for neighbour in graph[v]:
                Q.append(neighbour[0])
                alt = neighbour[1]+dist[v][1]
                if(alt<dist[neighbour[0]][1]):
                    s,t,d = v,neighbour[0],alt
                    dist[t]=(s,d)
            visited.append(v)
            if(v==target):
                break

    start = target
    while(start!=source):
        s,t,d = dist[start][0],start,dist[start][1]
        lst = [(s,t,d)]+lst
        start = s
    return lst

print(getShortestPath(G,'A','F'))