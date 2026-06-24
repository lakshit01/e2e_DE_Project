from faker import Faker
import pandas as pd
import random

fake = Faker()

def generate_driver_logs():

    records = []

    for _ in range(20000):

        hours_driven = random.randint(4,14)

        records.append({

            "driver_id":
                random.randint(1,1000),

            "date":
                fake.date(),

            "hours_driven":
                hours_driven,

            "distance_km":
                random.randint(50,800),

            "overworked":
                hours_driven > 10

        })

    df = pd.DataFrame(records)

    df.to_csv(

        "outputs/csv/driver_logs.csv",

        index=False

    )

    return df

def generate_warehouse_inventory():

    inventory = []

    for warehouse_id in range(1,51):

        inventory.append({

            "warehouse_id":
                warehouse_id,

            "inventory_count":
                random.randint(
                    1000,
                    100000
                ),

            "inventory_date":
                fake.date()

        })

    df = pd.DataFrame(
        inventory
    )

    df.to_csv(

        "outputs/csv/warehouse_inventory.csv",

        index=False

    )

import json

def generate_feedback():

    feedback = []

    ratings = [1,2,3,4,5]

    weights = [10,10,20,25,35]

    for _ in range(5000):

        feedback.append({

            "customer_id":
                random.randint(
                    1,
                    10000
                ),

            "shipment_id":
                random.randint(
                    1,
                    100000
                ),

            "rating":
                random.choices(
                    ratings,
                    weights
                )[0],

            "feedback":
                fake.sentence()

        })

    with open(

        "outputs/json/customer_feedback.json",

        "w"

    ) as file:

        json.dump(
            feedback,
            file,
            indent=4
        )


if __name__ == "__main__":

    generate_driver_logs()

    generate_warehouse_inventory()

    generate_feedback()