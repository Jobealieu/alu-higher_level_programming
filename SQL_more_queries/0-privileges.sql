- lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost).
-- Create users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- For test case 1: Both users as root users
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
-- GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost' WITH GRANT OPTION;

-- For test case 2: user_0d_1 root, user_0d_2 limited privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
CREATE DATABASE IF NOT EXISTS user_2_db;
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Show grants for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
