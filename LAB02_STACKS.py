# Q1 - Stack functions

def push(lst,item):
    lst.append(item)
    return lst
def pop(lst):
    return lst.pop()
def is_empty(lst):
    return len(lst)==0
    
# ==========================================================================
# Q2 - String Reversal by Stack

def string_reversal(s):
    if not(isinstance(s,str)):
        return False
    stack =list()
    result=''
    for x in s:
        stack = push(stack,x)
    for x in range(len(s)):
        while(not(is_empty(stack))):
            result+=pop(stack)
    return result

# ===========================================================================