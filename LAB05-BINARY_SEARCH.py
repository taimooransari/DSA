
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

# Q3 - Binary Search Recursive
# Return index of item or -1 if it doesn't exist.

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())

def binary_search_recursive(lst,item,low,high):
    if(low<=high):
        mid=(low+high)//2
        if(lst[mid]==item):
            return mid
        elif(lst[mid]>item):
            high = mid-1
        elif(lst[mid]<item):
            low = mid+1
        index = binary_search_recursive(lst,item,low,high)
        return index
    else:
        return -1
    

print(binary_search_recursive(lst, item, low, high))

# =====================================================================================

# Q4 - Binary Search Recursive and Modified
# Extension of Q3, if item doesn't exist add it in list and return the index.

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
low = int(input())
high = int(input())
def binary_search_recursive_modified(lst,item,low,high):
    if(low<=high):
        mid=(low+high)//2
        if(lst[mid]==item):
            return mid
        elif(lst[mid]>item):
            high = mid-1
        elif(lst[mid]<item):
            low = mid+1
        if(low>high):
            if(lst[mid]>=item):
                lst.insert(mid,item)
                return mid
            elif(lst[mid]<item):
                lst.insert(mid+1,item)
                return mid+1
        index = binary_search_recursive_modified(lst,item,low,high)
        return index
print(binary_search_recursive_modified(lst, item, low, high))

# =====================================================================================

# Q5 - Binary Search Application
# Find student record and update data(email/mid1/mid2), don't change ID

import ast
student_records = input()
student_records = ast.literal_eval(student_records)
ID = input()
record_title = input()
data = input()

def update_record(student_records,ID,record_title,data):
    if(record_title=='ID'):
        return "ID cannot be updated"
    if(record_title!='Email'):
        data=int(data)
    dic = {"Email":1,'Mid1':2,'Mid2':3}
    index_to_change = dic[record_title]
    low=0
    high=len(student_records)-1
    
    while(low<=high):
        mid=(low+high)//2
        rec = student_records[mid][0]
        if(rec==ID):
            temp = list(student_records[mid])
            temp[index_to_change]=data
            student_records[mid]=tuple(temp)
            return student_records
        elif(rec>ID):
            high = mid-1
        elif(rec<ID):
            low = mid+1
    return "Record not found"
        
    
    
    

print(update_record(student_records, ID, record_title, data))

# =====================================================================================

# Q6 - Binary Search Application
# Find endpoints with the given length, return -1 if doesnot exist

import ast
points_list = input()
points_list = ast.literal_eval(points_list)
length = float(input())

def check_length(p1,p2):
    c_y = (p2[1]-p1[1])**2
    c_x = (p2[0]-p1[0])**2
    length = round((c_x + c_y)**0.5,2)
    return length


def length_of_line(points_list,length):
    low=0
    high=len(points_list)-1
    while(low<=high):
        mid=(low+high)//2 
        p_l = check_length(points_list[mid][0],points_list[mid][1])
        if(p_l==length):
            return mid
        elif(p_l>length):
            high = mid-1
        elif(p_l<length):
            low = mid+1
    return -1
        
        
    
    

print(length_of_line(points_list, length))
# =====================================================================================

# Q6 - Binary Search Application
# Find list of indexes where the item exists, return [] if doesnot exist

import ast
lst = input()
lst = ast.literal_eval(lst)
item = int(input())
def binary_search_iterative(lst,item):
    low=0
    high=len(lst)-1
    indexes=[]    
    while(high>=low):
        mid=(low+high)//2
        if(lst[mid]==item):
            return mid
        elif(lst[mid]>item):
            high = mid-1
        elif(lst[mid]<item):
            low = mid+1
    return -1
  
    
def finding_multiple(lst,item):
    indexes=[]
    index = binary_search_iterative(lst,item)
    if(index!=-1):
        indexes.append(index)
    else:
        return indexes
    if(index<len(lst)-1):
        for x in range(index+1,len(lst)):
            if(lst[x]==item):
                indexes.append(x)
            else:
                break
            
    if(index>0):
        for x in range(index-1,-1,-1):
            if(lst[x]==item):
                indexes.append(x)
            else:
                break
    indexes.sort()
    return indexes
            
    
        
    
    
    

print(finding_multiple(lst, item))
# =====================================================================================


