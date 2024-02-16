-- creates a hbtn_0d_usa database with table states (id, name).
-- creating a new database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- selecting out database for use.
USE hbtn_0d_usa;
-- creating a table.
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
