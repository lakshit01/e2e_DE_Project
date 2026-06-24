from faker import Faker

import pandas as pd

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique

from utils.exporter import Exporter

fake = Faker()

class DriverGenerator(BaseGenerator):

    def __init__(self, config):

        self.config = config

        self.df = None

    def generate(self):

        drivers = []

        for driver_id in range(
            1,
            self.config["drivers"] + 1
        ):

            drivers.append({

                "driver_id": driver_id,

                "driver_name": fake.name(),

                "license_number":
                    fake.uuid4(),

                "joining_date":
                    fake.date()

            })

        self.df = pd.DataFrame(drivers)

    def validate(self):

        validate_unique(
            self.df,
            "driver_id"
        )

    def save(self):

        Exporter.export_csv(
            self.df,
            "outputs/drivers.csv"
        )