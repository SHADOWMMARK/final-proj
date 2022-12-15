import json
def loadData():
    # load the data from json files
    with open("airports.json", "r") as f:
        # load the contents of the file as a dictionary
        airports = json.load(f)
    with open("routes.json", "r") as f:
        routes = json.load(f)       
    return routes,airports
