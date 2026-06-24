import random

from datetime import datetime

def generate_gps_data():

    return {

        "vehicle_id":
            random.randint(
                1,
                500
            ),

        "latitude":
            round(
                random.uniform(
                    8,
                    37
                ),
                6
            ),

        "longitude":
            round(
                random.uniform(
                    68,
                    97
                ),
                6
            ),

        "speed":
            random.randint(
                0,
                120
            ),

        "timestamp":
            datetime.utcnow().isoformat()

    }

def generate_fuel_data():

    return {

        "vehicle_id":
            random.randint(
                1,
                500
            ),

        "fuel_level":
            random.randint(
                5,
                100
            ),

        "fuel_consumption":
            round(
                random.uniform(
                    4,
                    20
                ),
                2
            ),

        "timestamp":
            datetime.utcnow().isoformat()

    }

def generate_weather_data():

    return {

        "city":
            random.choice(

                [
                    "Delhi",
                    "Mumbai",
                    "Bangalore",
                    "Hyderabad"
                ]

            ),

        "temperature":
            random.randint(
                20,
                45
            ),

        "condition":
            random.choice(

                [
                    "Sunny",
                    "Cloudy",
                    "Rainy"
                ]

            ),

        "timestamp":
            datetime.utcnow().isoformat()

    }

