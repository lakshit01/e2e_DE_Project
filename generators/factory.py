from generators.customer_generator import CustomerGenerator
from generators.driver_generator import DriverGenerator
from generators.vehicle_generator import VehicleGenerator
from generators.warehouse_generator import WarehouseGenerator
from generators.shipment_generator import ShipmentGenerator
from generators.route_generator import RouteGenerator

class GeneratorFactory:

    @staticmethod
    def get_generator(
        entity,
        config
    ):

        mapping = {

            "customer":
                CustomerGenerator,

            "driver":
                DriverGenerator,

            "vehicle":
                VehicleGenerator,

            "warehouse":
                WarehouseGenerator,

            "route":
                RouteGenerator,

            "shipment":
                ShipmentGenerator
        }

        if entity not in mapping:

            raise ValueError(
                f"{entity} not supported"
            )

        return mapping[
            entity
        ](config)