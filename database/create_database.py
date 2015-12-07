#!/usr/bin/env python

import sqlite3
conn = sqlite3.connect('users.db')

table_name = 'users'

c = conn.cursor() 

c.execute('DROP TABLE IF EXISTS {}'.format(table_name))
conn.commit()
c.execute("""CREATE TABLE {}
             (id INTEGER PRIMARY KEY, 
              fname text, 
              lname text)""".format(table_name))

conn.commit()

conn.close()




