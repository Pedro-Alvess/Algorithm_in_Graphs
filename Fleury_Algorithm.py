
#%%

import networkx as nx
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (10,10)

# %%
def bfs(graph, starting_node):
    visited = []
    queue = [starting_node]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)            
            for edge in graph.edges:
                if edge[0] == node:
                    queue.append(edge[1])
                elif edge[1] == node:
                    queue.append(edge[0])
    return visited
# %%
nodes = 5
edge_probability= 0.4

G = nx.random_graphs.fast_gnp_random_graph(nodes, edge_probability)

while len(bfs(G, 0)) < len(G.nodes):
    G = nx.random_graphs.fast_gnp_random_graph(nodes, edge_probability)

def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, alpha=0.5)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
draw_graph(G)

#%%
def naive(graph):
    bridges = []
    aux_graph = graph.copy()

    for edge in graph.edges:
        aux_graph.remove_edge(edge[0],edge[1])
        
        if len(bfs(aux_graph, edge[0])) < len(graph.nodes):
            bridges.append(edge)
        
        aux_graph.add_edge(edge[0],edge[1])

    return bridges
# %%
def check_in_bridges():
    pass 
# %%
#Fleury
print("Naive: ", naive(G))

def fleury(graph):
    count_odd = 0
    aux_node = 0
    trail = [] 

    for node in graph.nodes:
        if len(G.edges(node)) % 2 != 0: # Check the degree
            aux_node = node; 
            count_odd += 1

        if count_odd >= 3:
            return []
    
    aux_graph = graph.copy()
    sub_graph = graph.copy()
    bridges = []
    trail.append(aux_node)

    while len(aux_graph.edges):
        print(trail)
        if len(aux_graph.edges(aux_node)) > 1:
            found = False
            for edge in aux_graph.edges(aux_node):
                if edge not in bridges:
                    aux_node = edge[1]
                    aux_graph.remove_edge(edge[0],edge[1])
                    sub_graph.remove_edge(edge[0],edge[1])
                    bridges = naive(sub_graph)
                    found = True
                    break

            if not found:
                return []
        elif len(aux_graph.edges(aux_node)) == 1:
            edge = list(aux_graph.edges(aux_node))[0]
            aux_node = edge[1]
            aux_graph.remove_edge(edge[0],edge[1])
            sub_graph.remove_node(edge[0])

            print("Vertices: ",sub_graph.nodes)
            print("Arestas: ",sub_graph.edges)
            bridges = naive(sub_graph) 
            print(bridges)

   
        else:
            if len(aux_graph.edges):
                #draw_graph(aux_graph)
                return []
    
        trail.append(aux_node)
    return trail

print(fleury(G))



# %%
