import folium

# Create a map object
m = folium.Map()

# Define a list of latitude and longitude coordinates for the route
route = [[45.5236, -122.6750], [37.7749, -122.4194], [40.7128, -74.0060]]

# Add the route to the map using the PolyLine method
line = folium.PolyLine(locations=route, color='red', weight=2.5, opacity=1)
line.add_to(m)

# Add a node at the end of each line
for coord in route:
    # Add the node to the map
    node = folium.CircleMarker(location=coord, radius=6, color='#6d0000', fill_color='#6d0000')
    node.add_to(m)

    # Add the name to the node
    folium.Popup("airport 1", parse_html=True).add_to(node)

# Save the map to an HTML file
m.save('map.html')
