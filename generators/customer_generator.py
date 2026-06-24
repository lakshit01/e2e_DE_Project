from faker import Faker
import pandas as pd

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique
from validators.null_validator import validate_null

from utils.exporter import Exporter

fake = Faker()

class CustomerGenerator(BaseGenerator):

    def __init__(self, config):

        self.config = config

        self.df = None

    def generate(self):

        customers = []

        for customer_id in range(
            1,
            self.config["customers"] + 1
        ):

            customers.append({

                "customer_id": customer_id,

                "customer_name": fake.name(),

                "city": fake.city(),

                "state": fake.state(),

                "created_date":
                    fake.date_time_this_decade()

            })

        self.df = pd.DataFrame(customers)

    def validate(self):

        validate_unique(
            self.df,
            "customer_id"
        )

        validate_null(
            self.df,
            "customer_name"
        )

    def save(self):

        Exporter.export_csv(

            self.df,

            "outputs/customers.csv"
        )