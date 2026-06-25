import pymysql

conn = pymysql.connect(
    host="logistics-mysql.cju20w6u0l15.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="Admin-321"
)

cursor = conn.cursor()

cursor.execute(
    "CREATE DATABASE IF NOT EXISTS logistics"
)

cursor.execute(
    "USE logistics"
)

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers
(
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    city VARCHAR(100),
    state VARCHAR(100),
    created_date DATETIME
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS drivers
(
    driver_id INT PRIMARY KEY,
    driver_name VARCHAR(100),
    license_number VARCHAR(50),
    joining_date DATE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS routes
(
 route_id INT PRIMARY KEY,
 source_city VARCHAR(100),
 destination_city VARCHAR(100),
 distance_km INT,
 expected_delivery_hours DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS shipments
(
    shipment_id INT PRIMARY KEY,
    customer_id INT,
    vehicle_id INT,
    warehouse_id INT,
    route_id INT,
    distance_km INT,
    expected_delivery_hours DECIMAL(10,2),
    actual_delivery_hours DECIMAL(10,2),
    pickup_time DATETIME,
    delivery_time DATETIME,
    shipment_status VARCHAR(50),
    shipment_cost DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehicles
(
    vehicle_id INT PRIMARY KEY,
    vehicle_type VARCHAR(50),
    registration_number VARCHAR(50),
    capacity_tons DECIMAL(10,2)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS warehouses
(
    warehouse_id INT PRIMARY KEY,
    warehouse_name VARCHAR(100),
    city VARCHAR(100)
)
""")

conn.commit()

print("Schema Created")