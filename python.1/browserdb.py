#!/usr/bin/python

import sqlite3

conn = sqlite3.connect("cookies.sqlite")

sites = []
# need a cursor to keep track of where we are
cur = conn.cursor()
for row in cur.execute("SELECT * FROM moz_cookies"):
    if row[1] not in sites:
        sites.append(row[1])

sites.sort()

for s in sites:
    print(s)

