def insert(bst,key):
    if('value' not in bst.keys()):
        bst = {

            'value':key,
            'left':{},
            'right':{}
            
            }
    elif(key < bst['value']):
        bst['left'] = insert(bst['left'],key)
    elif(key > bst['value']):
        bst['right'] = insert(bst['right'],key)
    return bst

def exist(bst,key):
    if(key == bst['value']):
        return True
    elif(key < bst['value'] and bst['left']!= {} ):
        return exist(bst['left'],key)
    elif(key > bst['value'] and bst['right']!= {} ):
        return exist(bst['right'],key)
    return False



def minimum(bst,start):
    if(start == bst['value'] and bst['left'] != {}):
        return minimum(bst['left'],bst['left']['value'])
    elif(start < bst['value'] and bst['left']!= {} ):
        return minimum(bst['left'],start)
    elif(start > bst['value'] and bst['right']!= {}):
        return minimum(bst['right'],start)
    return bst['value']
    


def maximum(bst,start):
    if(start == bst['value'] and bst['right'] != {}):
        return maximum(bst['right'],bst['right']['value'])
    elif(start < bst['value'] and bst['left']!= {} ):
        return maximum(bst['left'],start)
    elif(start > bst['value'] and bst['right']!= {}):
        return maximum(bst['right'],start)
    return bst['value']



def inorder_traversal(bst,visited=[]):
    if(bst == {}):
        return visited
    if(bst['left']!={}):
        visited= inorder_traversal(bst['left'],visited)
    visited.append(bst['value'])
    if(bst['right']!={}):
        visited= inorder_traversal(bst['right'],visited)
    return visited




def preorder_traversal(bst,visited=[]):
    if(bst == {}):
        return visited
    visited.append(bst['value'])
    if(bst['left']!={}):
        visited= preorder_traversal(bst['left'],visited)
    if(bst['right']!={}):
        visited= preorder_traversal(bst['right'],visited)
    return visited




def postorder_traversal(bst,visited=[]):
    if(bst == {}):
        return visited
    if(bst['left']!={}):
        visited= postorder_traversal(bst['left'],visited)
    if(bst['right']!={}):
        visited= postorder_traversal(bst['right'],visited)
    visited.append(bst['value'])
    return visited




# ========================================================================================
# Q1

# part a
lst=[68, 88, 61, 89, 94, 50, 4, 76, 66, 82]
bst = {}
for x in lst:
    bst = insert(bst,x)

print(bst)

# part b

print(exist(bst,50))

# part c

print(exist(bst,49))

# part d

print(minimum(bst,68))

# part e

print(minimum(bst,88))

# part f

print(maximum(bst,68))

# part g

print(maximum(bst,61))

# part h

print(inorder_traversal(bst))

# part i

print(preorder_traversal(bst))

# part j

print(postorder_traversal(bst))

# ===============================================================================================

# Q2

lst = ['begin', 'do', 'else', 'end', 'if', 'then', 'while']
bst2 = {}
for x in lst:
    bst2 = insert(bst2,x)

print(bst2)





