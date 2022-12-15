from flask import Flask, render_template, redirect, request
import json
import folium
from datetime import timedelta


app = Flask(__name__)
app.debug = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=1)

def loadData():
    # load the data from json files
    with open("airports.json", "r") as f:
        # load the contents of the file as a dictionary
        airports = json.load(f)
    with open("routes.json", "r") as f:
        routes = json.load(f)       
    return routes,airports

# load two dictionary from json file
routes,airports = loadData()


@app.route('/')
def index():
    # response = "<h1>Welcome!</h1>"
    return render_template("index.html")

# methods used for airport Locs part
@app.route('/airportPos', methods=["POST"])
def redirect_to_map():  
    airportToCheck = request.form['airport']
    # Redirect the user to the specified URL
    return redirect('/map/'+airportToCheck)

@app.route('/map/<string:IATA>')
def mapAirports(IATA):
    # Create a map object
    # get the airports location
    loc = airports[IATA][:2]
    world_map = folium.Map(location=[0,0], zoom_start=2)
    print(loc)
    name = airports[IATA][-1]
    # Add the loc to the map using the Marker   
    folium.Marker(loc, popup=name).add_to(world_map)
    world_map.save("templates/map.html")
    response = render_template("map.html", map = world_map.get_root())
    # response = render_template("map.html")
    response = "<h2>The loction of "+IATA+" , (Entire Name:) "+ name +" is shown below:</h2>" + response
    # os.remove("templates/map.html")
    return response


# methods that used for near airports part
@app.route('/nearAirportPos', methods=["POST"])
def redirect_to_near():  
    airportToCheck = request.form['airport']
    # Redirect the user to the specified URL
    return redirect('/near/'+airportToCheck)

@app.route('/near/<string:IATA>')
def nearAirports(IATA):
    world_map = folium.Map(location=[0,0], zoom_start=2)
    #get the nearest airports' IATA
    nearP = routes[IATA]
    selfLoc = airports[IATA][:2]
    nearLocs = [airports[x] for x in nearP]

    for line in nearLocs:
        loc = line[:2]
        folium.Marker(loc, popup=line[-1]).add_to(world_map)
        line = [selfLoc , loc]
        folium.PolyLine(locations=line, color='red', weight=1.5, opacity=0.6).add_to(world_map)
    world_map.save("templates/near.html")
    response = render_template("near.html", map = world_map.get_root())
    return response


# methods that used for
@app.route('/route', methods = ['POST'])
def findRoute():
    world_map = folium.Map(location=[0,0], zoom_start=2)
    source = request.form['source']
    des = request.form['destination']
    # using the connect 'graph' doing the dfs thing
    # add a list to record the visited airport in case of looping
    def findPathBetween(graph, a, b):
        # maintain a queue of paths
        queue = []
        # push the first path into the queue
        queue.append([a])

        visitedNodes = {a}
        # used for record if the node is visited
        while queue:
            # get the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == b:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for adjacent in graph.get(node, []):
                if adjacent not in visitedNodes:
                    new_path = list(path)
                    new_path.append(adjacent)

                    queue.append(new_path)
            visitedNodes.update(graph.get(node, []))
    route = findPathBetween(routes,source,des)
    if not route:
        return render_template("opps.html")
    else:
        world_map = folium.Map(location=[0,0], zoom_start=2)
        for i,node in enumerate(route):
            if i >= len(route)-1:
                break
            else:
                loc = airports[node]
                #draw this airport's loc
                folium.Marker(loc[:2], popup=loc[-1]).add_to(world_map)
                #find next connected airport and draw a line
                nextN = route[i+1]
                nextNLoc = airports[nextN]
                line = [loc[:2],nextNLoc[:2]]
                folium.PolyLine(locations=line, color='red', weight=1.5, opacity=0.7).add_to(world_map)
        world_map.save("templates/route.html")
        # response = "<h2>The route from " + source + " to " + des +" shown in below map</h2>" +\
        #     render_template("route.html", map = world_map.get_root())
        response = render_template("routePath.html")
        for node in route:
            response += "<p>" + node + "</p>"
        return response

@app.route("/showRoute", methods = ['POST'])
def showRoute():
    return render_template("route.html")

if __name__ == "__main__":
    app.run()
