import os
import datetime
import json
import random


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


def save_data_as_json(filepath):
	result_dict = dict()
	# lat, long = parse_gps()
	lat = random.uniform(-90.00, 90.00)
	long = random.uniform(-180.00, 180.00)

	ts_value = datetime.datetime.now().isoformat()

	result_dict["ts_value"] = ts_value
	result_dict["lat"] = lat
	result_dict["long"] = long

	if os.path.isfile(filepath):

		json_file = open(filepath)
		geo_log = json.load(json_file)
		geo_log.append(result_dict)

		with open(filepath, 'r+') as file:
			json.dump(geo_log, file, sort_keys=True)
			print(f"{filepath} Updated json with dumped data")

	else:
		with open(filepath, 'w') as file:
			geo_log = [result_dict]
			json.dump(geo_log, file, sort_keys=True)
			print(f"{filepath} Created json with dumped data")

	return None


json_filepath = setup_structure()
save_data_as_json(json_filepath)


