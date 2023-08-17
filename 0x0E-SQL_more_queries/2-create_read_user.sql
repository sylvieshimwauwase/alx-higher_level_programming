-- script that creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- script to create user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED  BY 'user_0d_2_pwd';
-- script to grant privileges
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
