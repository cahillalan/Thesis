import numpy as np
import csv
import Matrix
import markovchainProbtets
import random

def choose_random(nodelist):
    n = random.randint(0, len(nodelist))
    node = nodelist[n]
    return node

def apply_bankruptcy(nodelist, position):

    nodelist[position]['Bankruptcy'] = 1
    return nodelist

def open_nodes():
    with open('DataSets\\nodes.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        y = 0
        nodelist = []

        for i in csv_file:
            if y > 0:
                n = {
                    'County': '',
                    'Industry': '',
                    'Size':0,
                    'State' : 0,
                    'ID':0
                }

                mystr = i.split(',')


                n['County'] = mystr[0]
                n['Industry'] = mystr[1]
                n['Size'] = float(mystr[2].strip('\n'))
                n['State'] = int(mystr[3].strip('\n'))
                n['ID'] = int(mystr[4].strip('\n'))

                nodelist.append(n)
            y+=1

        return nodelist

        mymat = np.zeros((513, 513))
        positions = []
        mymat, positions = Matrix.matrix_list(.2,.1)
        return
        for i in range(10):
            bnode = choose_random(nodelist)
            enode = choose_random(nodelist)
            p = markovchainProbtets.calculateprob(bnode,enode,positions,mymat)
            print(p)



