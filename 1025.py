
def procura_valor(lista,valor,esquerda=0,direita= None):
    if direita ==None:
        direita = len(lista)-1

    while esquerda<= direita:
        meio = int((esquerda + direita)/2)
        if lista[meio]==valor:
            temp = 1
            while lista[meio-temp]==valor:
                temp+=1
            return (meio-temp)+1
        elif valor>lista[meio]:
            esquerda = meio+1
        else:
            direita = meio-1
            
    return -1
    
        
        #caso que preciso checar parte de cima da lista
    pass
n=1
q=1
numero_do_caso=0
while n!=0 and q!=0:
    if numero_do_caso==0:
        numero_do_caso+=1
        raw_input = input().strip()
        n, q = map(int, raw_input.split())
        continue
        
    lista_n=[]
    for i in range(n):
        lista_n.append(int(input().strip()))
    lista_n.sort()
    valores_a_procurar = []
    for i in range(q):
        valores_a_procurar.append(int(input().strip()))
        
    print(f"CASE# {numero_do_caso}:")
    for i in valores_a_procurar:
        valor = procura_valor(lista_n,i)
        if valor == -1:
            print(f"{i} not found")
        else:
            print(f"{i} found at {valor+1}")
            
    numero_do_caso+=1
    raw_input = input().strip()
    n, q = map(int, raw_input.split())
