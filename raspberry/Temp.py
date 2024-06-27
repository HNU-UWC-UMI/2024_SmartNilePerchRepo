import http.client
from urllib.parse import quote
import time
import board
import adafruit_dht
from datetime import datetime
import uuid

# Sensor data pin is connected to GPIO 4
sensor = adafruit_dht.DHT22(board.D4)
# Uncomment for DHT11
# sensor = adafruit_dht.DHT11(board.D4)

# timestamp_interval = 900 # 5 minutes in seconds
timestamp_interval = 2  # 2 seconds for testing
last_timestamp_time = time.time()
temp_range = (-5, 3)

#iDent = "4"
tempId = ""
inRange = ""

def generate_uuid():
    return str(uuid.uuid4())



while True:
    try:
        temp = sensor.temperature
        current_time = time.time()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tempId = generate_uuid()

        alert = ""
        if temp < temp_range[0] or temp > temp_range[1]:
            alert = f"Alert: Temperature {temp}°C outside the desired range of {temp_range[0]}°C to {temp_range[1]}°C"
            inRange = "1"
        else:
            inRange = "0"

        if current_time - last_timestamp_time >= timestamp_interval:
            last_timestamp_time = current_time
            print(f"Timestamp: {timestamp}, Temp={temp:.2f}°C, Alert={alert}")

            #encoded_iDent = quote(iDent)
            encoded_tempId = quote(tempId)
            encoded_temp = quote(str(temp))
            encoded_inRange = quote(inRange)
            encoded_timeStamps = quote(timestamp)
            print(encoded_temp)
            conn = http.client.HTTPSConnection("apex.oracle.com")
            api_url = f"https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/TEMPERATURE_DATA?iDent=1&tempId={encoded_tempId}&temp={encoded_temp}&inRange={encoded_inRange}&timeStamps={encoded_timeStamps}"

            conn.request("POST", api_url)

            res = conn.getresponse()
            data = res.read()

            if res.status == 200:
                print("Connection successful!")
            else:
                print(f"Connection failed. Status code: {res.status}")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error

    time.sleep(3)
