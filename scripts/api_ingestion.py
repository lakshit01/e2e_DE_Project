import requests
import json
import boto3
from datetime import datetime

s3 = boto3.client("s3")

gps = requests.get(
    "http://localhost:5001/gps"
).json()

s3.put_object(

   Bucket="logistics-dev-raw",

   Key=
   f"apis/gps/{datetime.now()}.json",

   Body=json.dumps(gps)

)

fuel = requests.get(
    "http://localhost:5002/fuel"
).json()

s3.put_object(

   Bucket="logistics-dev-raw",

   Key=
   f"apis/fuel/{datetime.now()}.json",

   Body=json.dumps(fuel)

)

weather = requests.get(
    "http://localhost:5003/weather"
).json()

s3.put_object(

   Bucket="logistics-dev-raw",

   Key=
   f"apis/weather/{datetime.now()}.json",

   Body=json.dumps(weather)


)