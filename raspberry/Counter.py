import time
import RPi.GPIO as GPIO
import json
import http.client
from urllib.parse import quote
# Set the gain to ±4.096V (adjust if needed)




# Define the GPIO pin for the push button
BUTTON_PIN = 17 # GPIO17
red_pin = 27
green_pin = 22
yellow_pin = 25
infrared = 23
# Initialize the GPIO pin for the button

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(infrared,GPIO.IN)
prev_button = "off"
count = 0
container_id= 1
size = "medium"
prev_sensor = 1
while True:
	while prev_button == "off":
		button_state = GPIO.input(BUTTON_PIN)
		GPIO.output(red_pin,GPIO.HIGH)
		GPIO.output(green_pin,GPIO.LOW)
		if button_state == GPIO.LOW:
		
			if prev_button == "on":
				
				prev_button = "off"
			else:
				prev_button = "on"
			print(prev_button)
			time.sleep(0.1)
	while prev_button == "on":
		button_state = GPIO.input(BUTTON_PIN)
		GPIO.output(green_pin,GPIO.HIGH)
		GPIO.output(red_pin,GPIO.LOW)
		GPIO.output(yellow_pin, GPIO.LOW)
		sensor= GPIO.input(infrared)
		if count >= 10:
				GPIO.output(yellow_pin, GPIO.HIGH)
				time.sleep(0.2)
				GPIO.output(yellow_pin, GPIO.LOW)
		
	
		if sensor == 0 and prev_sensor==1:
			count +=1
			dictionary = {
			"container_id": container_id, 
				"fish_id": count,
				"size": size,
			}		
			
			json_object = json.dumps(dictionary, indent=4)
			print(dictionary)
			encoded_container_id = quote(str(container_id))
			encoded_count = quote(str(count))
			encoded_size = quote(str(size))
			conn = http.client.HTTPSConnection("apex.oracle.com")
			api_url = f"https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/FISHCOUNTER_DATA?identCounter=1&fishCounterId={encoded_count}&containerId={encoded_container_id}&fishCounterSize={encoded_size}"
			print(api_url)
			conn.request("POST", api_url)

			res = conn.getresponse()
			data = res.read()

			if res.status == 200:
				print("Connection successful!")
			else:
				print(f"Connection failed. Status code: {res.status}")
		   
			
			time.sleep(0.1)
		prev_sensor = sensor
		if button_state == GPIO.LOW:
		
			if prev_button == "on":
				
				prev_button = "off"
			else:
				prev_button = "on"
			print(prev_button)
			time.sleep(0.1)	
		







