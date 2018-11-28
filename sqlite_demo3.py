import sqlite3
from employee import Employee

conn = sqlite3.connect(':memory:') #create connect obj, can be in memory
#in memory method each time start fresh, no need comment out create or insert code
c=conn.cursor()

c.execute("""CREATE TABLE employees (
             first text,
             last text,
             pay integer
             )""") #three quote for doc string

c.execute("INSERT INTO employees VALUES ('Corey','Schafer',50000)")
c.execute("INSERT INTO employees VALUES ('Marry','Schafer',50000)")
emp_1=Employee('John','Doe',80000)
emp_2=Employee('Jane','Doe',90000)
c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay)) 
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay})
conn.commit()

c.execute("SELECT * FROM employees WHERE last=?",('Schafer',)) #follow by tuple
print(c.fetchall())
c.execute("SELECT * FROM employees WHERE last=:last",{'last':'Doe'}) #follow by dict
print(c.fetchall())

conn.commit() #commit to submit current change
conn.close()
