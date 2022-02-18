# Convert decimal to binary/octal/hexadecimal according to given base.

# Approach 1 - Using Stacks
def push(stack,data):
    stack.append(data)
    return stack
    
def pop(stack):
    return stack.pop()
    
def is_empty(stack):
    return len(stack)==0
def top(stack):
    return stack[-1]

def dec_converter_stack(dec, base):
    dic = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    result=""
    stack =list()
    while(dec!=0):
        rem = dic[dec % base]
        stack = push(stack,rem)
        dec = dec // base
    while(not is_empty(stack)):
        result+=str(pop(stack))
    if(len(result)>0):
        print(result)
    else:
        print(0)

dec_converter_stack(910,2)
dec_converter_stack(910,8)
dec_converter_stack(910,16)


# ================================================================
# Approach 2 - Without Stack 

def dec_converter(dec, base):
    dic = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F',
    }
    rem = dic[dec % base]
    dec = dec // base
    if (dec != 0):
        dec_converter(dec, base)
    else:
        print('')
    print(rem, end='')

dec_converter(910, 2)
dec_converter(910, 8)
dec_converter(910, 16)
