
string = input().strip()
numero_erro,string_completa = list(map(str,string.split()))
while numero_erro !='0' and string_completa!='0':

    string_correta = string_completa.replace(numero_erro,'')
    cont = 0
    for letra in string_correta:
        if letra == '0':
            cont+=1
        else:
            break
    
    if len(string_correta)== cont:
        string_correta='0'
    print(int(string_correta))
    string = input().strip()
    numero_erro,string_completa = list(map(str,string.split()))
