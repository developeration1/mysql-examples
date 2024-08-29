CREATE DATABASE restaurant;
USE restaurant;

CREATE TABLE dishes (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    dish VARCHAR(20) NOT NULL,
    dish_description_ TEXT(100),
    price FLOAT NOT NULL,
    is_promo bool NOT NULL DEFAULT FALSE
);

CREATE TABLE addresses (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    building_number INT NOT NULL,
    internal_number INT,
    street VARCHAR(50) NOT NULL,
    zip_code INT(5) NOT NULL,
    zone VARCHAR(50),
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL
);

CREATE TABLE clients (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(15),
    last_name VARCHAR(15),
    phone INT
);

CREATE TABLE orders (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    client_id INT NOT NULL,
    address_id INT NOT NULL,
    FOREIGN KEY (client_id) REFERENCES clients(id),
    FOREIGN KEY (address_id) REFERENCES addresses(id)
);

CREATE TABLE dishes_on_orders (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
    dish_id INT NOT NULL,
    order_id INT NOT NULL,
    FOREIGN KEY (dish_id) REFERENCES dishes(id),
    FOREIGN KEY (order_id) REFERENCES orders(id)
);