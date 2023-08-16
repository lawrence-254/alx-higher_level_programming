-- Creates the database hbtn_0d_2 and the user user_0d_2

-- db creation
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- User creation
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- previlages granting
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
