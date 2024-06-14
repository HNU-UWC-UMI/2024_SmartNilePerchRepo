import http.client
import pandas as pd
import json
import folium
from folium.plugins import MarkerCluster


def database_respone_to_dataframe():
    host = 'apex.oracle.com'
    endpoint = '/pls/apex/hackathonjune2024/NilePProject/GpsData'  
    
    try:
        conn = http.client.HTTPSConnection(host, timeout=10)
        conn.request("GET", endpoint)
        response = conn.getresponse()
        if response.status == 200:
            data = response.read().decode()
            data = json.loads(data)
            return pd.json_normalize(data['items'])
        
    
        else:
            print(f"Error on GET Request: {response.status}, {response.reason}")
        conn.close()
        
    except (ConnectionError, TimeoutError) as e:
        print(f"Error on establishing connection to database: {e}")


df = database_respone_to_dataframe()


def create_line_color(param: str):
    if param == "boat":
        print("boat")
        # return "#0000ff"
        return "blue"
    if param == "plane":
        print("plane")
        # return "#008000"
        return "green"
    if param == "truck":
        print("truck")
        return "#ff0000"
    if param == "phone":
        return "yellow"


fg = folium.FeatureGroup("Lines") # use to plot lines from coordinates on the map


def create_geolocation(df):
    coords_all = df[["latitude", "longitude"]]
    coords_start = [df.loc[0, "latitude"], df.loc[0, "longitude"]]
    time_start = df.loc[0, "timestamp"]
    coord_last = [df.loc[(len(df) - 1), "latitude"], df.loc[(len(df) - 1), "longitude"]]
    time_last = df.loc[(len(df) - 1), "timestamp"]
    vehicle_last = df.loc[(len(df) - 1), "targetobj"]
        
    basemap = folium.Map(location = coord_last, zoom_start = 13)
    folium.PolyLine(coords_all).add_to(basemap)
    fg.add_to(basemap)
    folium.LayerControl(position='bottomright').add_to(basemap)

    folium.Marker(coords_start,
                  popup = f'Started at: {time_start}',
                  icon=folium.Icon(color='blue')).add_to(basemap)
    folium.Marker(coord_last,
                  popup = f'Last Seen at: {time_last}\nVehicle: {vehicle_last}',
                  icon=folium.Icon(color='red')).add_to(basemap)

    basemap.save("map.html")


create_geolocation(df_mocked_sorted)