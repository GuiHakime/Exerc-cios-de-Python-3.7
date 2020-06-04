def matriz_zeros(i,j):
    M=[]
    for i in range(i):
        M.append([0]*j)
        return M

def multmatriz(A,x):
    for i in range(len(A)):
        for j in range(len(A[0])):
                       A[i][j]=A[i][j]*x
    return A


def soma_matriz(A,B):
    C=(matriz_zeros(len(A),len(A[0])))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j]=A[i][j]+B[i][j]
    return C

def transposta(m):
    T=(matriz_zeros(len(m[0]),len(m)))
    for i in range(len(m)):
        for j in range(len(m[0])):
            m[i][j]=T[j][i]
    return T
    
    
    
        
    
