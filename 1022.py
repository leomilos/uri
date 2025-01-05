
from math import gcd
case_number =int(input().strip())

for i in range(case_number):
    n1,bar_1,d1,sinal,n2,bar_2,d2= list(map(str,input().strip().split()))
    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)
    
    if sinal =='+':
        result_nominador = (n1*d2)+(n2*d1)
        result_denominador = d1*d2
    elif sinal =='-':
        result_nominador = (n1*d2)-(n2*d1)
        result_denominador = d1*d2
    elif sinal =='*':
        result_nominador = n1*n2
        result_denominador = d1*d2
    elif sinal =='/':
        result_nominador = (n1*d2)
        result_denominador = (n2*d1)
    
    divisor = gcd(result_nominador, result_denominador)
    print(f"{result_nominador}/{result_denominador} = {int(result_nominador/divisor)}/{int(result_denominador/divisor)}")
