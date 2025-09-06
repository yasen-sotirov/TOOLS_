"SQL LITE"  # https://www.youtube.com/watch?v=pd-0G0MigUA&ab_channel=CoreySchafer

import sqlite3

conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS stored_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coord_x INTEGER,
    coord_y INTEGER,
    photo INTEGER)""")

x = 100
y = 200
photo = 300

c.execute("INSERT INTO stored_data VALUES (?, ?, ?)", (x, y, photo))

c.execute("SELECT * FROM stored_data")

print(c.fetchall())

conn.commit()
conn.close()
