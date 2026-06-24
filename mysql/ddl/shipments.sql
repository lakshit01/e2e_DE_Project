CREATE TABLE shipments
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
);