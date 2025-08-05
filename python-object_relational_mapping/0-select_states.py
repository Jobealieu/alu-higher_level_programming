#!/usr/bin/python3
"""Script that lists all states with a name starting with N from hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query - filter states starting with 'N', sorted by id
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
