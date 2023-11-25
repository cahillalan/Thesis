import csv
import copy
import OpenTotals
import random
import numpy

def get_nodes(thedata,keys,distributions):
    newdata = []
    states = [1,2,3,4]
    for i in thedata:
        for k in keys:
            if 'Engaged' in k:
                del i[k]
            elif 'Employees' in k:
                del i[k]
        newdata.append(i)
    newdata = newdata[1:len(newdata) - 2]
    nodes = []
    print(newdata)
    print('here')
    keys2 = [
        "Business",
        "Mining",
        "Manufacturing",
        "Electricity",
        "Water ",
        "Construction ",
        "Wholesale ",
        "Transportation",
        "Accommodation ",
        "Information ",
        "Financial ",
        "Real estate ",
        "Professional ",
        "Administrative ",
        "Education",
        "Human",
        "Arts",
        "Other",
        "ICT " ]
    for i in newdata:
        # All the data is looped through
        for k, d in i.items():
            if 'County' in k:
                county = d
                #if 'County' is in the key then the county for this loop is the data for that key
            else:
                for t in keys2:
                    #otherwise the keys2 list are looped through
                    if t in k:
                        # if the keys2 element is in the key of i.item it continues
                        uniform = []
                        for dist in distributions:
                            ##loops through the distributions
                            if county in dist['County']:
                                if t in dist['Industry']:

                                    uniform = dist['Uniform']
                                    dsize = dist['Size']
                                    # distributions are looped through to find the relevant distribution
                                    ## and the correct size parameter

                        if '..' not in d:

# if the number of active enterprises in that county/sector is not null it continues
                            for y in range(0, int(d)):
                                n = {
                                    'County': county,
                                    'Industry': t,
                                    'Size':uniform[y]/int(dsize),
                                    'State':random.choice(states),
                                }


                                ## for i in the range of the number of active enterprises the loop creates
                                ## that number of nodes and appends to the nodes list
                                nodes.append(n)
    x = 0
    for y in nodes:
        y['ID'] = x
        x += 1
        ## each nodes is given an id by incrementing x in a loop through all nodes
    return nodes


def run_creator():
    mydata,keys = OpenTotals.open_totals()
    ## good to here

    adata = copy.deepcopy(mydata)

    distribution = OpenTotals.get_distribution(adata,keys)
    mydis = copy.deepcopy(distribution)
    nodes = get_nodes(mydata,keys,mydis)

    keys = nodes[0].keys()

    with open('DataSets/nodes.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(nodes)
    return

def list_to_array(nodelist):

    industrylist = []
    countylist = []
    idlist = []
    statelist = []
    sizelist = []
    for i in nodelist:
        statelist.append(i['State'])
        idlist.append(i['ID'])
        sizelist.append(i['Size'])

        if 'Carlow' in i['County']:
            countylist.append(1)
        elif 'Cavan' in i['County']:
            countylist.append(2)
        elif 'Clare' in i['County']:
            countylist.append(3)
        elif 'Cork' in i['County']:
            countylist.append(4)
        elif 'Donegal' in i['County']:
            countylist.append(5)
        elif 'Dublin' in i['County']:
            countylist.append(6)
        elif 'Galway' in i['County']:
            countylist.append(7)
        elif 'Kerry' in i['County']:
            countylist.append(8)
        elif 'Kildare' in i['County']:
            countylist.append(9)
        elif 'Kilkenny' in i['County']:
            countylist.append(10)
        elif 'Laois' in i['County']:
            countylist.append(11)
        elif 'Leitrim' in i['County']:
            countylist.append(12)
        elif 'Limerick' in i['County']:
            countylist.append(13)
        elif 'Longford' in i['County']:
            countylist.append(14)
        elif 'Louth' in i['County']:
            countylist.append(15)
        elif 'Mayo' in i['County']:
            countylist.append(16)
        elif 'Meath' in i['County']:
            countylist.append(17)
        elif 'Monaghan' in i['County']:
            countylist.append(18)
        elif 'Offaly' in i['County']:
            countylist.append(19)
        elif 'Roscommon' in i['County']:
            countylist.append(20)
        elif 'Sligo' in i['County']:
            countylist.append(21)
        elif 'Tipperary' in i['County']:
            countylist.append(22)
        elif 'Waterford' in i['County']:
            countylist.append(23)
        elif 'Westmeath' in i['County']:
            countylist.append(24)
        elif 'Wexford' in i['County']:
            countylist.append(25)
        elif 'Wicklow' in i['County']:
            countylist.append(26)


        if i['Industry'] in "Mining":
            industrylist.append(2)
        elif i['Industry'] in "Manufacturing":
            industrylist.append(3)
        elif i['Industry'] in"Electricity":
            industrylist.append(4)
        elif i['Industry'] in "Water ":
            industrylist.append(5)
        elif i['Industry'] in "Construction " :
            industrylist.append(6)
        elif i['Industry'] in "Wholesale ":
            industrylist.append(7)
        elif i['Industry'] in "Transportation":
            industrylist.append(8)
        elif i['Industry'] in "Accommodation ":
            industrylist.append(9)
        elif i['Industry'] in "Information ":
            industrylist.append(10)
        elif i['Industry'] in "Real estate ":
            industrylist.append(11)
        elif i['Industry'] in "Professional ":
            industrylist.append(12)
        elif i['Industry'] in "Financial ":
            industrylist.append(13)
        elif i['Industry'] in "Administrative ":
            industrylist.append(14)
        elif i['Industry'] in "Education":
            industrylist.append(15)
        elif i['Industry'] in "Human":
            industrylist.append(16)
        elif i['Industry'] in "Arts":
            industrylist.append(17)
        elif i['Industry'] in "Other":
            industrylist.append(18)
        elif i['Industry'] in "ICT ":
            industrylist.append(19)
        elif i['Industry'] in "Business":
            industrylist.append(20)
    idmat = numpy.array(idlist)
    industrymat = numpy.array(industrylist)
    statemat = numpy.array(statelist)
    countymat = numpy.array(countylist)
    sizemat = numpy.array(sizelist)


    return idmat,industrymat,statemat,countymat,sizemat