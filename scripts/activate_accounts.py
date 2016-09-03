import sqlite3 as lite
import sys


con = lite.connect('../db.sqlite3')

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM auth_user")

    rows = cur.fetchall()

    for row in rows:
        if row[0] != 1:
            cur.execute("UPDATE auth_user SET is_staff = 1 WHERE id = %s" % row[0])
print "Complete"
