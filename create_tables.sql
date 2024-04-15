    CREATE TABLE Workers (
    worker_id                NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
    worker_first_name        VARCHAR2(100),
    worker_last_name         VARCHAR2(100),
    worker_email             VARCHAR2(100),
    worker_address           VARCHAR2(200),
    worker_role              NUMBER
);
    
    CREATE TABLE Customers (
    customer_id              NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
    customer_first_name      VARCHAR2(100),
    customer_last_name       VARCHAR2(100),
    customer_email           VARCHAR2(100),
    customer_address         VARCHAR2(200),
);

CREATE TABLE Cleaning_Variants (
    variant_id               CHAR(3) NOT NULL PRIMARY KEY,
    variant_name             VARCHAR2(50),
    variant_standard_cost_per_hour   NUMBER,
    variant_outside_cost_per_hour    NUMBER
);

CREATE TABLE Orders(
    order_id                 NUMBER GENERATED ALWAYS AS IDENTITY NOT NULL PRIMARY KEY,
    cleaning_variant_fk      CHAR(3),
    cleaning_duration        NUMBER,
    is_inside_cleaning       CHAR(1) CHECK(is_inside_cleaning in ('Y', 'N')),
    is_outside_cleaning      CHAR(1) CHECK(is_outside_cleaning in ('Y', 'N')),
    travel_distance          NUMBER,
    salesman_id_fk           NUMBER,
    customer_id_fk           NUMBER,
    cleaning_address         VARCHAR2(200),
    cleaning_date            DATE,
    FOREIGN KEY (cleaning_variant_fk) REFERENCES Cleaning_Variants(variant_id),
    FOREIGN KEY (salesman_id_fk) REFERENCES Workers(worker_id),
    FOREIGN KEY (customer_id_fk) REFERENCES Customers(customer_id)
);


ALTER TABLE orders DROP CONSTRAINT SYS_C008230;
ALTER TABLE orders DROP CONSTRAINT SYS_C008227;
ALTER TABLE orders DROP CONSTRAINT SYS_C008228;

ALTER TABLE cleaning_variants MODIFY variant_id INTEGER;

ALTER TABLE orders MODIFY cleaning_variant_fk INTEGER;

ALTER TABLE orders ADD CONSTRAINT fk_variant_id FOREIGN KEY (cleaning_variant_fk)
REFERENCES cleaning_variants (variant_id);

ALTER TABLE orders MODIFY is_inside_cleaning CHAR(5);
ALTER TABLE orders MODIFY is_outside_cleaning CHAR(5);
ALTER TABLE orders MODIFY cleaning_date VARCHAR(20);

ALTER TABLE orders ADD realization_date DATE;

UPDATE orders
SET realization_date = TO_DATE(SUBSTR(cleaning_date, 1, 10), 'YYYY-MM-DD');

ALTER TABLE orders DROP COLUMN cleaning_date;

UPDATE orders
SET realization_date = TO_DATE(realization_date, 'YYYY-MM-DD');
--------------------------------------------------------------------
--------------------------------------------------------------------
CREATE VIEW orders_with_costs AS
-- This view contains all the data needed for my analysis and project. 
-- It also creates three new columns storing data about the costs of orders
WITH temp_table AS (
    SELECT
        o.*,
        cv.variant_name, cv.variant_standard_cost_per_hour, cv.variant_outside_cost_per_hour,
        CASE
            WHEN o.is_outside_cleaning = 'True' THEN o.cleaning_duration * cv.variant_outside_cost_per_hour
            ELSE o.cleaning_duration * cv.variant_standard_cost_per_hour
        END AS cleaning_cost_without_travel,
        o.travel_distance * 2.2 as travel_cost
    FROM 
        orders o
    RIGHT JOIN 
        cleaning_variants cv ON o.cleaning_variant_fk = cv.variant_id
)
SELECT 
    tb.*,
    (cleaning_cost_without_travel + travel_cost) as total_cost,
    w.worker_first_name, w.worker_last_name, 
    c.customer_first_name, c.customer_last_name
FROM 
    temp_table tb
RIGHT JOIN
    workers w ON tb.salesman_id_fk = w.worker_id
RIGHT JOIN customers c ON tb.customer_id_fk = c.customer_id;