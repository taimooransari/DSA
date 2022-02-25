# Q1 selection sort
import ast

lst = input()
lst = ast.literal_eval(lst)
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if(lst[j]<lst[min_index]):
                min_index = j
        if(min_index!=i):
            lst[i],lst[min_index]=lst[min_index],lst[i]
        print(lst)
         

selection_sort(lst)
# ============================================
# Q2 insertion sort
import ast
lst = input()
lst = ast.literal_eval(lst)
def insertion_sort(lst):
    for i in range(1,len(lst)):
        j=i
        while(j>0 and lst[j-1]>lst[j]):
            lst[j],lst[j-1]= lst[j-1],lst[j]
            j-=1
        print(lst)
insertion_sort(lst)

# ================================================
# Q3- bubblee sort
import ast
lst = input()
lst = ast.literal_eval(lst)

def bubble_sort(lst):
    N = len(lst)
    if(N==1):
        print(lst)
        return
    for i in range(N-1):
        for j in range(N-i-1):
            if(lst[j+1]<lst[j]):
                lst[j+1],lst[j]=lst[j],lst[j+1]
        print(lst)
    

bubble_sort(lst)

# =======================================

# q4- sort matrix rows

import ast
lst = input()
lst = ast.literal_eval(lst)
def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if(lst[j]<lst[min_index]):
                min_index = j
        if(min_index!=i):
            lst[i],lst[min_index]=lst[min_index],lst[i]
    return(lst)
        
def sort_matrix_by_row(lst):
    for x in range(len(lst)):
        lst[x]=selection_sort(lst[x])
    return lst 
print(sort_matrix_by_row(lst))
# ===================================================================
# q5- sort matrix by column
import ast
lst = input()
lst = ast.literal_eval(lst)
column = int(input())

def selection_sort(lst,col):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1,len(lst)):
            if(lst[j][col]<lst[min_index][col]):
                min_index = j
        if(min_index!=i):
            lst[i],lst[min_index]=lst[min_index],lst[i]
    return(lst)

def sort_matrix_by_columnNumber(lst,column):
    lst = selection_sort(lst,column)
    return lst
    
    

print(sort_matrix_by_columnNumber(lst, column))

# ===========================================
# q6 - sort by title

import ast
rectangle_records = input()
rectangle_records = ast.literal_eval(rectangle_records)
record_title = input()
def insertion_sort(lst,title):
    for i in range(1,len(lst)):
        j=i
        while(j>0 and lst[j-1][title]>lst[j][title]):
            lst[j],lst[j-1]= lst[j-1],lst[j]
            j-=1
    return(lst)

def sort_rectangles(lst,title):
    lst = insertion_sort(lst,title)
    return lst

print(sort_rectangles(rectangle_records, record_title))