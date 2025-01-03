
class Grafo:
    def __init__(self):
        self.vertices = {}
        self.cor ={}
    def add_node(self,node):
        if node not in self.vertices:
            self.vertices[node]=[]
            self.cor[node]=False
            
    def add_aresta(self,node_1,node_2):
        self.vertices[node_1].append(node_2)
        self.vertices[node_2].append(node_1)
    
    def bfs(self,start):
        queue = self.vertices[start]
        self.visitados=set()
        self.cor[start]=True
        while queue:
            atual=queue.pop(0)
            self.visitados.add(atual)
            self.cor[atual] =True
            for vertice in self.vertices[atual]:
                if self.cor[vertice]==False:
                    queue.append(vertice)
            
        
        
        
t_test_case = int(input().strip())

for test in range(t_test_case):
    start_point = int(input().strip())
    entrada = input().strip()
    vertice,aresta = list(map(int,entrada.split()))
    grafo = Grafo()
    for path in range(aresta):
        entrada = input().strip()
        node_a,node_b = list(map(int,entrada.split()))
        grafo.add_node(node_a)
        grafo.add_node(node_b)
        grafo.add_aresta(node_a,node_b)
        
    grafo.bfs(start_point)
    print(len(grafo.visitados)*2)
