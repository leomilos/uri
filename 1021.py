# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 17:47:57 2025

@author: Leonardo Milos
"""

entrada_inicial = float(input())

def checa_valor (valor:float,casa:float):
    quantidades_de_notas = int(valor/casa)
    valor_a_retornar = valor - (quantidades_de_notas*casa)
    return round(valor_a_retornar,2),quantidades_de_notas
notas_pociveis = [100,50,20,10,5,2]
print('NOTAS:')
entrada = round(entrada_inicial, 2)
for casa in notas_pociveis:
    entrada,quantidade_notas = checa_valor(entrada,casa)
    print(f'{quantidade_notas} nota(s) de R$ {float(casa):.2f}')
    

moedas_pociveis = [1,.5,.25,.10,.05,.01]


print('MOEDAS:')
for casa in moedas_pociveis:
    entrada,quantidade_notas = checa_valor(entrada,casa)
    print(f'{quantidade_notas} moeda(s) de R$ {float(casa):.2f}')
