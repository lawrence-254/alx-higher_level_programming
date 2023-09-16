#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
"""import MySQLdb
from sys import argv
if __name__ == "__main__":

    """adding credentials"""
    user_name, password, database, match = argv[1], argv[2], argv[3], argv[4]
    """creating a connection to db"""
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database,
            port=3306
            )
    """connect db to an environment to work as db management tool"""
    db_selector = db.cursor()
    query = """
    SELECT * from states
    WHERE name = %s
    ORDER BY states.id ASC
    """
    db_selector.execute(query, (match,))
    rows = db_selector.fetchall()
    for row in rows:
        print("{}".format(row))

    db_selector.close()
    db.close()
