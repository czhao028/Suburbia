from urllib.request import Request, urlopen
from bs4 import *
import pickle
import xml.etree.ElementTree as ET
import requests
from collections import *
"""
This file takes all the Zillow HomeValueIndex (cost of house) to 
"""
#request = Request('http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g3f9kwkqvf_55f1z&state=md&childtype=zipcode')
response = requests.get('http://www.zillow.com/webservice/GetRegionChildren.htm?zws-id=X1-ZWz1g3f9kwkqvf_55f1z&state=md&childtype=zipcode')
soup = BeautifulSoup(response.content, ['lxml', 'xml'])
f = open('pretty_xml.xml', 'w')
f.writelines(soup.prettify())
f.close()

d = defaultdict(dict)
a = soup.find_all("region")
for tag in a:
    if("zindex" in str(tag)):
        d[tag.id.text]["zindex"] = tag.zindex.text

print(sorted(d))
with open("new.pickle", "wb") as f:
    pickle.dump(d, f)


# f = open('request.xml', 'w')
# f.write(urlopen(request))
# tree = ET.fromstring(response.content)
# print(tree)
# #soup = BeautifulSoup(response, "lxml")
# #pickle.dump(soup, open('j.pickle', 'wb'))
# for e in tree:
#     print(e.tag, e.attribute)

