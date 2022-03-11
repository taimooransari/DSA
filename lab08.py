
# ========================================
def addNodes(G,n):
    for x in n:
        G[x]=[]
    return G
    
# =========================================
def addEdges(G,edges,directed=False):
    
    for x in edges:
        key = x[0]
        edge = (x[1],x[2])
        G[key].append(edge)
    if(not directed):
        for x in edges:
            key = x[1]
            edge = (x[0],x[2])
            if(edge not in G[key]):
                G[key].append(edge)
    return G
        
# =========================================

def listOfNodes(G):
    return list(G.keys())

# ==========================================


G = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
edge_list = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 4, 1), (3, 4, 1), (3, 5, 1), (4, 5, 1)]
G = addEdges(G, edge_list,True)


# ==========================================


def listOfEdges(G,directed =False):
    edge_lst=[]
    if(directed):
        for x in G:
            if(len(G[x])>0):
                for y in G[x]:
                    edge = (x,y[0],y[1])
                    edge_lst.append(edge)
        return edge_lst
    else:
        for x in G:
            if(len(G[x])>0):
                for y in G[x]:
                    a=min(x,y[0])
                    b=max(x,y[0])
                    edge = (a,b,y[1])
                    if(edge not in edge_lst):
                        edge_lst.append(edge)
        return edge_lst

    
# ===========================================
def printIn_OutDegree(G):
    deg ={}
    for x in G:
        deg[x]={'inD':0,'outD':0}
    for x in G:
        deg[x]['outD'] = len(G[x])
        for y,z in G[x]:
            deg[y]['inD']+=1
    
    for x in deg:
        print(x,'=> In-Degree:',deg[x]['inD'],', Out-Degree:', deg[x]['outD'])

# ===========================================

def printDegree(G):
    for x in G:
        print(x,'=>',len(G[x]))


# ===========================================

def getNeighbors(G,node):
    lst = []
    for x in G[node]:
        lst.append(x[0])
    return lst

# ================================================



def getInNeighbours(G,node):
    lst = []
    for x in G:
        for y in G[x]:
            if(y[0]==node):
                lst.append(x)
                break
    return lst

# ================================================


def getOutNeighbours(G,node):
    lst = []
    for x in G[node]:
        lst.append(x[0])
    return lst

# ================================================

def getNearestNeighbor(G,node):
    nearest = False
    for x in G[node]:
        if(not nearest):
            nearest = x
        elif(x[1]<nearest[1]):
            nearest=x
    return nearest[0]

# ==================================================

def isNeighbor(G,n1,n2):
    for x in G[n1]:
        if(x[0]==n2):
            return True
    return False



# ==================================================
def removeNode(G,node):
    G.pop(node,None)
    vals = getInNeighbours(G,node)
    for x in vals:
        for y in G[x]:
            if(y[0]==node):
                G[x].remove(y)
                break
    return G
# =============================================

def removeNodes(G,nodes):
    for node in nodes:
        G.pop(node,None)
        vals = getInNeighbours(G,node)
        for x in vals:
            for y in G[x]:
                if(y[0]==node):
                    G[x].remove(y)
                    break
                    
    return G

# ============================================

def DisplayGraph(G):
    print(G)

# ============================================

def display_adj_matrix(G):
    matrix=[]
    for x in G:
        temp = []
        for x in G:
            temp.append(0)
        matrix.append(temp)

    for x in G:
        for y in G[x]:
            matrix[x][y[0]]=y[1]
    return(matrix)
        

# ============================================
nodes = ['BOS', 'ORD', 'JFK', 'DFW', 'MIA', 'SFO', 'LAX']
edges = [('BOS', 'JFK', 1) , ('BOS', 'MIA', 1), ('BOS', 'SFO', 1), ('JFK', 'BOS', 1),
('JFK', 'SFO', 1), ('JFK', 'MIA', 1), ('JFK', 'DFW', 1), ('ORD', 'MIA', 1),
('ORD', 'DFW', 1), ('MIA', 'DFW', 1), ('MIA', 'LAX', 1), ('DFW', 'ORD', 1),
('DFW', 'SFO', 1), ('DFW', 'LAX', 1), ('SFO', 'LAX', 1), ('LAX', 'ORD', 1)]
G = {}
print(addNodes(G,nodes))
print(addEdges(G,edges,True))
print(listOfNodes(G))
print(listOfEdges(G))

