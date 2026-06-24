from faker import Faker

import pandas as pd
import random

from generators.base_generator import BaseGenerator

from validators.unique_validator import validate_unique

from utils.exporter import Exporter

fake = Faker()

VEHICLE_TYPES = [
	"Truck",
	"Van",
	"Trailer",
	"Container",
	"Pickup"
]


class VehicleGenerator(BaseGenerator):

	def __init__(self, config):

		self.config = config

		self.df = None

	def generate(self):

		vehicles = []

		for vehicle_id in range(

			1,

			self.config["vehicles"] + 1

		):

			vehicle_type = random.choice(
				VEHICLE_TYPES
			)

			registration = fake.bothify(text="??-####-???")

			capacity = round(
				random.uniform(
					1,
					50
				),
				2
			)

			vehicles.append({

				"vehicle_id":
					vehicle_id,

				"vehicle_type":
					vehicle_type,

				"registration_number":
					registration,

				"capacity_tons":
					capacity

			})

		self.df = pd.DataFrame(
			vehicles
		)

	def validate(self):

		validate_unique(
			self.df,
			"vehicle_id"
		)

	def save(self):

		Exporter.export_csv(

			self.df,

			"outputs/vehicles.csv"

		)

