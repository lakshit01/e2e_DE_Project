import random
import pandas as pd

from faker import Faker
from datetime import timedelta

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique

from utils.exporter import Exporter

fake = Faker()


class ShipmentGenerator(BaseGenerator):

    def __init__(self, config):

        self.config = config

        self.df = None

    def generate(self):

        shipments = []

        # Load routes dimension
        routes_df = pd.read_csv(
            "outputs/routes.csv"
        )

        # 10% risky drivers
        risky_drivers = random.sample(
            range(
                1,
                self.config["drivers"] + 1
            ),
            int(
                self.config["drivers"] * 0.10
            )
        )

        for shipment_id in range(
            1,
            self.config["shipments"] + 1
        ):

            customer_id = random.randint(
                1,
                self.config["customers"]
            )

            driver_id = random.randint(
                1,
                self.config["drivers"]
            )

            vehicle_id = random.randint(
                1,
                self.config["vehicles"]
            )

            warehouse_id = random.randint(
                1,
                self.config["warehouses"]
            )

            # Random Route Selection
            route = routes_df.sample(
                n=1
            ).iloc[0]

            route_id = int(
                route["route_id"]
            )

            distance_km = int(
                route["distance_km"]
            )

            expected_delivery_hours = float(
                route[
                    "expected_delivery_hours"
                ]
            )

            # Shipment Status Distribution
            shipment_status = random.choices(
                [
                    "Delivered",
                    "Delayed",
                    "In Transit"
                ],
                weights=[
                    80,
                    10,
                    10
                ]
            )[0]

            # Risky Drivers Cause More Delays
            if driver_id in risky_drivers:

                if random.randint(
                    1,
                    100
                ) <= 30:

                    shipment_status = "Delayed"

            # Actual Delivery Hours

            if shipment_status == "Delivered":

                actual_delivery_hours = round(

                    expected_delivery_hours +

                    random.uniform(
                        -2,
                        5
                    ),

                    2
                )

            elif shipment_status == "Delayed":

                actual_delivery_hours = round(

                    expected_delivery_hours +

                    random.uniform(
                        10,
                        30
                    ),

                    2
                )

            else:

                actual_delivery_hours = None

            # Pickup Time

            pickup_time = fake.date_time_between(

                start_date="-365d",

                end_date="now"

            )

            # Delivery Time

            if shipment_status == "In Transit":

                delivery_time = None

            else:

                delivery_time = (

                    pickup_time +

                    timedelta(
                        hours=
                        actual_delivery_hours
                    )

                )

            # Shipment Cost

            shipment_cost = round(

                distance_km *

                random.uniform(
                    5,
                    15
                ),

                2
            )

            shipments.append({

                "shipment_id":
                    shipment_id,

                "customer_id":
                    customer_id,

                "driver_id":
                    driver_id,

                "vehicle_id":
                    vehicle_id,

                "warehouse_id":
                    warehouse_id,

                "route_id":
                    route_id,

                "distance_km":
                    distance_km,

                "expected_delivery_hours":
                    expected_delivery_hours,

                "actual_delivery_hours":
                    actual_delivery_hours,

                "pickup_time":
                    pickup_time,

                "delivery_time":
                    delivery_time,

                "shipment_status":
                    shipment_status,

                "shipment_cost":
                    shipment_cost

            })

        self.df = pd.DataFrame(
            shipments
        )

    def validate(self):

        validate_unique(
            self.df,
            "shipment_id"
        )

    def save(self):

        Exporter.export_csv(

            self.df,

            "outputs/shipments.csv"

        )