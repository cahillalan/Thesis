import Matrix
import csv
import numpy
import MarkovChain
import copy


def choose_contagion_type():
    print('Please Enter the Level of Geographical Contagion between 0.0 - 1.0 ')
    a = float(input())
    print('Please Enter the Level of Intra-Industry Contagion between 0.0 - 1.0 ')
    b = float(input())
    return a,b

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
                    'Size': 0,
                    'State': 0,
                    'ID': 0
                }

                mystr = i.split(',')

                n['County'] = mystr[0]
                n['Industry'] = mystr[1]
                n['Size'] = float(mystr[2].strip('\n'))
                n['State'] = int(mystr[3].strip('\n'))
                n['ID'] = int(mystr[4].strip('\n'))

                nodelist.append(n)
            y += 1
        return nodelist

def createrows(nodelist,positions):
    sizelist = []
    idlist = []
    for dic in positions:
        ids =[]
        sizes =[]
        for node in nodelist:
            if node['County'] in dic[0] and node['Industry'] in dic[1]:
                ids.append(node['ID'])
                sizes.append(node['Size'])
        sizelist.append(sizes)
        idlist.append(ids)
    total = []
    for i in sizelist:
        total.append(sum(i))
    for i in range(len(sizelist)):
        sizelist[i] = [n/total[i] for n in sizelist[i]]
    #sizeprob = [n / total for n in sizelist]
    idmat = numpy.array(idlist)
    sizemat = numpy.array(sizelist)
    #sizemat /= numpy.sum(sizemat)
    return sizemat,idmat

def choose_random(nodelist):
    n = numpy.random.randint(0, len(nodelist))
    node = nodelist[n]
    return node

def getSimData(a,b):
    nodelist = open_nodes()
    ##a,b = choose_contagion_type()
    c = Matrix.matrix_list(b, a)
    return c, nodelist

def getrandomandaffected(nodelist,  aggmatrix, positions,mortalitynumber,idrow,sizerow):
    bnode = choose_random(nodelist)
    mortalitynumber += 1
    affected = choose_affected(nodelist, bnode, aggmatrix, positions,idrow,sizerow)
    paffected= createdeepcopy(affected)
    return bnode,affected,paffected, mortalitynumber

def createdeepcopy(affected):
    paffected = []
    for i in affected:
        paffected.append(i['State'])
    return paffected


def applymarkovchain(affected,mortalitynumber,nodelist):
    newaffected = []
    mortalityrate = mortalitynumber/len(nodelist)
    for i in affected:
        newaffected.append(MarkovChain.setState(i,mortalityrate))
    return newaffected

def applynewstates(bnode,newaffected,nodelist):
    nodelist[bnode['ID']]['State'] = 4
    for i in newaffected:
        nodelist[i['ID']]['State'] = i['State']
    return nodelist

def checknewbankruptcy(paffected,newaffected,nodelist,aggmatrix,positions,mortalitynumber,idrow,sizerow):
    for i in range(len(newaffected)):
        if newaffected[i]['State'] == 4:
            bnode = newaffected[i]
            if paffected[i] < 4 :
                mortalitynumber +=1
                nodelist,mortalitynumber = runcontagion(bnode,nodelist,aggmatrix,positions,mortalitynumber,idrow,sizerow)
    return nodelist, mortalitynumber

def runcontagion(bnode,nodelist,aggmatrix,positions,mortalitynumber,idrow,sizerow):
    affected = choose_affected(nodelist, bnode, aggmatrix, positions,idrow,sizerow)
    paffected = createdeepcopy(affected)
    newaffected = applymarkovchain(affected,mortalitynumber,nodelist)
    nodelist = applynewstates(bnode, newaffected, nodelist)
    nodelist, mortalitynumber = checknewbankruptcy(paffected, newaffected, nodelist, aggmatrix, positions,mortalitynumber,idrow,sizerow)

    return nodelist, mortalitynumber

def choose_affected(nodelist,node,aggmatrix,positions,idmat,sizemat):
    position = 0
    ## finds which row to use in the aggmatrix from the positions list
    for i,dic in enumerate(positions):
        if node['County'] in dic[0] and node['Industry'] in dic[1]:
            position = i
    # this chooses the row in question and then standardises it to an integer
    row = aggmatrix[position,:]
    row = row.tolist()
    pos = []
    for i in range(len(row)):
        pos.append(i)
    countysector = []
    ## this chooses a random index from the list of index's
    for i in range(4):
        countysector.append(numpy.random.choice(pos,p=row))
    affected =[]
    ## this chooses a random company from the list of companies from the specific index
    for i in range(len(countysector)):
        idrow = idmat[position]
        sizerow = sizemat[position]
        Id = numpy.random.choice(idrow, replace=False, p=sizerow)
        for i in nodelist:
            if i['ID'] == Id:
                affected.append(i)
                break
    return affected

def runsimulation(nodelist,aggmatrix,positions,sizerow,idrow):


    mortalitynumber = 0

    bnode, affected, paffected,mortalitynumber = getrandomandaffected(nodelist, aggmatrix, positions,mortalitynumber,idrow,sizerow)
    newaffected = applymarkovchain(affected,mortalitynumber,nodelist)
    nodelist = applynewstates(bnode, newaffected, nodelist)
    nodelist,mortalitynumber = checknewbankruptcy(paffected, newaffected, nodelist, aggmatrix, positions,mortalitynumber,idrow,sizerow)
    return mortalitynumber

