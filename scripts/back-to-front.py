from processdata import Suburbia
import csv
import pickle
"""
-Adds rentindex to each county
-county to zipcode
"""
with open("suburbia.pk", "rb") as pk:
    suburbia = pickle.load(pk)
    nested_dictionary = suburbia.nested_dictionary
    # rent index
    with open('C:\\Users\czhao\Downloads\data\\Zip_Zri_AllHomesPlusMultifamily_Summary.csv') as csvFile:
        csvReader = csv.reader(csvFile)
        for i,row in enumerate(csvReader):
            if i == 1:
                continue
            try:
                nested_dictionary[row[1]]["rindex"] = row[7]
            except:
                continue
    #county to zip code
    with open('C:\\Users\czhao\Downloads\data\\st24_md_cou.txt') as csvFile:
        county_to_fid = dict()
        lines = csvFile.read().splitlines()
        for line in lines:
            l = line.split(",")
            id, county = l[2], l[3]
            county_to_fid[county] = id
    with open('C:\\Users\czhao\Downloads\data\\COUNTY_ZIP_092017.csv') as csvFile1:
        csvReader = csv.reader(csvFile1)
        fid_to_zip = dict()
        for row in csvReader:
            try:
                fid_to_zip[row[0]].append(row[1])
            except:
                fid_to_zip[row[0]] = row[1]
    suburbia.county_to_zip = {key:fid_to_zip[county_to_fid[key]] for key,val in county_to_fid}



"""
TO DO:

-packages and API's used (Fannie Mae?)
-county to FPIS
-FPIS to zip codes
-add ethnicity & population (young, old, children) characteristics to dictionary
-compute score, rank top 5, spit out zip code

DONE rental price index for zip codes 
"""