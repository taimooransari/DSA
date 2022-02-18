# Use stack to decode a string.
# '2[a]3[b]' = 'aabbb'\
# '2[a3[c]]' = '2[accc]' = 'acccaccc'
# Unlimited nesting within string allowed.


def push(stack,data):
    stack.append(data)
    return stack
    
def pop(stack):
    return stack.pop()
    
def is_empty(stack):
    return len(stack)==0
def top(stack):
    return stack[-1]
    
def main(s):
    result=''
    is_internal=False
    stack  =list()
    internal=''
    opened=0
    for x in s:
        if(x.isdigit()):
            if(is_empty(stack)):
                stack = push(stack,int(x))
            else:
                internal+=x
                is_internal=True
        elif(x.isalpha()):
            if(is_internal):
                internal+=x
            else:
                stack = push(stack,x)
        elif(x in '[]'):
            if(is_internal):
                if(x ==']'):
                    internal+=x
                    opened-=1
                    if(opened==0):
                        temp = main(internal)
                        stack = push(stack,temp)
                        internal=''
                        is_internal=False
                else:
                    internal+=x
                    opened+=1
            else:
                if(x ==']'):
                    while(not is_empty(stack)):
                        val = pop(stack)
                        if(val!='[' and type(val)!= int):
                            result=val+result
                        elif(type(val)==int):
                            return result*val
              
print(main('2[x2[y3[c2[v]]]]'))
    
    
    