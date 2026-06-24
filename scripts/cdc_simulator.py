import random
import time

from sqlalchemy import create_engine

engine = create_engine(

    "mysql+pymysql://"

    "root:root"

    "@localhost:3306"

    "/logistics"

)

def update_shipment():

    shipment_id = random.randint(
        1,
        100000
    )

    status = random.choice(

        [
            "Delivered",
            "Delayed",
            "In Transit"
        ]

    )

    sql = f"""

    UPDATE shipments

    SET shipment_status = '{status}'

    WHERE shipment_id = {shipment_id}

    """

    return sql

def delete_shipment():

    shipment_id = random.randint(
        1,
        100000
    )

    sql = f"""

    DELETE

    FROM shipments

    WHERE shipment_id = {shipment_id}

    """

    return sql

def insert_shipment():

    shipment_id = random.randint(
        100001,
        999999
    )

    sql = f"""

    INSERT INTO shipments

    (
      shipment_id,
      customer_id,
      driver_id,
      vehicle_id,
      warehouse_id,
      shipment_status,
      shipment_cost
    )

    VALUES

    (
      {shipment_id},
      1,
      1,
      1,
      1,
      'In Transit',
      1500
    )

    """

    return sql

while True:

    operation = random.choice(

        [
            "insert",
            "update",
            "delete"
        ]

    )

    if operation == "insert":

        sql = insert_shipment()

    elif operation == "update":

        sql = update_shipment()

    else:

        sql = delete_shipment()

    with engine.connect() as conn:

        conn.exec_driver_sql(sql)

        conn.commit()

    print(

        f"CDC Event -> "

        f"{operation}"

    )

    time.sleep(20)