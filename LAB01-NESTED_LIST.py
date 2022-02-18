# Q1 - Matrix Substraction

def matrix_subtraction(A,B):
    if(len(A)!=len(B) or len(A[0])!= len(B[0])):
        return "Matrices A and B don't have the same dimension required for matrix subtraction."
    else:
        for row in range(len(A)):
            for col in range(len(A[row])):
                A[row][col]-=B[row][col]
    return A

# ================================================================================================
# Q2 - Matrix Transpose

def matrix_transpose(A):
    A_fix =[]
    for x in range(len(A[0])):
        A_fix.append([])
        for y in range(len(A)):
            A_fix[x].append(A[y][x])
    return A_fix


# ================================================================================================
# Q3 - Matrix Multiplication

def matrix_multiplication(A,B):
    if(len(B)!= len(A[0])):
        return "The number of columns in Matrix A does not equal the number of rows in Matrix B required for Matrix Multiplication."
    else:
        C=list()
        for x in range(len(A)):
            C.append([])

            for y in range(len(B[0])):
                val = 0
                for i in range(len(B)):
                    val += A[x][i]*B[i][y]
                C[x].append(val)
        return C

# =================================================================================================
# Q4 - Image Sharpening


def sharpen_image(A):
    C = list()
    row = len(A)-1
    col = len(A[0])-1
    for x in range(row+1):
        C.append([])
        for y in range(col+1):
            C[x].append(0)
            top,bottom,right,left,div=0,0,0,0,0
            if(x > 0 and x<row):
                bottom = A[x+1][y]
                top = A[x-1][y]
                div+=2
            elif(x==0):
                bottom = A[x+1][y]
                div+=1
            elif(x==row):
                top = A[x-1][y]
                div+=1

            if(y > 0 and y<col):
                right = A[x][y+1]
                left = A[x][y-1]
                div+=2
            elif(y==0):
                right = A[x][y+1]
                div+=1
            elif(y==col):
                left = A[x][y-1]
                div+=1
            val=2*abs(A[x][y] -(top+bottom+right+left)/div)
            C[x][y]= round(val,2)
    return C

