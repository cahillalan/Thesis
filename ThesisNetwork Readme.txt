ThesisNetwork

Author: Alan Cahill
Student Number: 19204003

Order of file execution:
1. DataConversion.py
This file uses python to re-format the data into usable structures.
2. NodeCreator.py
This file creates nodes of individual companies that exist within the dataset.
3. EdgeList.py
This file creates an edge list from the nodes that connects nodes to eachother based off county and industry.
4. Network.py
This file uses networkx to create and display using matplotlib a network created from the edge list. 

Seperate file:
networktest.py
This file is used a test to ensure the structure of the network in network.py is viable.
This is needed as Network.py takes too long to test. 