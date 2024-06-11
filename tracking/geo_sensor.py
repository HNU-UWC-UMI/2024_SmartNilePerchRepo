import serial
import pynmea2
from geo_data import save_data_as_json, setup_structure


def parse_gps(io_port):
	if io_port.find('GGA') > 0:
		msg = pynmea2.parse(io_port)
		print("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude:%s %s" % (msg.timestamp, msg.lat, msg.lat_dir, msg.lon, msg.lon_dir, msg.altitude, msg.altitude_units))

		return msg.lat, msg.lon


serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
json_filepath = setup_structure()
while True:
	serial_port = serialPort.readline()
	lat, long = parse_gps(serial_port)
	save_data_as_json(json_filepath, lat, long)

