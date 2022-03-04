# q1----------------------
unimodel_sequence = input().split(" ")
unimodel_sequence = [int(i) for i in unimodel_sequence]
    
def getTopIndex_UnimodelSequence(unimodel_sequence):
    low = 0
    high =len(unimodel_sequence)-1

    while low<=high:
        mid = (low+high)//2
        if(unimodel_sequence[mid+1]<unimodel_sequence[mid] and unimodel_sequence[mid]>unimodel_sequence[mid-1] ):
            return mid
        elif(unimodel_sequence[mid+1]>unimodel_sequence[mid] and unimodel_sequence[mid]>unimodel_sequence[mid-1] ):
            low = mid+1
        elif(unimodel_sequence[mid+1]<unimodel_sequence[mid] and unimodel_sequence[mid]<unimodel_sequence[mid-1] ):
            high=mid-1
    return -1
        
# q2-------------------------

import ast
powerTwoList = input()
powerTwoList = ast.literal_eval(powerTwoList)
size = int(input())

def findMissingNumber(powerTwoList, size):
    low = 0
    high = len(powerTwoList)-1
    index = 0
    while(low<=high):
        mid =(low+high)//2
        if(powerTwoList[mid] > (2**(mid))):
            high = mid-1
            index=mid
        elif(powerTwoList[mid] == (2**(mid))):
            low = mid+1
            index = mid+1
    return 2**(index)
            
            
# q3--------------------------
import ast
lst = input()
lst = ast.literal_eval(lst)
def smallest_absdiff_pairs(L):
    lst=[]
    
    for i in range(1,len(L)):
        j=i
        while(j>0 and L[j-1]>L[j]):
            L[j],L[j-1]= L[j-1],L[j]
            j-=1    
    
    for i in range(len(L)):
        a = L[i]
        for j in range(i+1,len(L)):
            b = L[j]
            
            diff = abs(a-b)
            tup = (min(a,b),max(a,b))
            if(len(lst)==0):
                lst.append(tup)
            else:
                last_diff = lst[0][1]-lst[0][0]
                if(diff == last_diff):
                    lst.append(tup)
                elif(diff<last_diff):
                    lst =[tup]
                else:
                    break
    return lst

                    
# q4---------------------------------

import ast
lst = input()
lst = ast.literal_eval(lst)
x = int(input())
# Enter your code here. Read input from STDIN. Print output to STDOUT
def sort_abs_difference(lst,x):
    for i in range(1,len(lst)):
        j=i
        while(j>0 and abs(x-lst[j-1])>abs(x-lst[j])):
            lst[j],lst[j-1]= lst[j-1],lst[j]
            j-=1
    return lst

print(sort_abs_difference(lst, x))