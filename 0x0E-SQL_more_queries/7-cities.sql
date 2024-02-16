-- creates the database hbtn_0d_usa with table cities (id, states_id, name)
-- creating the database.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- selecting database for use.
USE hbtn_0d_usa;
-- creating table
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);
