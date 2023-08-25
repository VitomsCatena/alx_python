#!/usr/bin/python3

"""Module that lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and state name from command-line arguments
    # and Connect to MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    c.execute(query)
......
#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table of
   hbtn_0e_0_usa where name matches the argument, safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name =%s\
                  ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for r in rows:
        print(r)
