-- script that creates database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMART KEY UNIQUE NOT NULL,
	state_id INT,
	name VARCHAR(256) NOT NULL

	FOREIGN KEY (state_id) REFERENCES states(id)
);
