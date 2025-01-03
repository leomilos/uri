# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:34:15 2025

@author: Leonardo Milos
"""


def merge_sort(lista,esquerda,direita):
    if esquerda>=direita:
        return 0
    meio = int((esquerda+direita)/2)
    
    inversoes = merge_sort(lista,esquerda,meio)
    inversoes += merge_sort(lista,meio+1,direita)
    
    inversoes += merge_sort_count(lista, esquerda, meio, direita)
    
    return inversoes
def merge_sort_count(lista,esquerda,meio,direita):
    index_esquerda = esquerda
    index_direita = meio+1
    
    
    numero_inversoes = 0
    temp_index= []
    while index_esquerda <= meio and index_direita <= direita:
        if lista[index_esquerda] <= lista[index_direita]:
            temp_index.append(lista[index_esquerda])
            index_esquerda += 1
        else:
            temp_index.append(lista[index_direita])
            index_direita += 1
            numero_inversoes += meio - index_esquerda + 1
        
    while index_esquerda <= meio:
        temp_index.append(lista[index_esquerda])
        index_esquerda += 1

    while index_direita <= direita:
        temp_index.append(lista[index_direita])
        index_direita += 1
        
    lista[esquerda:direita + 1] = temp_index

    return numero_inversoes



player_1 ='Marcelo'
player_2 ='Carlos'

valor_um = -1
while valor_um!= 0:
    if valor_um ==-1:
        entrada = input().strip()
        
        valores = list(map(int, entrada.split()))
        
        valor_um = valores[0]
        lista = valores[1:valor_um+1]
        continue
    
    trocas = 0
    trocas = merge_sort(lista,0,len(lista)-1)
    resultado = trocas%2
    if resultado == 1:
        print(player_1)
    else:
        print(player_2)
    entrada = input().strip()
    
    valores = list(map(int, entrada.split()))
    valor_um = valores[0]
    lista = valores[1:valor_um+1]
        
        
            
                
            
    
