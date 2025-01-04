
class Graf:
    def __init__(self):
        self.graf = {}
        self.tree_status = {}
        self.connections_tree={}
        self.start_count = 0
    def add_vertex(self,vertex):
        self.graf[vertex] = []
        self.tree_status[vertex] = 0
    def add_edge(self,node_1,node_2):
        self.graf[node_1].append(node_2)
        self.graf[node_2].append(node_1)
    
    def find_all_values_of_tree(self,start):
        queue = [start]
        self.start_count +=1
        self.connections_tree[self.start_count] = [start]
        alredy_visit = set()
        alredy_visit.add(start)
        while queue:
            vertex_queue = queue.pop(0)
            self.tree_status[vertex_queue] = self.start_count
            for vertex in self.graf[vertex_queue]:
                if vertex not in alredy_visit:
                    alredy_visit.add(vertex)
                    self.connections_tree[self.start_count].append(vertex)
                    queue.append(vertex)
    def run_all_tree(self):
        for vertex in self.graf:
            if self.tree_status[vertex]==0:
                self.find_all_values_of_tree(vertex)
        
    
            
    


case_qty = int(input().strip())

for case in range(case_qty):
    vertex,edge = list(map(int,input().strip().split()))
    letter = 'a'
    graf = Graf()
    for _ in range(vertex):
        graf.add_vertex(letter)
        letter = chr(ord(letter) + 1)
    
    for _ in range(edge):
        node_1,node_2 = list(map(str,input().strip().split()))
        graf.add_edge(node_1, node_2)
    graf.run_all_tree()
    
    print(f"Case #{case+1}:")
    for node in graf.connections_tree:
        for letter in sorted(graf.connections_tree[node]):
            print(letter,end=',')
        print()
    print(f'{graf.start_count} connected components')
    print()
    
