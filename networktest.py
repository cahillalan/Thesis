import networkx as nx
import matplotlib.pyplot as plt
import pickle



mydata = []
dicti = {'County':'Carlow',
                'Industry':'Mining'}
#mydata.append(dicti)
dicti ={
         'County': 'Laois',
         'Industry': 'Mining'}
mydata.append(dicti)
dicti ={
         'County': 'Carlow',
         'Industry': 'Business'}
mydata.append(dicti)
dicti = {
         'County': 'Dublin',
         'Industry': 'Mining'}
mydata.append(dicti)
dicti={
         'County': 'Dublin',
         'Industry': 'Business',}
#mydata.append(dicti)
dicti={
         'County': 'Dublin',
         'Industry': 'Business',}
#mydata.append(dicti)
G = nx.Graph()
a = 0
for n in mydata:
    G.add_node(a,county = n['County'])
    G.nodes[a]['county'] = n['County']
    G.nodes[a]['industry']= n['Industry']
    a+=1
x = len(mydata)

countyx = nx.get_node_attributes(G,'county')
countyi = nx.get_node_attributes(G,'county')
for y in range(0,x):
    for i in range(0,x):
        print(countyx[y],y)
        print(countyi[i],i)
        if countyx[y] in countyi[i]:
            if y != i:
                G.add_edge(y,i,weight=1)
indx = nx.get_node_attributes(G, 'industry')
indi = nx.get_node_attributes(G, 'industry')
for y in range(0,x):
    for i in range(0, x):

        if indx[y] in indi[i]:
            if y != i:
                if G.has_edge(y,i) is False:
                    G.add_edge(x, i, weight=1)
                else:
                    G[x][i]['weight'] = 2
print(indi)
y = 0
print(G.edges())
elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 1]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 1]
print(elarge)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, edgelist=elarge,
                       width=11)
nx.draw_networkx_edges(G, pos, edgelist=esmall,
                       width=4,alpha=0.5, edge_color='b')
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
plt.axis('off')
plt.show()


plt.show()
with open ('DataSets\\test.weighted.edgelist','wb') as picklefile:
    pickle.dump(G, picklefile,pickle.HIGHEST_PROTOCOL)


with open ('DataSets\\test.weighted.edgelist','rb') as picklefile:
    G = nx.Graph(pickle.load(picklefile))
    indx = nx.get_edge_attributes(G, 'weight')
    print(indx)
    print(G.nodes.data())

    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 1]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 1]
    print(elarge)
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, edgelist=elarge,
                           width=11)
    nx.draw_networkx_edges(G, pos, edgelist=esmall,
                           width=4, alpha=0.5, edge_color='b')
    nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
    plt.axis('off')
    plt.show()

    plt.show()
    print(nx.degree_centrality(G))
    print(nx.degree_histogram(G))
    print(nx.density(G))
    print(nx.info(G))
    print(nx.number_of_edges(G))

