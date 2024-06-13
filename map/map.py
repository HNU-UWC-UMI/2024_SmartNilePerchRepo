import json
import folium
from folium.plugins import MarkerCluster
import pandas as pd
import webbrowser

json_file = "geodata_mocking.json"


def get_request():
    # implement request and store response as json
    pass


def get_geolocation(param: str):
    # parse json with open and give it an argument
    pass


def set_up_map():
    # Ulm
    # latitude + longitude
    country_overview = [48.39841000, 9.99155000]
    # initial creation of the map
    return folium.Map(location=country_overview, zoom_start=13)


def set_markers(map):
    # implement json
    with open(json_file) as jason_data:
        data = json.loads(jason_data)

    print(data)
    """
    for mark in markers:
        folium.Marker(mark, popup="CU Boulder").add_to(map)

    return map
    """


overview = set_up_map()
map = set_up_map(overview)

# Display the map
map.save("test.html")
webbrowser.open("test.html")
