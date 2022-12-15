My project has not used an API key because the data I got from need not, it is entirely open
access to the data: https://openflights.org/data.html

required python package:

flask (web framework)
json   (cache and load the json file)
folium (help with the map)
requests  (crawl from the website)
csv  (middle store the data)
collections (used the defualt dictionary)

running instructions:
First run the data.py file alone, this will generate two json file for later use
this process it will get the requests from two website:

    1. https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat
    processed and stored it into airports.json file:
    IATA	str, 3-letter IATA code to stand an unique airport
    (example as: WWK, EWR...)
    Latitude	float, usually to six significant digits. Negative is South, positive is North.
    Longitude	float, usually to six significant digits. Negative is West, positive is East.
    name    str, name of the airport

    about 7000 records


    2. https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat
    processed and stored it into routes.json file:
    Source  str, 3-letter IATA code to stand an unique airport
    Des     list, contain destination airports around the source airport stored a into list

(if you directly download those two json files you could skip the first step)
Second, run the final.py file. This will result give a weblink as:
http://127.0.0.1:5000/ this is the index page of the web app

About the data structure:
The airports.json file is just like dictionary
The routes.json file is like connected graph, every node stored a str (3-letter IATA code to stand an unique airport. 
example: dict = {
    'airportA' : [airportA,airportB,airportC],
    'airportB' : [airportA,airportD,airportE],
    ...
}

Inside the page you will see three options:
    1. Search airport on the map:
    you could enter an IATA code that stands for an airport, then click the button
    a map will be shown, the location of the airport marked on map

    2. Find the nearby airports within 1 flight
    you could enter an IATA code that stands for an airport, then click the button
    a map will be shown, the location of the airport marked on map, and all the airports
    within 1 flight will be marked and linked with the airport you input

    3. Find the route from airport A to B
    you could enter two IATA codes that stands for two airport, then click the button
    a map will be shown, a linked route of A B airports will be shown