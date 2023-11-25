import networkx as nx
import matplotlib.pyplot as plt
import pickle

import csv

with open('DataSets\\nodes.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    mydata = []
    y= 0
    for stri in csv_file :
        if y == 0:
            keys = stri.split(',')
            y+=1
        else:
            dicti = {
                'County':'',
                'Industry':''
            }
            stri = stri.split(',')
            dicti['County']=stri[0]
            dicti['Industry']=stri[1]

            mydata.append(dicti)
    G = nx.Graph()
    a = 0
    for n in mydata:
        G.add_node(a,county = n['County'])
        G.nodes[a]['county'] = n['County']
        G.nodes[a]['industry']= n['Industry']
        a+=1
    x = len(mydata) -1
    y = 0

    countyx = nx.get_node_attributes(G,'county')
    countyi = nx.get_node_attributes(G,'county')
    for y in range(0, x):
        for i in range(0, x):
            print(countyx[y], y)
            print(countyi[i], i)
            if countyx[y] in countyi[i]:
                if y != i:
                    G.add_edge(y, i, weight=1)
    indx = nx.get_node_attributes(G, 'industry')
    indi = nx.get_node_attributes(G, 'industry')
    for y in range(0, x):
        for i in range(0, x):

            if indx[y] in indi[i]:
                if y != i:
                    if G.has_edge(y, i) is False:
                        G.add_edge(x, i, weight=1)
                    else:
                        G[x][i]['weight'] = 2

    with open('DataSets\\RealEdgeList', 'wb') as picklefile:
        pickle.dump(G, picklefile, pickle.HIGHEST_PROTOCOL)

    with open('DataSets\\RealEdgeList', 'rb') as picklefile:
        G = nx.Graph(pickle.load(picklefile))
        indx = nx.get_edge_attributes(G, 'weight')