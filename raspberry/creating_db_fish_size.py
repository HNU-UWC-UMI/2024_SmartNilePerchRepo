import http.client
from urllib.parse import quote
import time

from datetime import datetime
import uuid

# timestamp_interval = 900 # 5 minutes in seconds


fishID = 2
fishWeight = 1000
fishSize = "small-medium"
LocalExport = 0

# encoded_iDent = quote(iDent)
encoded_fishId = quote(str(fishID))
encoded_temp = quote(str(fishWeight))
encoded_inRange = quote(fishSize)
encoded_timeStamps = quote(str(LocalExport))
print(encoded_temp)
conn = http.client.HTTPSConnection("apex.oracle.com")
api_url = f"https://apex.oracle.com/pls/apex/hackathonjune2024/NilePProject/FISHDESC_DATA?identFish=1&fishID={encoded_fishId}&fishWeight={encoded_temp}&fishSize={encoded_inRange}&LocalExport={encoded_timeStamps}"

conn.request("POST", api_url)

res = conn.getresponse()
data = res.read()

if res.status == 200:
    print("Connection successful!")
else:
    print(f"Connection failed. Status code: {res.status}")
