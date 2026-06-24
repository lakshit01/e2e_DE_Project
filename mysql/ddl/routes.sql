CREATE TABLE routes
(
 route_id INT PRIMARY KEY,

 source_city VARCHAR(100),

 destination_city VARCHAR(100),

 distance_km INT,

 expected_delivery_hours DECIMAL(10,2)
);