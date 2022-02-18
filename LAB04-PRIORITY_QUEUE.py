# Q1 - Priority Queue Application

def Enqueue(queue, item, priority):
    tup = (item,priority)
    if(len(queue)==0):
        queue.append(tup)
    else:
        for x in range(len(queue)):
            if (queue[x][1]<priority):
                queue.insert(x,tup)
                return queue
        queue.append(tup)
        return queue

def Dequeue(queue):
    val = queue.pop(0)
    return val[0]

def main():
    queue=[]
    
    Enqueue(queue,'AC Not working in Tariq Rafi',5)
    Enqueue(queue,'Password Change Issue',4) 
    Enqueue(queue,'Need Installation on laptop',3)
    Enqueue(queue,'Need license',1)
    Enqueue(queue,'Lab PCs Setup',3)
    Enqueue(queue,'Login Issue',4)
    
    print(Dequeue(queue))
    print(Dequeue(queue))
    print(Dequeue(queue))
    print(Dequeue(queue))
    print(Dequeue(queue))
    print(Dequeue(queue))
    
main()

# ======================================================================

# Q2 - Interleave Queue

import ast

lst = input()
lst = ast.literal_eval(lst)


def Enqueue(queue, item, priority):
    tup = (item, priority)
    if (len(queue) == 0):
        queue.append(tup)
        return queue
    else:
        for x in range(len(queue)):
            if (queue[x][1] < priority):
                queue.insert(x, tup)
                return queue
        queue.append(tup)
        return queue


def Dequeue(queue):
    val = queue.pop(0)
    return val[0]


def InterLeaveQueue(lst):
    queue1 = []
    queue2 = []
    mid = (len(lst) - 1) // 2
    for x in range(len(lst)):
        if (x <= mid):
            queue1 = Enqueue(queue1, lst[x], 0)
        else:
            queue2 = Enqueue(queue2, lst[x], 0)
    lst = list()
    for x in range(mid + 1):
        v1 = Dequeue(queue1)
        v2 = Dequeue(queue2)
        lst.append(v1)
        lst.append(v2)

    return lst


print(InterLeaveQueue(lst))