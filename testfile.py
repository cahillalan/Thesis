def testchoice(nodelist):
    companies = []
    for t in nodelist:
        if t['County'] in 'Dublin':
            if t['Industry'] in 'Business':
                companies.append(t)
    affected = []
    companylist = []
    for i in companies:
        for t in range(int(i['Size']*100)):
            companylist.append(i['ID'])
    Id = numpy.random.choice(companylist)
    for i in nodelist:
        if i['ID'] == Id:
            affected.append(i)
            break

    return affected


def testselection():
    a, nodelist = getSimData()
    aggmatrix, positions = a
    for i in positions:
        print(i)
    mortalitynumber = 0
    companylist = []
    bnode = choose_random(nodelist)
    for i in range(100000):
        affected = choose_three_affected(nodelist, bnode, aggmatrix, positions)
        for i in affected:
            companylist.append(i['Size'])

    from matplotlib import pyplot as plt
    print('here')
    plt.hist(companylist)
    plt.show()
    print(companylist)
    return



def runtestchoice():
    a, nodelist = getSimData()
    companylist = []
    for i in range(10000):
        affected = testchoice(nodelist)
        companylist.append(affected[0]['Size'])

    from matplotlib import pyplot as plt
    print('here')
    plt.hist(companylist)
    plt.show()
    print(companylist)



def choose_three_affected(nodelist,node,aggmatrix,positions):
    position = 0
    ## finds which row to use in the aggmatrix from the positions list
    for i,dic in enumerate(positions):
        if node['County'] in dic[1] and node['Industry'] in dic[1]:
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
        choice = positions[countysector[i]]
        companies = [t for t in nodelist if t['County']in choice[0] and t['Industry'] in choice[1]]
        companylist = []
        size = []
        for i in companies:
            companylist.append(i['ID'])
            size.append(i['Size'])
        total = sum(size)
        sizeprob = [n/total for n in size]
        Id = numpy.random.choice(companylist,replace = False,p = sizeprob)
        for i in nodelist:
            if i['ID'] == Id:
                affected.append(i)
                break
    return affected
