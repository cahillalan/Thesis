import csv
import numpy

def open_totals():
    # this opens the totals.csv and saves it to a dictionary for use elsewhere
    with open('DataSets//totals.csv') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        mydata = []
        y=0
        for stri in readCSV :
            if y == 0:
                keys = stri
                y+=1
            else:
                dicti = {
                    "County" : '',


                    "Mining Active Enterprises": '',
                    "Mining Person Engaged": '',
                    "Mining Employees": '',

                    "Manufacturing Active Enterprises": '',
                    "Manufacturing Person Engaged": '',
                    "Manufacturing Employees": '',

                    "Electricity Active Enterprises": '',
                    "Electricity Person Engaged": '',
                    "Electricity Employees": '',

                    "Water Active Enterprises": '',
                    "Water Person Engaged": '',
                    "Water Active Employees": '',

                    "Construction Active Enterprises": '',
                    "Construction Person Engaged": '',
                    "Construction Employees": '',

                    "Wholesale Active Enterprises": '',
                    "Wholesale Person Engaged": '',
                    "Wholesale Employees": '',

                    "Transportation Active Enterprises": '',
                    "Transportation Person Engaged": '',
                    "Transportation Employees": '',

                    "Accommodation Active Enterprises": '',
                    "Accommodation Person Engaged": '',
                    "Accommodation Employees": '',

                    "Information Active Enterprises": '',
                    "Information Person Engaged": '',
                    "Information Employees": '',

                    "Financial Active Enterprises": '',
                    "Financial Person Engaged": '',
                    "Financial Employees": '',

                    "Real estate Active Enterprises": '',
                    "Real estate Person Engaged": '',
                    "Real estate Employees": '',

                    "Professional Active Enterprises": '',
                    "Professional Person Engaged": '',
                    "Professional Employees": '',

                    "Administrative Active Enterprises": '',
                    "Administrative Person Engaged": '',
                    "Administrative Employees": '',

                    "Education Active Enterprises": '',
                    "Education Person Engaged": '',
                    "Education Active Employees": '',

                    "Human Activities Active Enterprises": '',
                    "Human Activities Person Engaged": '',
                    "Human Activities Employees": '',

                    "Arts Active Enterprises": '',
                    "Arts Person Engaged": '',
                    "Arts Active Employees": '',

                    "Other Active Enterprises": '',
                    "Other Person Engaged": '',
                    "Other Active Employees": '',

                    "ICT Active Enterprises": '',
                    "ICT Person Engaged": '',
                    "ICT Active Employees": '',

                    "Business Active Enterprises": '',
                    "Business Person Engaged": '',
                    "Business Employees": '',
                    "Missing":'',
                    "Missing": ''

                }

                a = 0
                for s in stri:
                    dicti[keys[a]]= s
                    a+=1

                mydata.append(dicti)
                y+=1

        return mydata,keys

def get_uniform(h,size):
    # if the size attribute is '..' then size is zero
    if '..' in size:
        size = 0
    # a numpy matrix of a uniform distribution of lenght size is created
    a = numpy.random.uniform(low=0.0, high=1.0, size=int(float(size)))
    a.tolist()

    # the matrix is converted to a list
    nsize = []
    mylist = []
    ## the probabilities are multiplied by the size attribute to create a size attribute in a distribution
    for i in a:
        d = int(float(i) * int(h))
        mylist.append(d)
    return mylist



def get_distribution(adata,keys):
    newdata = []
    for i in adata:
        for k in keys:
            if 'Employees' in k:
                del i[k]
        newdata.append(i)
    newdata = newdata[1:len(newdata) - 2]
    mylist = []
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
        "ICT ", ]
    industry = '0'
## The data is looped through to find the appropriate county and sector combinations
    for i in newdata:
        for k, d in i.items():

            if 'County' in k:
                county = d
            elif 'Enterprises' in k:
                if '..' in d:
                    industry = '0'
                else:
                    industry = d
            else:
                for t in keys2:

                    if t in k:
                        if '..' not in d:
                    # if the active companies in the county sector attribute is not '..' then the uniform is
                    #retrieved for that county and sector using get_uniform()
                    #it is added to the dictionary which is appened to the list
                            n = {
                                'County': county,
                                'Industry': t,
                                'Size': d,
                                'Uniform': get_uniform(d,industry)
                            }
                            mylist.append(n)
                        else:
                            n = {
                                'County': county,
                                'Industry': t,
                                'Size': '0',
                                'Uniform': get_uniform(0,industry)
                            }

                            mylist.append(n)
    return mylist