# Stack Implementation in Python.


# push data to the end/top of stack
def push(stack,data):
    stack.append(data)
    return stack

# removes data from top of stack and return it  
def pop(stack):
    return stack.pop()

# returns if stack is empty or not  
def is_empty(stack):
    return len(stack)==0

# returns the topmost element of stack
def top(stack):
    return stack[-1]
    
# returns the size of stack
def size(stack):
    return len(stack)