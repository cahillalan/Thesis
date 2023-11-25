import csv
import re

with open('DataSets\\202022414314515458913BRA1852348602550.csv') as csv_file:
    readCSV = csv.reader(csv_file, delimiter=',')
    # this reads in the csv file and saves it to a list.
    all_data = []
    a = 0
    b = 0
    c = 0
    d = 1
    business_list = []
    for stri in csv_file:
        a += 1

        if a < 4:
            print(a)
        elif a == 4:
            business = stri
            b += 1
            c += 1
        else:
            c +=1
        ## b is used to seperate active enterprise, employees engaged and county
        ## at position 1 and every 113 steps there is a heading, therefore when c-d is 113 d is equal to c
        ## then each time 113 steps are taken c-d will equal 113 meaning the if statment will not be entered
            if c < 1 or c - d != 113:
                if b == 1:
                    my_list =[]
                    ## All strings are santised as below. Then added to a list
                    county = stri.replace(',','').replace('"','').replace(' ','').rstrip()
                    my_list.append(business)
                    my_list.append(county)
                    b += 1
                elif b == 2:
                    activeEnt = stri

                    index = activeEnt.find('(Number)",')
                    activeEnt = activeEnt[index:].strip('(Number)",').split(',')
                    if len(activeEnt) >8:
                        activeEnt = activeEnt[9].rstrip()

                    my_list.append(activeEnt)
                    b += 1
                elif b == 3:
                    personEng = stri
                    index = personEng.find('(Number)",')
                    personEng = personEng[index:].strip('(Number)",').split(',')
                    if len(personEng) > 8:
                        personEng = personEng[9].rstrip()
                    my_list.append(personEng)
                    b += 1
                elif b == 4:
                    employee = stri
                    index = employee.find('(Number)",')
                    employee = employee[index:].strip('(Number)",').split(',')
                    if len(employee) > 8:
                        employee = employee[9].rstrip()
                    b = 1
                    my_list.append(employee)
                    all_data.append(my_list)



            else:
                business = stri.rstrip()
                business_list.append(business)
                b = 1
                d = c
    #individual county lists are created and appended to the all_lists list.
    all_lists = []
    AllCounties =[]
    Carlow=[]
    Cavan=[]
    Clare=[]
    Cork=[]
    Donegal=[]
    Dublin=[]
    Galway=[]
    Kerry=[]
    Kildare=[]
    Kilkenny=[]
    Laois=[]
    Leitrim=[]
    Limerick=[]
    Longford=[]
    Louth=[]
    Mayo=[]
    Meath=[]
    Monaghan=[]
    Offaly=[]
    Roscommon=[]
    Sligo=[]
    Tipperary=[]
    Waterford=[]
    Westmeath=[]
    Wexford=[]
    Wicklow=[]
    Unknown=[]
    Mining=[]
    Manufacturing=[]
    Electricity=[]
    Water=[]
    Construction=[]
    Wholesale=[]
    Transportation =[]
    Accommodation=[]
    Information=[]
    Financial =[]
    Realestate=[]
    Professional=[]
    Administrative=[]
    Education=[]
    Human=[]
    Arts=[]
    Other =[]
    ICT =[]
    all_lists.append(AllCounties)
    all_lists.append(Carlow )
    all_lists.append(Cavan )
    all_lists.append( Clare )
    all_lists.append(Cork )
    all_lists.append( Donegal )
    all_lists.append( Dublin )
    all_lists.append(Galway )
    all_lists.append(Kerry )
    all_lists.append(Kildare )
    all_lists.append( Kilkenny )
    all_lists.append(Laois )
    all_lists.append(Leitrim )
    all_lists.append(Limerick )
    all_lists.append(Longford )
    all_lists.append(Louth )
    all_lists.append(Mayo )
    all_lists.append(Meath)
    all_lists.append(Monaghan)
    all_lists.append(Offaly )
    all_lists.append(Roscommon)
    all_lists.append(Sligo )
    all_lists.append(Tipperary )
    all_lists.append(Waterford )
    all_lists.append(Westmeath)
    all_lists.append(Wexford )
    all_lists.append( Wicklow )
    all_lists.append(Unknown )
    all_industry = []
    all_industry.append(Mining )
    all_industry.append(Manufacturing )
    all_industry.append(Electricity )
    all_industry.append(Water )
    all_industry.append(Construction )
    all_industry.append(Wholesale )
    all_industry.append(Transportation )
    all_industry.append(Accommodation )
    all_industry.append(Information )
    all_industry.append(Financial )
    all_industry.append(Realestate )
    all_industry.append(Professional )
    all_industry.append(Administrative )
    all_industry.append(Education )
    all_industry.append(Human )
    all_industry.append(Arts )
    all_industry.append(Other )
    all_industry.append(ICT)
    ## All the data is looped through and if a county appears in teh list it is appened to its parent list
    for i in all_data:
        if 'AllCounties' in i:
            AllCounties.append(i)
        if 'Carlow' in i:
            Carlow.append(i)
        if 'Cavan' in i:
            Cavan.append(i)
        if 'Clare' in i:
            Clare.append(i)
        if 'Cork' in i:
            Cork.append(i)
        if 'Donegal' in i:
            Donegal.append(i)
        if 'Dublin' in i:
            Dublin.append(i)
        if 'Galway' in i:
            Galway.append(i)
        if 'Kerry' in i:
            Kerry.append(i)
        if 'Kildare' in i:
            Kildare.append(i)
        if 'Kilkenny' in i:
            Kilkenny.append(i)
        if 'Laois' in i:
            Laois.append(i)
        if 'Leitrim' in i:
            Leitrim.append(i)
        if 'Limerick' in i:
            Limerick.append(i)
        if 'Longford' in i:
            Longford.append(i)
        if 'Louth' in i:
            Louth.append(i)
        if 'Mayo' in i:
            Mayo.append(i)
        if 'Meath' in i:
            Meath.append(i)
        if 'Monaghan' in i:
            Monaghan.append(i)
        if 'Offaly' in i:
            Offaly.append(i)
        if 'Roscommon' in i :
            Roscommon.append(i)
        if 'Sligo' in i:
            Sligo.append(i)
        if 'Tipperary' in i:
            Tipperary.append(i)
        if 'Waterford' in i:
            Waterford.append(i)
        if 'Westmeath' in i:
            Westmeath.append(i)
        if  'Wexford' in i:
            Wexford.append(i)
        if 'Wicklow' in i:
            Wicklow.append(i)
        if 'Unknown' in i:
            Unknown.append(i)
        if "Mining and quarrying (B)" in i:
            Mining.append(i)
        if "Manufacturing (C)" in i:
            Manufacturing.append(i)
        if "Electricity, gas, steam and air conditioning supply (D)" in i:
            Electricity.append(i)
        if "Water supply, sewerage, waste management and remediation activities (E)" in i:
            Water.append(i)
        if "Construction (F)" in i:
            Construction.append(i)
        if "Wholesale and retail trade, repair of motor vehicles and motorcycles (G)" in i:
            Wholesale.append(i)
        if "Transportation and storage (H)" in i:
            Transportation.append(i)
        if "Accommodation and food service activities (I)" in i:
            Accommodation.append(i)
        if "Information and communication (J)" in i:
            Information.append(i)
        if "Financial and insurance activities excluding activities of holding companies (K-642)" in i:
            Financial.append(i)
        if "Real estate activities (L)" in i:
            Realestate.append(i)
        if "Professional, scientific and technical activities (M)" in i:
            Professional.append(i)
        if "Administrative and support service activities (N)" in i:
            Administrative.append(i)
        if "Education (P)" in i:
            Education.append(i)
        if "Human Health and Social Work Activities (Q)" in i:
            Human.append(i)
        if "Arts, Entertainment and Recreation (R)" in i:
            Arts.append(i)
        if "Other Service Activities (S)" in i:
            Other.append(i)
        if "ICT total (261 to 264,268,465,582,61,62,631,951)" in i:
            ICT.append(i)
    print(Carlow)
    s = 0
    ## If there is a '..' in a number then this will be used to display missing values
    ## this was only needed at the beginning of the project to assertain the usefulness of the data
    for i in all_lists:
        f = 0
        for n in i:
            for t in n:
                if t == '..':
                    s +=1
                    f +=1
        i.append([f])
    keys = [
        "Business Active Enterprises",
        "Business Person Engaged", "Business Employees",
        "Mining Active Enterprises",
            "Mining Person Engaged","Mining Employees",
            "Manufacturing Active Enterprises",
    "Manufacturing Person Engaged",
            "Manufacturing Employees",
            "Electricity Active Enterprises",
    "Electricity Person Engaged",
    "Electricity Employees",
    "Water Active Enterprises",
    "Water Person Engaged",
    "Water Active Employees",
    "Construction Active Enterprises",
    "Construction Person Engaged",
    "Construction Employees",
    "Wholesale Active Enterprises",
    "Wholesale Person Engaged",
    "Wholesale Employees",
    "Transportation Active Enterprises",
    "Transportation Person Engaged",
    "Transportation Employees",
    "Accommodation Active Enterprises",
    "Accommodation Person Engaged",
    "Accommodation Employees",
    "Information Active Enterprises",
    "Information Person Engaged",
    "Information Employees",
    "Financial Active Enterprises",
    "Financial Person Engaged",
    "Financial Employees",
    "Real estate Active Enterprises",
    "Real estate Person Engaged",
    "Real estate Employees",
    "Professional Active Enterprises",
    "Professional Person Engaged",
    "Professional Employees",
    "Administrative Active Enterprises",
    "Administrative Person Engaged",
    "Administrative Employees",
    "Education Active Enterprises",
    "Education Person Engaged",
    "Education Active Employees",
    "Human Activities Active Enterprises",
    "Human Activities Person Engaged",
    "Human Activities Employees",
    "Arts Active Enterprises",
    "Arts Person Engaged",
    "Arts Active Employees",
    "Other Active Enterprises",
    "Other Person Engaged",
    "Other Active Employees",
    "ICT Active Enterprises",
    "ICT Person Engaged",
    "ICT Active Employees",
    "Missing"]
    dicti = {
        "Mining Active Enterprises" : '',
        "Mining Person Engaged": '',
        "Mining Employees": '',

        "Manufacturing Active Enterprises" : '',
        "Manufacturing Person Engaged": '',
        "Manufacturing Employees": '',

        "Electricity Active Enterprises" : '',
        "Electricity Person Engaged": '',
        "Electricity Employees": '',

        "Water Active Enterprises" : '',
        "Water Person Engaged": '',
        "Water Active Employees": '',

        "Construction Active Enterprises" : '',
        "Construction Person Engaged": '',
        "Construction Employees": '',

        "Wholesale Active Enterprises" : '',
        "Wholesale Person Engaged": '',
        "Wholesale Employees": '',

        "Transportation Active Enterprises" : '',
        "Transportation Person Engaged": '',
        "Transportation Employees": '',

        "Accommodation Active Enterprises" : '',
        "Accommodation Person Engaged": '',
        "Accommodation Employees": '',

        "Information Active Enterprises" : '',
        "Information Person Engaged": '',
        "Information Employees": '',

        "Financial Active Enterprises" : '',
        "Financial Person Engaged": '',
        "Financial Employees": '',

        "Real estate Active Enterprises" : '',
        "Real estate Person Engaged": '',
        "Real estate Employees": '',

        "Professional Active Enterprises" : '',
        "Professional Person Engaged": '',
        "Professional Employees": '',

        "Administrative Active Enterprises" : '',
        "Administrative Person Engaged": '',
        "Administrative Employees": '',

        "Education Active Enterprises" : '',
        "Education Person Engaged": '',
        "Education Active Employees": '',

        "Human Activities Active Enterprises" : '',
        "Human Activities Person Engaged": '',
        "Human Activities Employees": '',

        "Arts Active Enterprises" : '',
        "Arts Person Engaged": '',
        "Arts Active Employees": '',

        "Other Active Enterprises" : '',
        "Other Person Engaged": '',
        "Other Active Employees": '',

        "ICT Active Enterprises": '',
        "ICT Person Engaged": '',
        "ICT Active Employees": '',
        "Missing": ''

    }
    full_list =[]
    # this loopes through all the lists in all_lists
    for lists in all_lists:
        dicti = {
            "County": '',
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
            "ICT Active Employees": ''

        }
        a = 0
        ## loops through each sublist
        for sublist in lists:
            if len(sublist)> 1:
                ## if the sublist is greater than lenght 1 then the sublists point[1] is assigned to county
                dicti['County'] = str(sublist[1])
                if type(sublist) is not dict  :
                # provided the sublist is not a dict(this was a bug that had to be fixed, unknown reason)
                ## then the sublist of 2,3,4 are enterprise, persons engaged and employed of the appropriate
                # enterprise
                    dicti[str(keys[a])]= sublist[2]
                    dicti[str(keys[a+1])]= sublist[3]
                    dicti[str(keys[a+2])]= sublist[4]
                    a += 3
            else:
                dicti[str(keys[a])] = sublist[0]
        full_list.append(dicti)
    totals_list = []
    dicti2 = dicti
    for key,val in dicti2.items():
        dicti2[key] = 0
    print(dicti2)
    print(full_list)
    for i in full_list:
        a = 0
        for key, val in i.items():
            if val =='..':
                dicti2[key] +=1
            a +=1

    dicti2['County'] = 'Totals'

    full_list.append(dicti2)
## the data is saved to totals.csv
    keys = full_list[0].keys()
    with open('DataSets\\totals.csv', 'w+') as output_file:
        dict_writer = csv.DictWriter(output_file, keys,lineterminator = '\n')
        dict_writer.writeheader()
        dict_writer.writerows(full_list)

