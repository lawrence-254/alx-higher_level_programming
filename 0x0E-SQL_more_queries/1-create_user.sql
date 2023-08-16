-- Script that creates the MySQL server user user_0d_1

-- creating user if not available
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED WITH mysql_native_password BY 'user_0d_1_pwd';
-- grants privileges to user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- reloads privilages to ensure user access
FLUSH PRIVILEGES;
