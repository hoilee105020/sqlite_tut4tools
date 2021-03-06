import sqlite3
from datetime import date, datetime

conn = sqlite3.connect(':memory:') #create connect obj, can be in memory
#in memory method each time start fresh, no need comment out create or insert code
#conn = sqlite3.connect('nmh.db') #create connect obj

c=conn.cursor()
c.execute("PRAGMA foreign_keys=ON")
#c.execute("PRAGMA foreign_keys")
#only execute this once
c.execute("""CREATE TABLE curators (
             id INT PRIMARY KEY,
             name VARCHAR(255),
             bio TEXT
             )""")

c.execute("""CREATE TABLE exhibits (
             id INT,
             name VARCHAR(255),
             start_date DATE,
             end_date DATE,
             curator_id INT,
             FOREIGN KEY(curator_id) REFERENCES curators(id)
             )""") #three quote for doc string

#check sqlite data type online

#insert curators
c.execute("INSERT INTO curators VALUES (11,'Simon Strauss','Space man')")
c.execute("INSERT INTO curators VALUES (71,'Rick Sanchez','Grandfather')")
c.execute("INSERT INTO curators VALUES (5,'Rebecca Votea','Esteemed naturalist')")


#insert exhibits
c.execute("INSERT INTO exhibits VALUES (3,'Free The Fishes','2018-01-01','2018-06-30',5)")
c.execute("INSERT INTO exhibits VALUES (17,'Space, What Lies Above','2018-02-01','2018-05-30',11)")
c.execute("INSERT INTO exhibits VALUES (23,'Bears Bears Bears','2018-02-14','2018-02-24',5)")
c.execute("INSERT INTO exhibits VALUES (46,'Humans? Aliens?','2019-03-14','2019-10-21',11)")

#select statement i.e. read
# c.execute("SELECT * FROM exhibits")
# rows=c.fetchall() #get all remaining rows in a list
# print(rows[0])
# print(rows[1])
# print(rows[2])
# print(rows[3])

#read curators and sort by descend id
#Syntax: SELECT * FROM table_name ORDER BY column_name ASC|DESC
# c.execute("SELECT name FROM curators ORDER BY id DESC")
# rows=c.fetchall() #get all remaining rows in a list
# print(rows[0])
# print(rows[1])
# print(rows[2])

#learn different kind of join, right and outer join not support in sqlite
#c.execute("SELECT c.name, e.name FROM curators c JOIN exhibits e ON c.id=e.curator_id")
# c.execute("SELECT c.name, e.name FROM curators c LEFT JOIN exhibits e ON c.id=e.curator_id")
# rows=c.fetchall()
# print(rows)

#c.execute("SELECT c.name, e.name FROM curators c LEFT JOIN exhibits e ON c.id=e.curator_id WHERE c.name LIKE 'R%'")
# c.execute("SELECT c.name, COUNT(e.name) FROM curators c LEFT JOIN exhibits e ON c.id=e.curator_id WHERE c.name LIKE 'R%' GROUP BY c.name")
# rows=c.fetchall()
# print(rows)

#figure out date
c.execute("SELECT * from exhibits")
rows=c.fetchall()
now0=datetime.strptime(rows[0][2],'%Y-%m-%d').date()
now1=datetime.strptime(rows[1][2],'%Y-%m-%d').date()
now2=datetime.strptime(rows[2][2],'%Y-%m-%d').date()
now3=datetime.strptime(rows[3][2],'%Y-%m-%d').date()

#now00=date.strftime('%Y-%m-%d',rows[0][2])
#now00=datetime(int(rows[0][2]))

#show overlap
#trick is use e1.id<e2.id to make them unique
c.execute("SELECT e1.name,e2.name from exhibits e1, exhibits e2 WHERE e1.start_date<=e2.end_date and e2.start_date<=e1.end_date and e1.id<e2.id")
rows=c.fetchall()
print(rows)

conn.commit() #commit to submit current change
conn.close()
