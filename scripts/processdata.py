import csv
import pickle
import json
import requests
from numpy import random
"""
This file takes care of reading urban areas/urban clusters and their respective UACE (Census Code for a zip code)
Transfers UACE to zip code and adds urban/suburban/rural classifiers to each zip code
Adds transit info to "transportation" key in nested dict
"""
class Suburbia:
    def __init__(self):
        self.nested_dictionary = pickle.load(open('new.pickle', 'rb'))
        self.ua_to_zip = dict()
    def read_transfer(self):
        with open("zip.csv") as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                self.ua_to_zip[row[0]] = row[2]
    def read_urban(self):
        urban = 'C:\\Users\czhao\Downloads\data\\ua_list_ua.csv'
        urb_cluster = 'C:\\Users\czhao\Downloads\data\\ua_list_uc.csv'
        with open(urban) as csv1:
            csvReader = csv.reader(csv1)
            for row in csvReader:
                try:
                    self.nested_dictionary[self.ua_to_zip[row[0]]]["urban?"] = "urban"
                except:
                    continue
        with open(urb_cluster) as csv2:
            csvReader = csv.reader(csv2)
            for row in csvReader:
                try:
                    self.nested_dictionary[self.ua_to_zip[row[0]]]["urban?"] = "suburban"
                except:
                    continue
        for key,dict in self.nested_dictionary.items():
            try:
                t = self.nested_dictionary[key]["urban?"]
            except:
                self.nested_dictionary[key]["urban?"] = "rural"
        csv1.close()
        csv2.close()
    def read_transit(self):
        stops = 'C:\\Users\czhao\Downloads\google_transit\stops.txt'
        s = open(stops,"r")
        count = 0
        arr = s.read().splitlines()
        for line in random.choice(arr, 500):
            if count == 0:
                count+=1
                continue
            l = line.split(",")
            lat, lng = l[4], l[5]
            print(lat,lng)
            request = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+lat+","+lng+"&key=AIzaSyDabeDf_8wl6qq9jV8CO-vRxPtr_m0b0ik")
            json_data = json.loads(request.text)
            zip = json_data["results"][0]['address_components'][-1]["long_name"]
            name = l[2]
            try:
                self.nested_dictionary[zip]["transportation"].append(name)
            except:
                self.nested_dictionary[zip]["transportation"] = [name]
        s.close()

        #https://maps.googleapis.com/maps/api/geocode/json?latlng=39.350945,-76.660393&key=AIzaSyBfTI7D3XHGHH2aFm6Ncgk7kKO-HBhdSNg

if __name__ == "__main__":
    S = Suburbia()
    S.read_transfer()
    S.read_urban()
    S.read_transit()
    print(S.nested_dictionary)
    with open("suburbia.pk", "wb") as pk:
        pickle.dump(S, pk)


