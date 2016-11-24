import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge(1,2, weight=3)
G.add_edge(2,3, weight=4)
G.add_edge(2,4, weight=6)
G.add_edge(3,5, weight=7)
G.add_edge(5,7, weight=1)
G.add_edge(4,7, weight=2)
G.add_edge(4,6, weight=3)
G.add_edge(6,7, weight=4)
G.add_edge(7,8, weight=1)
G.add_edge(8,9, weight=2)

nx.set_node_attributes(G, 't1', 0)
nx.set_node_attributes(G, 't2', 0)
nx.set_node_attributes(G, 'luz', 0)

visited = []
unvisited = G.nodes()

print(unvisited)

while unvisited:
    node = unvisited[0]
    #print(unvisited[0]['t1'])
    for successor in G.successors_iter(node):
        waga = G.edge[node][successor]['weight'] #waga krawedzi miedzy wierzchołkami
        droga = G.node[node]['t1']
        suma_droga_waga = droga + waga
        if G.node[successor]['t1'] == 0:
            G.node[successor]['t1'] = suma_droga_waga
        elif G.node[successor]['t1'] < suma_droga_waga:
            G.node[successor]['t1'] = suma_droga_waga

    visited.append(unvisited[0])
    unvisited.remove(unvisited[0])

print(G.node[9])
print(G.node[6])




#for i in G.edges_iter():
#    waga = G.get_edge_data(i[0], i[1])
#    G.node[i[1]]['t1'] = waga['weight'] + G.node[i[0]]['t1']
#    print(G.node[i[1]]['t1'])

#for i in G.nodes_iter():
#    print(i, G.node[1])

#nx.draw(G)
#plt.show()




