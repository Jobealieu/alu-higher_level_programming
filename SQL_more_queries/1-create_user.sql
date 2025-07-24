-- 1-create_user.sql

-- Check if the user exists
SELECT COUNT(*) INTO @user_exists FROM mysql.user WHERE user = 'user_0d_1';

-- If the user does not exist, create it and output a message
IF @user_exists = 0 THEN
    CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
    SELECT 'user_0d_1 doesn''t exist, created user_0d_1.' AS message;
ELSE
    SELECT 'user_0d_1 exists.' AS message;
END IF;

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Flush privileges to ensure that the changes take effect
