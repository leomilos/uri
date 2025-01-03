# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:15:45 2025

@author: Leonardo Milos
"""
import heapq
class Grafo:
    def __init__(self):
        self.grafo = {}
    def add_node(self,node):
        if node not in self.grafo:
            self.grafo[node] = []
    def add_aresta_peso(self,node_1,node_2,peso):
        self.grafo[node_1].append((node_2,peso))
        self.grafo[node_2].append((node_1,peso))

    def get_vizinho_peso(self, no, vizinho_desejado):
        for vizinho,peso in self.grafo[no]:
            if vizinho ==vizinho_desejado:
                return peso
        
    def dikstra(self,inicio,rota_origem):
        self.distancia = {no: float('inf') for no in self.grafo}
        self.distancia[inicio]
        ja_visitados = set()
        pq = [(0, inicio)]
        while pq:
            distancia_atual, no_atual = heapq.heappop(pq)
            if no_atual in ja_visitados:
                continue
            ja_visitados.add(no_atual)
            if no_atual in rota_origem:
                no_anterior = no_atual
                proximo_no = no_atual+1
                nova_distancia = distancia_atual + self.get_vizinho_peso(no_anterior,proximo_no)
                if nova_distancia < self.distancia[proximo_no]:
                    self.distancia[proximo_no] = nova_distancia
                    heapq.heappush(pq, (nova_distancia, proximo_no))
        
                    
            else:
                for vizinho, peso in self.grafo[no_atual]:
                    nova_distancia = distancia_atual+peso
                    if nova_distancia < self.distancia[vizinho]:
                        self.distancia[vizinho] = nova_distancia
                        heapq.heappush(pq, (nova_distancia, vizinho))
        
            


entrada = input().strip()

n_cidades,m_estradas,c_cidade_rotas,k_cidade_concertado = list(map(int, entrada.split()))# k ponto de partida
while n_cidades!=0 and m_estradas !=0 and c_cidade_rotas!=0 and k_cidade_concertado !=0:
    cidade_entrega = c_cidade_rotas -1
    cidades_rota_origina=[i for i in range(cidade_entrega)]
    graf = Grafo()
    for _ in range(m_estradas):
        entrada_estradas = input().strip()
        ponto_um,ponto_dois,pedagio = list(map(int, entrada_estradas.split()))
        graf.add_node(ponto_um)
        graf.add_node(ponto_dois)
        graf.add_aresta_peso(ponto_um,ponto_dois,pedagio)
        
    graf.dikstra(k_cidade_concertado,cidades_rota_origina)
    print(graf.distancia[cidade_entrega])
    entrada = input().strip()
    
    n_cidades,m_estradas,c_cidade_rotas,k_cidade_concertado = list(map(int, entrada.split()))# k ponto de partida

    
