import folium

# Create a map object
m = folium.Map()

# Define a list of latitude and longitude coordinates for the route
route = [[45.5236, -122.6750], [37.7749, -122.4194], [40.7128, -74.0060]]

# Add the route to the map using the PolyLine method
folium.PolyLine(locations=route, color='red', weight=2.5, opacity=1).add_to(m)

# Save the map to an HTML file
m.save('map.html')
