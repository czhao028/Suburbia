from processdata import Suburbia
import csv
import pickle
"""
-Adds rentindex to each county
-
"""
with open("suburbia.pk", "rb") as pk:
    suburbia = pickle.load(pk)
    nested_dictionary = suburbia.nested_dictionary
    with open('C:\\Users\czhao\Downloads\data\\Zip_Zri_AllHomesPlusMultifamily_Summary.csv') as csvFile:
        #rent index
        csvReader = csv.reader(csvFile)
        for i,row in enumerate(csvReader):
            if i == 1:
                continue
            try:
                nested_dictionary[row[1]]["rindex"] = row[7]
            except:
                continue
    with open('C:\\Users\czhao\Downloads\data\\st24_md_cou.txt') as csvFile:



"""
TO DO:

-packages and API's used (Fannie Mae?)
-county to FPIS
-FPIS to zip codes
-add ethnicity & population (young, old, children) characteristics to dictionary
-compute score, rank top 5, spit out zip code

DONE rental price index for zip codes 
"""