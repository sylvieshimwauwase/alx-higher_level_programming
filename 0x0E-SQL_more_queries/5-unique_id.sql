-- script that creates the table
CREATE TABLE IF NOT EXISTS id_not_null (
        id INT = 1 UNIQUE,
        name VARCHAR(256)
);
