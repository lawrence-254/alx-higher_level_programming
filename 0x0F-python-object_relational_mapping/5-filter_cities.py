#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    user_name, password, database, state = argv[1], argv[2], argv[3], argv[4]
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=password,
            db=database,
            port=3306
            )
    db_selector = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    WHERE cities.state_id = (
        SELECT states.id
        FROM states
        WHERE states.name = %s
    )
    ORDER BY cities.id ASC
    """
    db_selector.execute(query, (state, ))
    rows = db_selector.fetchall()
    city_names = [row[0] for row in rows]

    city_name_str = ", ".join(city_names)
    print(city_name_str)

    db_selector.close()
    db.close()
