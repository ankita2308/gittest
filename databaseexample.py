import sqlite3
con=sqlite3.connect('data.db')
c=con.cursor()
c.execute("create table person(name varchar,age int,address varchar)")
