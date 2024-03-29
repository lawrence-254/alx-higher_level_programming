#!/usr/bin/python3
"""
a script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv
if __name__ == "__main__":
    """CHECKS FOR CORRECT NUMBER OF ARGUMENTS"""
    if len(argv) != 5:
        print("Usage: ./2-my_filter_states.py root"
              "root hbtn_0e_0_usa 'state_name'")
        exit(1)

    """adding credentials"""
    user_name, password, database, match = argv[1], argv[2], argv[3], argv[4]
    try:
        db = MySQLdb.connect(
                host="localhost",
                user=user_name,
                passwd=password,
                db=database,
                port=3306
                )
        db_selector = db.cursor()
        query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '%{}%'
        ORDER BY states.id ASC
        """.format(match)

        db_selector.execute(query)
        rows = db_selector.fetchall()
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)

    finally:
        db_selector.close()
        db.close()
