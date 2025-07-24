-- Script to create users and assign privileges, then list them
-- Create user_0d_1 and grant root privileges (all privileges)
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Create user_0d_2 and grant only SELECT and INSERT on user_2_db
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS user_2_db;
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

-- Show privileges for both users
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
