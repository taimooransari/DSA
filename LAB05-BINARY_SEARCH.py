
# Q1 - Binary Search Iterative
# Return index of item or -1 if it doesn't exist.

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative(lst,item):
    low=0
    high=len(lst)-1
    
    while(high>=low):
        mid=(low+high)//2
        if(lst[mid]==item):
            return mid
        elif(lst[mid]>item):
            high = mid-1
        elif(lst[mid]<item):
            low = mid+1
    return -1

print(binary_search_iterative(lst, item))

# =====================================================================================

# Q2 - Binary Search Iterative and Modified
# Extension of Q1, if item doesn't exist add it in list and return the index.

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())

def binary_search_iterative_modified(lst,item):
    low=0
    high=len(lst)-1
    while(high>=low):
        mid=(low+high)//2
        if(lst[mid]==item):
            return mid
        elif(lst[mid]>item):
            high = mid-1
        elif(lst[mid]<item):
            low = mid+1
    if(lst[mid]>item):
        lst.insert(mid,item)
        return mid
    elif(lst[mid]<item):
        lst.insert(mid+1,item)
        return mid+1
        
    
    

print(binary_search_iterative_modified(lst, item))

# =====================================================================================
