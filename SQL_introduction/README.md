
# SQL - Introduction

This project is an introduction to SQL and MySQL databases. It covers fundamental database concepts and basic SQL operations.

## Description

This project teaches the basics of databases, relational databases, SQL, and MySQL. Through a series of tasks, you'll learn how to create databases, tables, and perform basic CRUD (Create, Read, Update, Delete) operations.

## Learning Objectives

By the end of this project, you should be able to explain:

- What's a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does DDL and DML stand for
- How to CREATE or ALTER a table
- How to SELECT data from a table
- How to INSERT, UPDATE or DELETE data
- What are subqueries
- How to use MySQL functions

## Requirements

- Allowed editors: vi, vim, emacs
- All files executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All files should end with a new line
- All SQL queries should have a comment just before
- All files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- The length of your files will be tested using wc

## Installation

### Install MySQL 8.0 on Ubuntu 20.04 LTS


bash
sudo apt update
sudo apt install mysql-server
mysql --version

### Connect to MySQL server


bash
sudo mysql

## Files

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Script that lists all databases |
| `1-create_database_if_missing.sql` | Script that creates the database hbtn_0c_0 |
| `2-remove_database.sql` | Script that deletes the database hbtn_0c_0 |
| `3-list_tables.sql` | Script that lists all tables of a database |
| `4-first_table.sql` | Script that creates a table called first_table |
| `5-full_table.sql` | Script that prints the full description of first_table |
| `6-list_values.sql` | Script that lists all rows of first_table |
| `7-insert_value.sql` | Script that inserts a new row in first_table |
| `8-count_89.sql` | Script that displays the number of records with id = 89 |
| `9-full_creation.sql` | Script that creates second_table and adds multiple rows |
| `10-top_score.sql` | Script that lists all records ordered by score |
| `11-best_score.sql` | Script that lists records with score >= 10 |
| `12-no_cheating.sql` | Script that updates Bob's score to 10 |

## Usage

To run any SQL script:


bash
cat filename.sql | mysql -hlocalhost -uroot -p database_name



Example:

bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p



## Author

**Alieu O. Jobe**

## Repository

- **GitHub repository:** `alu-higher_level_programming`
- **Directory:** `SQL_introduction`
