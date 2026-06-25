import boto3
import os

s3 = boto3.client("s3")

bucket = "logistics-dev-raw"

for file in os.listdir("outputs/csv"):

    s3.upload_file(

        f"outputs/csv/{file}",

        bucket,

        f"files/{file}"

    )

    print(file)


for file in os.listdir("outputs/json"):

    s3.upload_file(

        f"outputs/json/{file}",

        bucket,

        f"files/{file}"

    )
    print(file)