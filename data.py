import csv
import requests
import collections
import json
"""
    this py function runs as a result of saving a csv file as airports.csv, routes.csv
    and in order to cache, saved as json file
"""
# URL of the route data
url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"
urlP = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

# Get the data from the URL
response = requests.get(url)
responseP = requests.get(urlP)

# Write the data to a CSV file
csvfile =  open("routes.csv", "w", encoding="utf-8",newline="") 
writer = csv.writer(csvfile)
for line in response.text.splitlines():
    writer.writerow(line.split(",")[2:6])

csvfileP = open("airports.csv", "w", encoding="utf-8",newline="")
writer2 = csv.writer(csvfileP)
for line in responseP.text.splitlines():
    writer2.writerow(line.split(",")[4:8]+[line.split(",")[1]])

def cacheRoutesData():
    # cache the routes data from routes.csv
    sourceToDes = collections.defaultdict(list)
    with open("routes.csv","r") as f:
        reader = csv.reader(f)
        for line in reader:
            sourceToDes[line[0]].append(line[2])
    return sourceToDes

def cacheAirportsData():
    sourceToDes = collections.defaultdict()
    with open("airports.csv","r",encoding="utf-8") as f:
        reader = csv.reader(f)
        for line in reader:
            if len(line[0]) == 5:
                key = line[0].replace('"', '')
                sourceToDes[key] = (float(line[2]),float(line[3]),line[4])
    return sourceToDes

routes = cacheRoutesData()
airports = cacheAirportsData()
with open("routes.json", "w") as f:
    # write the contents of the dictionary to the file
    json.dump(routes, f)

with open("airports.json", "w") as f:
    json.dump(airports, f)


