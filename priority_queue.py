# Prioirty Queue Implementation in Python.

import ast
queue = input()
queue = ast.literal_eval(queue)


# Add element in queue according to priority
def Enqueue(queue, item, priority):
    tup = (item,priority)
    if(len(queue)==0):
        queue.append(tup)
    else:
        if(priority>queue[0][1]):
            queue.insert(0,tup)
            return queue
        for x in range(len(queue)):
            if (queue[x][1]<priority):
                queue.insert(x,tup)
                return queue
        queue.append(tup)
        return queue
        
# Remove the element at the front and return it
def Dequeue(queue):
    val = queue[0][0]
    queue.pop(0)
    return val

operation = input()

if operation == "Enqueue":
    item = input()
    priority = int(input())
    Enqueue(queue, item, priority)
    print(queue)
elif operation == "Dequeue":
    print(Dequeue(queue))
    print(queue)
