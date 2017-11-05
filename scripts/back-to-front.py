from processdata import Suburbia
import csv
import pickle
"""
-Adds rentindex to each county
-county to zipcode
-adds percentages of <5, <18, and 65+ populations
"""
with open("suburbia.pk", "rb") as pk:
    suburbia = pickle.load(pk)
    nested_dictionary = suburbia.nested_dictionary
    # rent index
    with open('C:\\Users\czhao\Documents\Technica\data\\Zip_Zri_AllHomesPlusMultifamily_Summary.csv') as csvFile:
        csvReader = csv.reader(csvFile)
        for i,row in enumerate(csvReader):
            if i == 0:
                continue
            try:
                nested_dictionary[row[1]]["rindex"] = row[7]
            except:
                continue
    #county to zip code
    with open('C:\\Users\czhao\Documents\Technica\data\\all-geocodes-v2016.csv') as csvFile:
        county_to_fid = dict()
        lines = csvFile.read().splitlines()
        for i,line in enumerate(lines):
            if i < 5:
                continue
            l = line.split(",")
            id, county = l[2], l[6]
            county_to_fid[county] = id
    with open('C:\\Users\czhao\Documents\Technica\data\\COUNTY_ZIP_092017.csv') as csvFile1:
        csvReader = csv.reader(csvFile1)
        fid_to_zip = dict()
        for row in csvReader:
            try:
                fid_to_zip[row[0]].append(row[1])
            except:
                fid_to_zip[row[0]] = row[1]
    #county: list[of county ids]
    suburbia.county_to_zip = {county:fid_to_zip[fid] for county,fid in county_to_fid.items()}
    # adds kids, <18, seniors to Suburbia object
    ages = 'C:\\Users\czhao\Documents\Technica\data\\COUNTY_ZIP_092017.csv'
    with open(ages) as csvFile:
        csvReader = csv.reader(csvFile)
        for i, row in enumerate(csvReader):
            if i == 0:
                continue
            county,five,teen,senior = row[0], row[1], row[2], row[3]
            for zip in suburbia.county_to_zip[county]:
                suburbia.nested_dictionary[zip][five.__name__]  = five
                suburbia.nested_dictionary[zip][teen.__name__] = teen
                suburbia.nested_dictionary[zip][senior.__name__] = senior






"""
TO DO:

-packages and API's used (Fannie Mae?)
-county to FPIS
-FPIS to zip codes
-add ethnicity & population (young, old, children) characteristics to dictionary
-compute score, rank top 5, spit out zip code

DONE rental price index for zip codes 
"""