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