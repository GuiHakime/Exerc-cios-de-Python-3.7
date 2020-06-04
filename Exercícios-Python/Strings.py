def retangulo(x):
    y=len(x)
    S='*'*(y+2)
    print(S)
    print('*'+x+'*')
    print(S)

def ordem(x,y,z):
    L=[x,y,z]
    L.sort()
    print('\n'.join(L))


def numero_palavras(x):
    Z=x.count(' ')+1
    return Z


def frase(S):
    x=S.split(' ')
    for i in range(len(x)):
        print(x[i])
        
    

    
