import argparse

from utils.config_reader import load_config

from generators.factory import GeneratorFactory

from utils.logger import logger

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--entity",
        default="all"
    )

    parser.add_argument(
        "--env",
        default="dev"
    )

    args = parser.parse_args()

    config = load_config(
        args.env
    )

    entities = [

        "customer",
        "driver",
        "vehicle",
        "warehouse",
        "route",
        "shipment"

    ]

    if args.entity != "all":

        entities = [
            args.entity
        ]

    for entity in entities:

        logger.info(
            f"Generating {entity}"
        )

        generator = (
            GeneratorFactory
            .get_generator(
                entity,
                config
            )
        )

        generator.generate()

        generator.validate()

        generator.save()

        logger.info(
            f"{entity} completed"
        )

if __name__ == "__main__":

    main()