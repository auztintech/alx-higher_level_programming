#!/usr/bin/python3
"""
this script lists all 'states' from the database 'hbtn_0e_0_usa'
where `name` matches the argument 'state name searched'
Arguments:
    mysql username (str)
    mysql password (str)
    database name (str)
"""

import sys
import MySQLdb

if __name__ == "__main__":
    mySql_user = sys.argv[1]
    mySql_passwd = sys.argv[2]
    mySql_database = sys.argv[3]

    searched_name = sys.argv[4]

    #By default the it will connect to localhost @ 3306
    db = MySQLdb.connect(user=mySql_user, passwd=mySql_passwd, db=mySql_database)
    mycur = db.cursor()

    mycur.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                (searched_name, ))
    rows = mycur.fetchall()

    for row in rows:
        print(row)
    