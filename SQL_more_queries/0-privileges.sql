-- Script to list all privileges for user_0d_1 and user_0d_2 on localhost
-- This script works for both test scenarios:
-- Scenario 1: Both users have root privileges
-- Scenario 2: user_0d_1 has root privileges, user_0d_2 has SELECT/INSERT on user_2_db
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
