import csv

with open('DataSets\\totals.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')

    mydata = []
    y= 0
    for stri in csv_file :
        if y == 0:
            keys = stri.split(',')
            y+=1
            print(keys)
        else:
            dicti = {
                'County':'',
                'Industry':''
            }

            dicti['County']=stri[0]
            dicti['Industry']=stri[1]

            mydata.append(dicti)

