import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

# Ulm
# latitude + longitude
location = [48.39841000, 9.99155000]

my_map = folium.Map(location=location, zoom_start=13)

# Display the map
my_map.save("test.html")
webbrowser.open("test.html")
