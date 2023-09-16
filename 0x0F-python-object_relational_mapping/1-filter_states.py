#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
(upper N) from the database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    """adding credentials"""
    user_name, password, database = argv[1], argv[2], argv[3]
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
    SELECT * FROM states
    WHERE BINARY name LIKE 'N%'
    ORDER BY states.id ASC
    """
    db_selector.execute(query)
    rows = db_selector.fetchall()
    for row in rows:
        print("{}".format(row))

    db_selector.close()
    db.close()
