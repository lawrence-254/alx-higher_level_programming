#!/usr/bin/python3
"""
a script that lists all cities from the database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    """adding credentials"""
    user_name, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database,
            port=3306
            )
    db_selector = db.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON states.id = cities.state_id
    ORDER BY cities.id ASC
    """
    db_selector.execute(query)
    rows = db_selector.fetchall()
    for row in rows:
        print("{}".format(row))

    db_selector.close()
    db.close()
