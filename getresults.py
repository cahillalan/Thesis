import norecursiontest
import NodeCreator
import datetime
import random
import csv
import contagion_simulatorfirstdraft
import contagion_simulator
import contagion_simulator_nobabc

def randomise_states(statemat):
    states = [1,2,3]
    for i in range(len(statemat)):
        statemat[i] = random.choice(states)
    return statemat
def runnormal():
    start = datetime.datetime.now()
    avector = [.1,.5,.9]
    bvector = [.1,.5,.9]
    myseed = 101
    results = []
    for a in avector:
        for b in bvector:


            NodeCreator.run_creator()
            t, nodelist = contagion_simulatorfirstdraft.getSimData(a, b)
            aggmatrix, positions = t
            sizerow, idrow = contagion_simulatorfirstdraft.createrows(nodelist, positions)
            for i in range(100):
                mydict = {}
                nodelist = randomise_states(nodelist)
                mortalitynumber = contagion_simulatorfirstdraft.runsimulation(nodelist, aggmatrix, positions, sizerow, idrow)
                myseed += 100
                mydict['Seed'] = myseed
                print(mydict['Seed'])
                print(myseed)
                random.seed(a = myseed)
                mydict['Mortality'] = mortalitynumber
                mydict['A'] = a
                mydict['B'] = b
                results.append(mydict)


    keys = results[0].keys()

    with open('DataSets\\SimResults.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)


    print(start)
    print(datetime.datetime.now())

def runsimulationOne():

    import contagionsimulator_nob
    start = datetime.datetime.now()
    lower = .25
    higher = 2
    f = 0
    avector = [.1, .5, .9]
    bvector = [.1, .5, .9]
    cvector = [.1, .3,.6, .9]
    myseed = datetime.datetime.now()
    results = []
    for d in avector:
        for b in bvector:

            t, nodelist = contagionsimulator_nob.getSimData(d, b)
            idmat, industrymat, statemat, countymat, sizemat = NodeCreator.list_to_array(nodelist)
            aggmatrix, positions = t
            sizerow, idrow, positions =contagionsimulator_nob.createrows(nodelist, positions)
            print('newrun')
            for i in range(1000):
                mydict = {}
                f+=1
                print(f)
                statemat = randomise_states(statemat)
                mortalitynumber = contagionsimulator_nob.runsimulation(idmat, industrymat, statemat, countymat,
                                                                    sizemat, aggmatrix, positions, sizerow,
                                                                    idrow)
                myseed = datetime.datetime.now()
                mydict['Seed'] = myseed
                random.seed(a=myseed)
                mydict['Mortality'] = mortalitynumber
                mydict['A'] = d
                mydict['B'] = b

                results.append(mydict)

    print(mortalitynumber)
    keys = results[0].keys()

    with open('DataSets/Sim1Results4effectedlowerhighernob13.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print(start)
    print(datetime.datetime.now())

def runsimulationTwo():
    import contagion_simulator_2000
    lower = .25
    higher = 2
    start = datetime.datetime.now()
    avector = [.1, .5, .9]
    bvector = [.1, .5, .9]
    cvector = [.1, .5, .9]
    myseed = datetime.datetime.now()
    results = []
    for d in avector:
        for b in bvector:

            t, nodelist = contagion_simulator_2000.getSimData(d, b)
            idmat, industrymat, statemat, countymat, sizemat = NodeCreator.list_to_array(nodelist)
            aggmatrix, positions = t

            print(type(aggmatrix))
            sizerow, idrow, positions = contagion_simulator_2000.createrows(nodelist, positions)
            print('now')
            for i in range(100):
                mydict = {}

                print(myseed)
                statemat = randomise_states(statemat)
                mortalitynumber,times = contagion_simulator_2000.runsimulation(idmat, industrymat, statemat, countymat,
                                                                       sizemat, aggmatrix, positions, sizerow,
                                                                       idrow)
                myseed =datetime.datetime.now()
                end = datetime.datetime.now()
                mydict['Seed'] = myseed
                random.seed(a=myseed)
                mydict['Times'] = times
                mydict['A'] = d
                mydict['B'] = b
                mydict['Time'] = end - start

                results.append(mydict)

    print(mortalitynumber)
    keys = results[0].keys()

    with open('DataSets/Sim1Results4effectedlowerhigher20007.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print(start)
    print(datetime.datetime.now())

def runsimulationThree():

    import contagion_simulator_5
    lower = .25
    higher = 2
    f = 0
    start = datetime.datetime.now()
    avector = [.1, .5, .9]
    bvector = [.1, .5, .9]
    cvector = [.1, .3,.6, .9]
    myseed = datetime.datetime.now()
    results = []
    for d in avector:
        for b in bvector:

            t, nodelist = contagion_simulator_5.getSimData(d, b)
            idmat, industrymat, statemat, countymat, sizemat = NodeCreator.list_to_array(nodelist)
            aggmatrix, positions = t

            sizerow, idrow, positions =contagion_simulator_5.createrows(nodelist, positions)
            print('newrun')
            for i in range(1000):
                mydict = {}
                f+=1
                print(f)
                statemat = randomise_states(statemat)
                mortalitynumber,numaffected = contagion_simulator_5.runsimulation(idmat, industrymat, statemat, countymat,
                                                                      sizemat, aggmatrix, positions, sizerow,
                                                                      idrow)
                myseed = datetime.datetime.now()
                mydict['Seed'] = myseed
                random.seed(a=myseed)
                mydict['Mortality'] = mortalitynumber
                mydict['NumAffected'] = numaffected
                mydict['A'] = d
                mydict['B'] = b

                results.append(mydict)

    print(mortalitynumber)
    keys = results[0].keys()

    with open('DataSets/Sim1Results42.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print(start)
    print(datetime.datetime.now())
def runsimulationFour():

    import contagion_simulator_5
    lower = .25
    higher = 2
    f = 0
    start = datetime.datetime.now()
    avector = [.1, .5, .9]
    bvector = [.1, .5, .9]
    cvector = [.1, .3,.6, .9]
    myseed = datetime.datetime.now()
    results = []
    for d in avector:
        for b in bvector:

            t, nodelist = contagion_simulator_5.getSimData(d, b)
            idmat, industrymat, statemat, countymat, sizemat = NodeCreator.list_to_array(nodelist)
            aggmatrix, positions = t

            sizerow, idrow, positions =contagion_simulator_5.createrows(nodelist, positions)
            print('newrun')
            for i in range(1000):
                mydict = {}
                f+=1
                print(f)
                statemat = randomise_states(statemat)
                mortalitynumber, numaffected = contagion_simulator_5.runsimulation(idmat, industrymat, statemat,
                                                                                   countymat,
                                                                                   sizemat, aggmatrix, positions,
                                                                                   sizerow,
                                                                                   idrow)
                myseed = datetime.datetime.now()
                mydict['Seed'] = myseed
                random.seed(a=myseed)
                mydict['Mortality'] = mortalitynumber
                mydict['NumAffected'] = numaffected
                mydict['A'] = d
                mydict['B'] = b

                results.append(mydict)

    print(mortalitynumber)
    keys = results[0].keys()

    with open('DataSets/Sim1Results41.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print(start)
    print(datetime.datetime.now())

def runsimulationFive():

    import contagion_simulator10
    lower = .25
    higher = 2
    f = 0
    start = datetime.datetime.now()
    avector = [.1, .5, .9]
    bvector = [.1, .5, .9]
    cvector = [.1, .3,.6, .9]
    myseed = datetime.datetime.now()
    results = []
    for d in avector:
        for b in bvector:

            t, nodelist = contagion_simulator10.getSimData(d, b)
            idmat, industrymat, statemat, countymat, sizemat = NodeCreator.list_to_array(nodelist)
            aggmatrix, positions = t

            sizerow, idrow, positions =contagion_simulator10.createrows(nodelist, positions)
            print('newrun')
            for i in range(500):
                mydict = {}
                f+=1
                print(f)
                statemat = randomise_states(statemat)
                mortalitynumber,numaffected = contagion_simulator10.runsimulation(idmat, industrymat, statemat, countymat,
                                                                      sizemat, aggmatrix, positions, sizerow,
                                                                      idrow)
                myseed = datetime.datetime.now()
                mydict['Seed'] = myseed
                random.seed(a=myseed)
                mydict['Mortality'] = mortalitynumber
                mydict['NumAffected'] = numaffected
                mydict['A'] = d
                mydict['B'] = b

                results.append(mydict)

    print(mortalitynumber)
    keys = results[0].keys()

    with open('DataSets/Sim1Results10.csv', 'w+') as output_file:
        dict_writer = csv.writer(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print(start)
    print(datetime.datetime.now())
def createAgg():
    import pandas as pd
    import contagionsimulator_nob
    start = datetime.datetime.now()

    d = .1
    b = .1
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg11.csv")
    print(type(aggmatrix))
    d = .5
    b = .1
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg51.csv")

    d = .1
    b = .5
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg15.csv")

    d = .9
    b = .1
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg91.csv")

    d = .1
    b = .9
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg19.csv")

    d = .5
    b = .5
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg55.csv")

    d = .5
    b = .9
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg59.csv")

    d = .9
    b = .5
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg95.csv")
    d = .9
    b = .9
    t, nodelist = contagionsimulator_nob.getSimData(d, b)
    aggmatrix, positions = t
    pd.DataFrame(aggmatrix).to_csv("DataSets/Agg99.csv")
    print(start)
    print(datetime.datetime.now())

createAgg()