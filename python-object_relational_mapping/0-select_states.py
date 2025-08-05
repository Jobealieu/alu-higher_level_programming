#!/usr/bin/python3
"""Script that lists all states with a name starting with N from the database"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    # Create cursor object
    cursor = db.cursor()
    
    # Execute SQL query to select states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Fetch all results
    results = cursor.fetchall()
    
    # Print results
    for row in results:
        print(row)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
