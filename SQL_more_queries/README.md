
# SQL - More queries

This project covers advanced MySQL concepts including user management, privileges, constraints, and complex queries with joins and subqueries.

## Description

This project is part of the ALU Higher Level Programming curriculum, focusing on advanced SQL operations in MySQL 8.0. You'll learn to manage users, handle database privileges, work with constraints, and perform complex queries across multiple tables.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without external help:

### General
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a `PRIMARY KEY`
- What's a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before (syntax above)
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (`SELECT`, `WHERE`, etc.)
- File length will be tested using `wc`

## Environment Setup

### Install MySQL 8.0 on Ubuntu 20.04 LTS


bash
$ sudo apt update
$ sudo apt install mysql-server
$ mysql --version


### Connect to MySQL Server


bash
$ sudo mysql

In container, use credentials: root/root

### Import SQL Dump Example


bash
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows


## Project Structure


SQL_more_queries/
├── README.md
├── 0-privileges.sql          # List user privileges
├── 1-create_user.sql         # Create MySQL user with all privileges
├── 2-create_read_user.sql    # Create database and read-only user
├── 3-force_name.sql          # Create table with NOT NULL constraint
├── 4-never_empty.sql         # Create table with default value
├── 5-unique_id.sql           # Create table with UNIQUE constraint
├── 6-states.sql              # Create states table with PRIMARY KEY
├── 7-cities.sql              # Create cities table with FOREIGN KEY
├── 8-cities_of_california_subquery.sql  # Query with subquery
├── 9-cities_by_state_join.sql           # Query with JOIN
├── 10-genre_id_by_show.sql              # TV shows with genres
└── 11-genre_id_all_shows.sql            # All shows including those without genres


## Key Concepts Covered

### User Management
- Creating MySQL users
- Granting and managing privileges
- Database and table-level permissions

### Database Constraints
- `PRIMARY KEY`: Unique identifier for table records
- `FOREIGN KEY`: References primary key in another table
- `NOT NULL`: Prevents null values
- `UNIQUE`: Ensures unique values
- `DEFAULT`: Sets default values for columns

### Advanced Queries
- **Subqueries**: Nested queries for complex data retrieval
- **JOINs**: Combining data from multiple tables
- **UNION**: Combining results from multiple SELECT statements

## Usage Examples

### Running SQL Scripts


bash
# Execute a script
$ cat script_name.sql | mysql -hlocalhost -uroot -p database_name

Check privileges
$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p

Create user and database
$ cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p


### SQL Comment Format


sql
-- Description of what the query does
-- Additional context if needed
SELECT column1, column2 FROM table_name WHERE condition;


## Files Description

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists privileges for specified users |
| `1-create_user.sql` | Creates user with all privileges |
| `2-create_read_user.sql` | Creates database and read-only user |
| `3-force_name.sql` | Creates table with NOT NULL constraint |
| `4-never_empty.sql` | Creates table with default values |
| `5-unique_id.sql` | Creates table with UNIQUE constraint |
| `6-states.sql` | Creates states table with auto-increment PRIMARY KEY |
| `7-cities.sql` | Creates cities table with FOREIGN KEY reference |
| `8-cities_of_california_subquery.sql` | Uses subquery to find California cities |
| `9-cities_by_state_join.sql` | Uses JOIN to list cities with their states |
| `10-genre_id_by_show.sql` | Lists TV shows with their genres |
| `11-genre_id_all_shows.sql` | Lists all shows including those without genres |

## Author

**Alieu O. Jobe**

## Repository

- **GitHub repository**: `alu-higher_level_programming`
- **Directory**: `SQL_more_queries`

## Resources

- [MySQL 8.0 Documentation](https://dev.mysql.com/doc/refman/8.0/en/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
