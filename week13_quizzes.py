# MAKE A FRIENDS CIRCLE FROM ADJ MATRIX, direct and indirect connections matter

def all_friends(M,a,lst=[]):
    if(a not in lst):
        lst=[a]
    f=[]
    for x in range(len(M[a])):
        if(M[a][x]==1 and x not in lst):
            if(x not in lst):
                f.append(x)
                lst.append(x)
    if(f!=[]):
        for x in f:
            p= all_friends(M,x,lst)
            for y in p:
                if(y not in lst):
                    lst.append(y)
    return lst


def extractFriendsCircle(M):
    circles = []
    considered = []
    for a in range(len(M)):
        if(a not in considered):
            circle = all_friends(M,a)
            circles.append(circle)
            considered+=circle
    return circles


M = [
    [1,1,0,0],
    [1,1,1,0],
    [0,1,1,0],
    [0,0,0,1]
]

N = [
    [1,1,0,0],
    [1,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

print(extractFriendsCircle(M))
print(extractFriendsCircle(N))
            