
class Graf_kruskal:
    def __init__(self):
        self.graf = {}
        self.weight = {}
        self.edge = []
    def add_vertex(self,node):
        if node not in self.graf:
            self.graf[node] = []
    def add_edge(self,node_1,node_2,weight):
        self.edge.append((weight,node_1,node_2))
        # self.graf[node_1].append((node_2,weight))
        # self.graf[node_2].append((node_1,weight))
        # self.add_weight(weight,node_1,node_2)
        
    def find(self,parent,node):# the goal is to find a color for it
        if parent[node] != node:    
            parent[node] = self.find(parent, parent[node])
        return parent[node]
    def union(self,parent,root_1,root_2):
        parent[root_1]=root_2
    def kruskal(self):
        minimum_spaming_tree=[]
        self.edge.sort()
        
        parent = {node: node for node in self.graf}
        
        for weight, node_1,node_2 in self.edge:
            root_1 = self.find(parent,node_1)
            root_2 = self.find(parent,node_2)
            if root_1 != root_2:
                minimum_spaming_tree.append((node_1,node_2,weight))
                self.union(parent,root_1,root_2)
        return minimum_spaming_tree
        
        
    

vertex,edges = list(map(int,input().strip().split()))

while vertex!=0 and edges!=0:
    kruskal = Graf_kruskal()
    money_spend = 0
    for edge in range(edges):
        node_1,node_2,weight= list(map(int,input().strip().split()))
        kruskal.add_vertex(node_1)
        kruskal.add_vertex(node_2)
        kruskal.add_edge(node_1, node_2, weight)
        money_spend += weight
    minimum = kruskal.kruskal()
    sum_weight = 0
    for i,j,weight in minimum:
        sum_weight+=weight
    
    print(money_spend-sum_weight)
