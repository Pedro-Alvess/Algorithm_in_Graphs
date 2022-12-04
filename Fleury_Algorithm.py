#%%
import networkx as nx
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (10,10)

# %%
def breadth_first_search(graph, starting_node):
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
nodes = 21
edge_probability= 1

G = nx.random_graphs.fast_gnp_random_graph(nodes, edge_probability)

while len(breadth_first_search(G, 0)) < len(G.nodes):
    G = nx.random_graphs.fast_gnp_random_graph(nodes, edge_probability)

def draw_graph(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500, alpha=0.5)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
draw_graph(G)

#%%
def naive(graph,edge):
    graph.remove_edge(edge[0],edge[1])
    
    is_bridge = len(breadth_first_search(graph, edge[0])) < len(graph.nodes)

    graph.add_edge(edge[0],edge[1])

    return is_bridge
# %%
#Fleury
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
    trail.append(aux_node)

    while len(aux_graph.edges): 
        if len(aux_graph.edges(aux_node)) > 1:
            found = False
            for edge in aux_graph.edges(aux_node): 

                if not naive(sub_graph,edge): 
                    aux_node = edge[1]
                    aux_graph.remove_edge(edge[0],edge[1])
                    sub_graph.remove_edge(edge[0],edge[1])
                    found = True
                    break

            if not found:
                return []
        elif len(aux_graph.edges(aux_node)) == 1:
            edge = list(aux_graph.edges(aux_node))[0]
            aux_node = edge[1]
            aux_graph.remove_edge(edge[0],edge[1])
            sub_graph.remove_node(edge[0])

        else:
            if len(aux_graph.edges):
                return []
    
        trail.append(aux_node)
    return trail

print(fleury(G))
# %%
