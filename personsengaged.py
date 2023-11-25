import csv

with open('DataSets\\totals.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    mydata = []
    y=0
    for stri in csv_file :
        if y == 0:
            keys = stri.split(',')
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

            mystr = stri.split(',')
            a = 0
            for s in mystr:
                dicti[keys[a]]= s
                a+=1

            mydata.append(dicti)
            y+=1
    ## good to here
    newdata =[]
    for i in mydata:
         for k in keys:
             if 'Engaged' in k:
                 del i[k]
             elif 'Enterprises' in k:
                 del i[k]
         newdata.append(i)
    newdata = newdata[1:len(newdata) - 2]
    nodes = []
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
        "Education ",
        "Human",
        "Arts ",
        "Other ",
        "ICT ", ]

    print(newdata)
    for i in newdata:
        for k, d in i.items():
            if 'County' in k:
                county = d
            else:
                for t in keys2:
                    if t in k:

                        if '..' not in d:
                                n = {
                                    'County': county,
                                    'Industry': t,
                                    'Size': d
                                }
                                nodes.append(n)
                        else:
                            n ={
                                'County':county,
                                'Industry':t,
                                'Size':0
                            }

    keys = nodes[0].keys()
    with open('DataSets\\industrysize.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys, lineterminator='\n')
        dict_writer.writeheader()
        dict_writer.writerows(nodes)


