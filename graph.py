import networkx as nx
import matplotlib.pyplot as plt
#===================== GRAF ==============================

def createGraph(G):
	nx.set_node_attributes(G, 't1', 0)
	nx.set_node_attributes(G, 't2', 0)
	nx.set_node_attributes(G, 'luz', 0)
	nx.set_node_attributes(G, 'from', 0)
#G.add_edge(1,2, weight=3)
#G.add_edge(2,3, weight=4)
#G.add_edge(2,4, weight=6)
#G.add_edge(3,5, weight=7)
#G.add_edge(5,7, weight=1)
#G.add_edge(4,7, weight=2)
#G.add_edge(4,6, weight=3)
#G.add_edge(6,7, weight=4)
#G.add_edge(7,8, weight=1)
#G.add_edge(8,9, weight=2)

def add_Edge(G, fro, to, weigh):
	G.add_edge(fro,to, weight=weigh)
	print(fro, to, weigh)

#================================= algorytm przechodzenia grafu po najdłuższych ścieżkach ======================================
# po drodze uzupełniam wartości 't1'

def CPM(G):
	visited = [] #lista odwiedzonych wierzchołków
	unvisited = G.nodes() #lista wierzchołków do odwiedzenia	
	print(unvisited)
	while unvisited:            #pętla dopóki jest coś nieodwiedzonego
	    node = unvisited[0]        #biorę kolejne nieodwiedzone wierchołki
	    for successor in G.successors_iter(node):         #iteracja po sąsiadach noda
	        waga = G.edge[node][successor]['weight'] #waga krawedzi miedzy wierzchołkami
	        droga = G.node[node]['t1']  #droga od początku grafu do wierzchołka który jest rozpatrywany
	        suma_droga_waga = droga + waga
	        if G.node[successor]['t1'] < suma_droga_waga: #przypisuję najgorszą drogę
	            G.node[successor]['t1'] = suma_droga_waga
	            G.node[successor]['from'] = node #zaznaczam z którego wierzchołka była najgorsza droga, potrzebne do ścieżki krytycznej	

	    visited.append(unvisited[0])     #przerzucam odwiedzone wierzchołki
	    unvisited.remove(unvisited[0])	

	#========================================= znajduję koniec grafu ================================
	# czyli node z najwiekszym t1
	max = 0
	last_node = G.node[1]
	for node in G.nodes_iter():
	    if G.node[node]['t1'] > max:
	        max = G.node[node]['t1']
	        last_node = G.node[node]	

	#======================================== idę od końca i buduję ścieżkę krytyczną ==========================
	sciezka_krytyczna = []
	while 1:
	    sciezka_krytyczna.append(last_node)
	    last_node = G.node[last_node['from']]
	    if last_node['from'] == 0:
	        break
	sciezka_krytyczna.reverse()
	print(sciezka_krytyczna)	

	#====================================== rysowanko grafu ============================================	
	

	pos = nx.spring_layout(G)	

	nx.draw(G, pos)
	node_labels = nx.get_node_attributes(G,'t1')
	nx.draw_networkx_labels(G, pos, labels = node_labels)
	edge_labels = nx.get_edge_attributes(G,'weight')
	nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
	plt.show()





