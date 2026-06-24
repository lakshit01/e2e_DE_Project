from faker import Faker

import pandas as pd
import random

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique

from utils.exporter import Exporter

fake = Faker()

WAREHOUSE_CITIES = [

    "Delhi",

    "Mumbai",

    "Bangalore",

    "Hyderabad",

    "Chennai",

    "Pune",

    "Kolkata"

]

class WarehouseGenerator(BaseGenerator):

    def __init__(self, config):

        self.config = config

        self.df = None

    def generate(self):

        warehouses = []

        for warehouse_id in range(

            1,

            self.config["warehouses"] + 1

        ):

            city = random.choice(
                WAREHOUSE_CITIES
            )

            warehouses.append({

                "warehouse_id":
                    warehouse_id,

                "warehouse_name":
                    f"WH_{city}_{warehouse_id}",

                "city":
                    city

            })

        self.df = pd.DataFrame(
            warehouses
        )

    def validate(self):

        validate_unique(
            self.df,
            "warehouse_id"
        )

    def save(self):

        Exporter.export_csv(

            self.df,

            "outputs/warehouses.csv"
        )