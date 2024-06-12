import os
import datetime
import json
import time
import requests
import xml.etree.ElementTree as ET
from tqdm import tqdm


def get_route_between_locations(filepath, route_source: tuple, route_dest: tuple, tracked_object: str, route_datetime: datetime):

	if tracked_object == "truck":
		start = "{},{}".format(route_source[0], route_source[1])
		end = "{},{}".format(route_dest[0], route_dest[1])
		# Service - 'route', mode of transportation - 'driving', without alternatives
		url = 'http://router.project-osrm.org/route/v1/driving/{};{}?alternatives=false&annotations=nodes'.format(start, end)

		headers = {'Content-type': 'application/json'}
		r = requests.get(url, headers=headers)
		print("Calling API ...:", r.status_code)  # Status Code 200 is success
		time.sleep(0.5)

		routejson = r.json()
		route_nodes = routejson['routes'][0]['legs'][0]['annotation']['nodes']

		route_list = []
		for i in range(0, len(route_nodes)):
			# keep every nth-point of 0.1 miles distance = n miles distance
			if i % 60 == 1:
				route_list.append(route_nodes[i])

		coordinates = []

		for node in tqdm(route_list):
			try:
				url = 'https://api.openstreetmap.org/api/0.6/node/' + str(node)
				r = requests.get(url, headers=headers)
				myroot = ET.fromstring(r.text)
				for child in myroot:
					lat, long = child.attrib['lat'], child.attrib['lon']

				save_data_as_json(filepath, lat, long, route_datetime, tracked_object)
				coordinates.append((lat, long))
				route_datetime += datetime.timedelta(minutes=60)

			except:
				continue

	elif tracked_object == "boat":
		route_datetime += datetime.timedelta(hours=2)
		save_data_as_json(filepath=filepath, lat=route_source[1], long=route_source[0], datetime_value=route_datetime, tracked_object=tracked_object)

	else:  # plane
		route_datetime += datetime.timedelta(hours=3)
		save_data_as_json(filepath=filepath, lat=route_dest[1], long=route_dest[0], datetime_value=route_datetime, tracked_object=tracked_object)

	return route_datetime


def setup_structure(filename: str = "tracking_data.json", init: bool = False):
	dir_filepath = "data/"

	if init:
		create_dirs(dir_filepath)

	filepath = dir_filepath + filename

	return filepath


def create_dirs(parent_dir):
	try:
		os.makedirs(parent_dir)
	except FileExistsError:
		pass
	return None


def save_data_as_json(filepath: str, lat, long, datetime_value, tracked_object):
	result_dict = dict()

	timestamp = datetime_value.isoformat()

	result_dict["timestamp"] = timestamp
	result_dict["lat"] = lat
	result_dict["long"] = long
	result_dict["tracked_object"] = tracked_object

	# print(f"Datetime: {timestamp}, Latitude: {lat}, Longitude: {long}, Longitude: {long}, Target: {tracked_object}")

	if os.path.isfile(filepath):

		json_file = open(filepath)
		geo_log = json.load(json_file)
		geo_log.append(result_dict)

		with open(filepath, 'r+') as file:
			json.dump(geo_log, file, sort_keys=True)
			# print(f"Updated '{filepath}' with dumped data")

	else:
		with open(filepath, 'w') as file:
			geo_log = [result_dict]
			json.dump(geo_log, file, sort_keys=True)
			print(f"Created '{filepath}' with dumped data")

	return None


# (Long, Lat)
route_dict = {
	"route_1": {
		"source": (33.04421661, -0.56328107),  # - victoria lake
		"dest": (32.80135216, 0.15211125),  # - victoria lake coast
		"target_object": "boat"
	},
	"route_2": {
		"source": (32.80135216, 0.15211125),  # - victoria lake coast
		"dest": (32.56389848, 0.32974216),  # - kampala factory
		"target_object": "truck"
	},
	"route_3": {
		"source": (32.56389848, 0.32974216),   # - kampala factory
		"dest": (32.44064755, 0.06019266),  # - kampala airport
		"target_object": "truck"
	},
	"route_4": {
		"source": (32.44064755, 0.06019266),  # - kampala airport
		"dest": (55.36431779410911, 25.256819319427102),  # - dubai airport
		"target_object": "plane"
	},
	"route_5": {
		"source": (55.36431779410911, 25.256819319427102),  # - dubai airport
		"dest": (4.483329753377929, 50.898982303185264),  # - brussels airport
		"target_object": "plane"
	}
}

date_and_time = datetime.datetime.now()
datetime_for_name = date_and_time.strftime("%Y%m%d_%H%M%S")
date_and_time.replace(minute=0, second=0, microsecond=0)

json_filepath = setup_structure(f"{datetime_for_name}_tracking_data.json")

for key, value in route_dict.items():
	source = value["source"]
	dest = value["dest"]
	target_object = value["target_object"]

	date_and_time = get_route_between_locations(json_filepath, source, dest, target_object, date_and_time)

print("Finished process successfully")

