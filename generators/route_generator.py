import pandas as pd

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique

from utils.exporter import Exporter

import random

CITIES = [

    "Delhi",

    "Mumbai",

    "Bangalore",

    "Chennai",

    "Hyderabad",

    "Pune",

    "Kolkata",

    "Ahmedabad"

]

class RouteGenerator(BaseGenerator):

    def __init__(self, config):

        self.config = config

        self.df = None

    def generate(self):

        routes = []

        for route_id in range(

            1,

            self.config["routes"] + 1

        ):

            source_city = random.choice(
                CITIES
            )

            destination_city = random.choice(
                [
                    c for c in CITIES
                    if c != source_city
                ]
            )

            distance_km = random.randint(
                50,
                2500
            )

            expected_delivery_hours = round(

                distance_km / 45,

                2

            )

            routes.append({

                "route_id":
                    route_id,

                "source_city":
                    source_city,

                "destination_city":
                    destination_city,

                "distance_km":
                    distance_km,

                "expected_delivery_hours":
                    expected_delivery_hours

            })

        self.df = pd.DataFrame(
            routes
        )


    def validate(self):

        validate_unique(
            self.df,
            "route_id"
        )

    def save(self):

        Exporter.export_csv(

            self.df,

            "outputs/routes.csv"

        )
        