
# Python - Object-relational mapping

This project demonstrates the connection between Python and MySQL databases using two different approaches: direct MySQL queries with MySQLdb and Object-Relational Mapping (ORM) with SQLAlchemy.

## 📋 Table of Contents

- [Description](#description)
- [Technologies Used](#technologies-used)
- [Requirements](#requirements)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Tasks Overview](#tasks-overview)
- [Usage Examples](#usage-examples)
- [Learning Objectives](#learning-objectives)
- [Author](#author)

## 📝 Description

This project explores two fundamental approaches to database interaction in Python:

1. **Direct MySQL Queries**: Using the MySQLdb module to execute raw SQL queries
2. **Object-Relational Mapping (ORM)**: Using SQLAlchemy to interact with databases through Python objects

The project progresses from basic database connections and queries to advanced ORM concepts, demonstrating the evolution from SQL-dependent code to storage-agnostic Python applications.

## 🛠 Technologies Used

- **Python 3.8.5**
- **MySQL 8.0**
- **MySQLdb 2.0.x**
- **SQLAlchemy 1.4.x**
- **Ubuntu 20.04 LTS**

## 📋 Requirements

### System Requirements
- Ubuntu 20.04 LTS
- Python 3.8.5
- MySQL 8.0

### Python Modules
- MySQLdb (version 2.0.x)
- SQLAlchemy (version 1.4.x)

### Code Standards
- All files must end with a new line
- First line: `#!/usr/bin/python3`
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- All modules, classes, and functions must have documentation

## 🔧 Installation

### Install MySQL 8.0

bash
# Follow MySQL 8.0 installation guide for Ubuntu 20.04

### Install MySQLdb module

bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient

### Install SQLAlchemy module

bash
sudo pip3 install SQLAlchemy

### Verify Installation

bash
python3
import MySQLdb
MySQLdb.version_info 
(2, 0, 3, 'final', 0)
import sqlalchemy
sqlalchemy.version 
'1.4.22'





## 📁 Project Structure


python-object_relational_mapping/
├── README.md
├── 0-select_states.py          # List all states
├── 1-filter_states.py          # Filter states starting with 'N'
├── 2-my_filter_states.py       # Filter states by user input
├── 3-my_safe_filter_states.py  # SQL injection safe filtering
├── 4-cities_by_state.py        # List all cities with their states
├── 5-filter_cities.py          # Filter cities by state name
├── model_state.py              # State model definition
├── 6-model_state.py            # Create State table using SQLAlchemy
├── 7-model_state_fetch_all.py  # Fetch all states using ORM
├── 8-model_state_fetch_first.py # Fetch first state using ORM
├── 9-model_state_filter_a.py   # Filter states containing 'a'
├── 10-model_state_my_get.py    # Get state by name
├── 11-model_state_insert.py    # Insert new state
├── 12-model_state_update_id_2.py # Update state with id=2
├── 13-model_state_delete_a.py  # Delete states containing 'a'
├── model_city.py               # City model definition
└── 14-model_city_fetch_by_state.py # Fetch cities by state


## 📋 Tasks Overview

### MySQLdb Tasks (0-5)
- **Task 0**: Basic state listing
- **Task 1**: Filter states by name pattern
- **Task 2**: User input filtering (vulnerable to SQL injection)
- **Task 3**: Safe user input filtering
- **Task 4**: Join queries for cities and states
- **Task 5**: Filter cities by state name

### SQLAlchemy Tasks (6-14)
- **Task 6**: Define State model class
- **Task 7**: List all states using ORM
- **Task 8**: Get first state using ORM
- **Task 9**: Filter states containing specific characters
- **Task 10**: Get state by name
- **Task 11**: Insert new state record
- **Task 12**: Update existing state record
- **Task 13**: Delete states with specific criteria
- **Task 14**: City model and relationship queries

## 💡 Usage Examples

### MySQLdb Example

python
#!/usr/bin/python3
import MySQLdb
Connect to database
conn = MySQLdb.connect(host="localhost", port=3306, 
                      user="root", passwd="root", 
                      db="hbtn_0e_0_usa", charset="utf8")
cur = conn.cursor()

Execute query
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cur.fetchall()

Display results
for row in query_rows:
    print(row)

Close connections
cur.close()
conn.close()


### SQLAlchemy Example

python
#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
Create engine and session
engine = create_engine('mysql+mysqldb://root:root@localhost/hbtn_0e_6_usa')
Session = sessionmaker(bind=engine)
session = Session()

Query using ORM
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

session.close()


### Running the Scripts

bash
# MySQLdb examples
./0-select_states.py root root hbtn_0e_0_usa
./1-filter_states.py root root hbtn_0e_0_usa
./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
SQLAlchemy examples
./7-model_state_fetch_all.py root root hbtn_0e_6_usa
./8-model_state_fetch_first.py root root hbtn_0e_6_usa
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas


## 🎯 Learning Objectives

By completing this project, you will understand:

- **Database Connectivity**: How to connect Python to MySQL databases
- **SQL Operations**: SELECT, INSERT, UPDATE, DELETE operations from Python
- **SQL Injection**: Understanding and preventing SQL injection attacks
- **ORM Concepts**: Object-Relational Mapping principles and benefits
- **SQLAlchemy**: Using SQLAlchemy for database operations
- **Model Definition**: Creating Python classes that map to database tables
- **Relationships**: Handling foreign keys and table relationships
- **Query Building**: Building complex queries using ORM syntax

## 🔍 Key Concepts

### Without ORM (MySQLdb)
- Direct SQL query execution
- Manual connection management
- SQL injection vulnerabilities
- Database-specific syntax

### With ORM (SQLAlchemy)
- Object-oriented database interaction
- Automatic connection management
- Built-in SQL injection protection
- Database-agnostic code

## 🚀 Advanced Features

- **Declarative Base**: Using SQLAlchemy's declarative base for model definition
- **Session Management**: Proper session handling for database operations
- **Query Optimization**: Efficient querying techniques
- **Relationship Mapping**: Foreign key relationships between models

## ⚠️ Important Notes

- Always validate user input to prevent SQL injection
- Use parameterized queries when working with MySQLdb
- SQLAlchemy provides built-in protection against SQL injection
- Ensure proper session management to avoid memory leaks
- All classes inheriting from Base must be imported before calling `Base.metadata.create_all(engine)`

## 🧪 Testing

The project includes various test scenarios:
- Empty database handling
- SQL injection attempts
- Invalid input handling
- Relationship queries
- CRUD operations

## 📚 Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [MySQLdb Documentation](https://mysqlclient.readthedocs.io/)
- [MySQL 8.0 Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)

## 👨‍💻 Author

**Alieu O. Jobe**
