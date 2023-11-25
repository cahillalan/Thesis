import numpy as np
import OpenTotals


def apply_maths(mymat, biglist, b, a, c):
    total = 0
    print(biglist)
    for i in biglist:
        total += int(i[2])
    ##This finds the total for active industries in the country
    x = 0
    ## iterates through biglist
    for i in biglist:
        y = 0
        ## iterates through biglist again so that the matrix can be filled in properly, i.e 0,1 0,2 etc.
        for t in biglist:

            # density co_loc and n are set to the appropriate value
            density = int(t[2]) / total

            ## Applys the .9 for counties in the same county and .1 for others.
            if i[0] == t[0]:
                co_loc = 3
            else:
                co_loc = .1
            ## Applys 1 - b for different sector and b for same sector
            if i[1] == t[1]:
                inter_sec = 3
            else:
                inter_sec = .1

            if i[1] != t[1]:
                intra_sec = 3
            else:
                intra_sec = .1
            ## this multiplies co-loc by a and cosec by a to determine the effect of geographical contagion
            # high value for a means larger effect of geographical contagion
            coloca = co_loc * a
            interseca = inter_sec * b
            intraseca = intra_sec * c

            n = coloca + interseca + intraseca

            mymat[x][y] = n
            y += 1
        x += 1
    return mymat


def matrix_list(b, a,d):
    counties = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry',
                'Kildare', 'Kilkenny', 'Laois', 'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo',
                'Meath', 'Monaghan', 'Offaly', 'Roscommon', 'Sligo', 'Tipperary', 'Waterford', 'Westmeath',
                'Wexford', 'Wicklow']

    businesses = [
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
        "Education ",
        "Human",
        "Arts ",
        "Other ",
        "ICT ",
        "Business"]

    biglist = []
    mydata, keys = OpenTotals.open_totals()
    ## Opens the data from the csv to retrieve the data and the keys as shown in Open Totals
    distribution = OpenTotals.get_distribution(mydata, keys)
    ## Gets a distribution of the persons engaged variable for each county/sector
    c = 0
    ## Loops through the distribution and the list of counties and businesses
    ## each combination is assigned to its relative size value
    ## The combinations have been inspected and are correct
    for i in counties:
        for t in businesses:
            if int(distribution[c]['Size']) > 0:
                littlelist = []
                littlelist.append(i)
                littlelist.append(t)
                littlelist.append(distribution[c]['Size'])
                biglist.append(littlelist)
            c += 1
    ## This creates a numpy matrix of all 0's using big lists length for accuracy
    mymat = np.zeros((len(biglist), len(biglist)))

    ## This sends the matrix and list to apply_maths method
    mymat = apply_maths(mymat, biglist, b, a,d)
    ## This prints the matrix to a heatmap on the screen
    mymat /= mymat.sum(axis=1)[:, np.newaxis]
    # import matplotlib.pyplot as plt
    # plt.imshow(mymat, cmap='viridis', interpolation='none')
    # plt.show()
    for i in biglist:
        if int(i[2]) < 1:
            print(i)
    return mymat, biglist


def convert_pos(biglist):
    for i in biglist:
        if 'Carlow' in i[0]:
            i[0] = 1
        elif 'Cavan' in i[0]:
            i[0] = 2
        elif 'Clare' in i[0]:
            i[0] = 3
        elif 'Cork' in i[0]:
            i[0] = 4
        elif 'Donegal' in i[0]:
            i[0] = 5
        elif 'Dublin' in i[0]:
            i[0] = 6
        elif 'Galway' in i[0]:
            i[0] = 7
        elif 'Kerry' in i[0]:
            i[0] = 8
        elif 'Kildare' in i[0]:
            i[0] = 9
        elif 'Kilkenny' in i[0]:
            i[0] = 10
        elif 'Laois' in i[0]:
            i[0] = 11
        elif 'Leitrim' in i[0]:
            i[0] = 12
        elif 'Limerick' in i[0]:
            i[0] = 13
        elif 'Longford' in i[0]:
            i[0] = 14
        elif 'Louth' in i[0]:
            i[0] = 15
        elif 'Mayo' in i[0]:
            i[0] = 16
        elif 'Meath' in i[0]:
            i[0] = 17
        elif 'Monaghan' in i[0]:
            i[0] = 18
        elif 'Offaly' in i[0]:
            i[0] = 19
        elif 'Roscommon' in i[0]:
            i[0] = 20
        elif 'Sligo' in i[0]:
            i[0] = 21
        elif 'Tipperary' in i[0]:
            i[0] = 22
        elif 'Waterford' in i[0]:
            i[0] = 23
        elif 'Westmeath' in i[0]:
            i[0] = 24
        elif 'Wexford' in i[0]:
            i[0] = 25
        elif 'Wicklow' in i[0]:
            i[0] = 26



        if i[1] in "Mining":
            i[1] = 1
        elif i[1] in "Manufacturing":
            i[1] = 2
        elif i[1] in "Electricity":
            i[1] = 3
        elif i[1] in "Water ":
            i[1] = 4
        elif i[1] in "Construction ":
            i[1] = 5
        elif i[1] in "Wholesale ":
            i[1] = 6
        elif i[1] in "Transportation":
            i[1] = 7
        elif i[1] in "Accommodation ":
            i[1] = 8
        elif i[1] in "Information ":
            i[1] = 9
        elif i[1] in "Real estate ":
            i[1] = 10
        elif i[1] in "Professional ":
            i[1] = 11
        elif i[1] in "Financial ":
            i[1] = 12
        elif i[1] in "Administrative ":
            i[1] = 13
        elif i[1] in "Education":
            i[1] = 14
        elif i[1] in "Human":
            i[1] = 15
        elif i[1] in "Arts":
            i[1] = 16
        elif i[1] in "Other":
            i[1] = 17
        elif i[1] in "ICT ":
            i[1] = 18
        elif i[1] in "Business":
            i[1] = 19

    return biglist
