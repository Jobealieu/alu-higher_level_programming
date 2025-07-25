-- Creates table unique_id on MySQL server
-- id INT with default value 1 and must be unique
-- name VARCHAR(256)
-- If table already exists, script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
