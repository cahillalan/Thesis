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
    # for each position a row is created with the Id and size of the companies
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
    # this standardises teh rows by dividing by the total
    for i in sizelist:
        total.append(sum(i))
    for i in range(len(sizelist)):
        sizelist[i] = [n/total[i] for n in sizelist[i]]
    # converts lists to numpy array
    idmat = numpy.array(idlist)
    sizemat = numpy.array(sizelist)
    # converts postitions to numerical values
    positions = Matrix.convert_pos(positions)
    return sizemat, idmat, positions

def choose_random(idmatfull,industrymat,statemat,countymat,):
    # chooses a random company id
    n = numpy.random.randint(0, len(idmatfull)-1)
    node = []
    # appends that companies data to a list by referincing the matrix's
    node.append(idmatfull[n])
    node.append(industrymat[n ])
    node.append(statemat[n ])
    node.append(countymat[n ])
    return node

def getSimData(a,b,c):
    nodelist = open_nodes()
    # gets the data from nodelist and matrixlist
    c = Matrix.matrix_list(b, a,c)
    return c, nodelist

def getrandomandaffected(idmatfull,industrymat,statemat,countymat,  aggmatrix, positions,mortalitynumber,idrow,sizerow):
    # calling the random company selector
    bnode = choose_random(idmatfull,industrymat,statemat,countymat)
    mortalitynumber += 1
    # chooses the affected companies
    affected = choose_affected(idmatfull,statemat, bnode, aggmatrix, positions,idrow,sizerow)
    # creates a copy of the affected companies data
    paffected= createdeepcopy(affected)
    return bnode,affected,paffected, mortalitynumber

def createdeepcopy(affected):
    paffected = []
    # simply creates a copy of affected
    for i in affected:
        paffected.append(i)

    return paffected


def applymarkovchain(affected,mortalitynumber,idmatfull,statemat,fullsizemat):
    newaffected = []
    mortalityrate = mortalitynumber/len(idmatfull)
    # send the state and size of each effected company to the markov chain, then saves the relevant data to a list
    for i in affected:
        node =[]
        node.append(i[0])
        node.append(MarkovChain.setState(i[1],fullsizemat[i[0]],mortalityrate))
        newaffected.append(node)
    return newaffected

def applynewstates(bnode,newaffected,idmatfull,statemat):
    # makes the random node bankrupt in the statematrix
    statemat[bnode[0]]= 4
    # alters the newaffected states in the state matrix
    for i in newaffected:
        statemat[i[0]] = i[1]
    return statemat

def checknewbankruptcy(paffected,newaffected,idmatfull,industrymat,statemat,countymat,sizemat,aggmatrix,positions,mortalitynumber,idrow,sizerow):
    # for each new effected
    for i in range(len(newaffected)):
        # if it is bankrupts
        if newaffected[i][1] == 4:
            bnode = newaffected[i]
            # it becomes the node

            # if it was previously not bankrupt
            if paffected[i][1] < 4 :
                mortalitynumber +=1
                # it is sent to contagion propogation
                statemat,mortalitynumber = runcontagion(bnode,idmatfull,industrymat,statemat,countymat,sizemat,aggmatrix,positions,mortalitynumber,idrow,sizerow)
    return statemat, mortalitynumber

def runcontagion(bnode,idmatfull,industrymat,statemat,countymat,sizemat,aggmatrix,positions,mortalitynumber,idrow,sizerow):
    # this runs a node through contagion for nodes that have newly become bankrupt
    affected = choose_affected(idmatfull,statemat,bnode,aggmatrix,positions,idrow,sizerow)
    paffected = createdeepcopy(affected)
    newaffected = applymarkovchain(affected,mortalitynumber,idmatfull,statemat,sizemat)
    statemat = applynewstates(bnode, newaffected,idmatfull,statemat)
    statemat,mortalitynumber = checknewbankruptcy(paffected, newaffected, idmatfull,industrymat,statemat,countymat,sizemat, aggmatrix, positions,mortalitynumber,idrow,sizerow)

    return statemat, mortalitynumber

def choose_affected(idmatfull,statemat,node,aggmatrix,positions,idmat,sizemat):
    position = 0
    ## finds which row to use in the aggmatrix from the positions list
    for i,dic in enumerate(positions):
        if node[0] == dic[0] and node[1] == dic[1]:
            position = i
    # this chooses the row in question and then standardises it to an integer
    row = aggmatrix[position,:]
    row = row.tolist()
    pos = []
    for i in range(len(row)):
        pos.append(i)
    countysector = []
    ## this chooses a random index from the list of index's with row being used to weight the decision
    for i in range(4):
        countysector.append(numpy.random.choice(pos,p=row))
    affected =[]
    ## for each index in countysector
    for i in range(len(countysector)):
        # the row is chosen for the size and id position relevant matrixs
        idrow = idmat[position]
        sizerow = sizemat[position]
        # and id is chosen at random using size as a weight
        Id = numpy.random.choice(idrow, replace=False, p=sizerow)
        #the companies data is added to a list and appended to another list
        node = [idmatfull[Id],statemat[Id]]
        affected.append(node)

    return affected

def runsimulation(idmatfull,industrymat,statemat,countymat,sizemat,aggmatrix,positions,sizerow,idrow):

    times = 0
    mortalitynumber = 0

    ## This calls the getrandom affected function to retrieve a random company and the affected companies
    bnode, affected, paffected,mortalitynumber = getrandomandaffected(idmatfull,industrymat,statemat,countymat, aggmatrix, positions,mortalitynumber,idrow,sizerow)
    newaffected = applymarkovchain(affected,mortalitynumber,idmatfull,statemat,sizemat)
    statemat = applynewstates(bnode, newaffected,idmatfull,statemat)
    statemat,mortalitynumber = checknewbankruptcy(paffected, newaffected, idmatfull,industrymat,statemat,countymat,sizemat, aggmatrix, positions,mortalitynumber,idrow,sizerow)
    return mortalitynumber

