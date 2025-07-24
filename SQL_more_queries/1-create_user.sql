-- 1-create_user.sql

-- Check if the user exists
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1') 
        THEN 'user_0d_1 exists.' 
        ELSE 'user_0d_1 doesn''t exist, created user_0d_1.' 
    END AS message;

-- Create the user if it does not exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure that the changes take effect
FLUSH PRIVILEGES;
