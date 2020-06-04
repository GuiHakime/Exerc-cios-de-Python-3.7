def remove_repetidos(lista):
    i=0
    L=[]
    while i<len(lista):
        if lista[i] not in L:
            L.append(lista[i])
            L.sort()
        i=i+1
    return L

def inserir_zeros(L):
    i=1
    while i<len(L):
        L.insert(i,0)
        i=i+2
    return L


def pares(lista):
    L=[]
    for i in range(len(lista)):
        if lista[i]%2==0:
            L.append(i)
    return L

def meia_ordenada(lista):
    i=len(lista)//2
    L1=lista[:i]
    L2=lista[i:]
    L1.sort()
    L2.sort()
    L2.reverse
    return L1+L2

def lista_intercalada(L):
    L1=[]
    L2=[]
    for x in range(0,len(L),2):
        L1.append(L[x])
    for x in range(1,len(L),2):
        L2.append(L[x])
    return L1,L2


def intercalada2(L):
    L1=[]
    L2=[]
    for i in range(len(L)):
        if i%2==0:
            L1.append(L[i])
        else:
            L2.append(L[i])
    return L1,L2


    
    
   
    
    
  
        
    
 
  
            


  
