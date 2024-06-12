import os
import datetime
import json
import random
# from faker import Faker

import requests
import xml.etree.ElementTree as ET
from tqdm import tqdm

# Plotting
# import plotly.express as px


def get_route_between_locations(filepath, source: tuple, dest: tuple, tracked_object: str, date_and_time: datetime):

	date_and_time.replace(minute=0, second=0, microsecond=0)

	if tracked_object != "plane_container":
		start = "{},{}".format(source[0], source[1])
		end = "{},{}".format(dest[0], dest[1])
		# Service - 'route', mode of transportation - 'driving', without alternatives
		url = 'http://router.project-osrm.org/route/v1/driving/{};{}?alternatives=false&annotations=nodes'.format(start, end)

		headers = {'Content-type': 'application/json'}
		r = requests.get(url, headers=headers)
		print("Calling API ...:", r.status_code)  # Status Code 200 is success

		routejson = r.json()
		route_nodes = routejson['routes'][0]['legs'][0]['annotation']['nodes']

		### keeping every third element in the node list to optimize time
		route_list = []
		for i in range(0, len(route_nodes)):
			# get every 300. point of 0.1 miles distance = 30 miles distance
			if i % 60 == 1:
				route_list.append(route_nodes[i])

		coordinates = []

		# length_of_data = len(route_list)
		# first_border = int(length_of_data / 3)
		# second_border = first_border * 2
		# counter = 1

		for node in tqdm(route_list):
			try:
				url = 'https://api.openstreetmap.org/api/0.6/node/' + str(node)
				r = requests.get(url, headers=headers)
				myroot = ET.fromstring(r.text)
				for child in myroot:
					lat, long = child.attrib['lat'], child.attrib['lon']

				# if counter < first_border:
				# tracked_object = "boat"
				# if first_border <= counter <= second_border:
				# 	tracked_object = "truck"
				# elif counter > second_border:
				# 	tracked_object = "plane_container"

				save_data_as_json(filepath, lat, long, date_and_time, tracked_object)
				coordinates.append((lat, long))
				date_and_time += datetime.timedelta(minutes=60)
				# counter += 1

			except:
				continue
		# print(coordinates[:10])
		return date_and_time

	date_and_time += datetime.timedelta(hours=3)
	save_data_as_json(filepath=filepath, lat=dest[1], long=dest[0], date_and_time=date_and_time, tracked_object=tracked_object)
	return date_and_time


def setup_structure(filename: str = "tracking_data.json"):
	dir_filepath = "data/tracking/"
	create_dirs(dir_filepath)

	filepath = dir_filepath + filename

	return filepath


def create_dirs(parent_dir):
	try:
		os.makedirs(parent_dir)
	except FileExistsError:
		pass
	return None


def save_data_as_json(filepath: str, lat, long, date_and_time, tracked_object):
	result_dict = dict()

	# lat = random.uniform(-90.00, 90.00)
	# long = random.uniform(-180.00, 180.00)

	timestamp = date_and_time.isoformat()

	result_dict["timestamp"] = timestamp
	result_dict["lat"] = lat
	result_dict["long"] = long
	result_dict["tracked_object"] = tracked_object

	print(f"Datetime: {timestamp}, Latitude: {lat}, Longitude: {long}, Longitude: {long}, Target: {tracked_object}")

	if os.path.isfile(filepath):

		json_file = open(filepath)
		geo_log = json.load(json_file)
		geo_log.append(result_dict)

		with open(filepath, 'r+') as file:
			json.dump(geo_log, file, sort_keys=True)
			print(f"Updated '{filepath}' with dumped data")

	else:
		with open(filepath, 'w') as file:
			geo_log = [result_dict]
			json.dump(geo_log, file, sort_keys=True)
			print(f"Created '{filepath}' with dumped data")

	return None


# Lat, Long
# -0.56328107, 33.04421661
# Long, Lat
source = (33.04421661, -0.56328107)  # Victoria Lake
# Lat, Long
# 50.88360814831935, 4.3575478300498744
# Long, Lat
dest = (4.35754783, 50.88360814)  # Brussels

route_dict = {
	"route_1": {
		"source": (33.04421661, -0.56328107),
		"dest": (32.56389848, 0.32974216),
		"target_object": "boat"
	},
	"route_2": {
		"source": (32.56389848, 0.32974216),
		"dest": (32.44064755, 0.06019266),
		"target_object": "truck"
	},
	"route_3": {
		"source": (32.44064755, 0.06019266),
		"dest": (25.256819319427102, 55.36431779410911),
		"target_object": "plane_container"
	},
	"route_4": {
		"source": (25.256819319427102, 55.36431779410911),
		"dest": (4.483329753377929, 50.898982303185264),
		"target_object": "plane_container"
	},
}

destinations = {
	"victoria_lake": (33.04421661, -0.56328107),
	"kampala_factory": (32.56389848, 0.32974216),
	"kampala_airport": (32.44064755, 0.06019266),
	"dubai_airport": (25.256819319427102, 55.36431779410911),
	"brussels_airport": (4.483329753377929, 50.898982303185264)
}


json_filepath = setup_structure("mocked_tracking_data.json")
date_and_time = datetime.datetime.now()
for key, value in route_dict.items():
	source = value["source"]
	dest = value["dest"]
	target_object = value["target_object"]

	date_and_time = get_route_between_locations(json_filepath, source, dest, target_object, date_and_time)

