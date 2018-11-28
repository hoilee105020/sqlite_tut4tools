import sqlite3
from employee import Employee

#this demo show how to insert python var to database
conn = sqlite3.connect('employee.db') #create connect obj
c=conn.cursor()

emp_1=Employee('John','Doe',80000)
emp_2=Employee('Jane','Doe',90000)
# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)

#c.execute("INSERT INTO employees VALUES ('{}','{}',{})".format(emp_1.first,emp_1.last,emp_1.pay)) #bad way of insert subject to sql injection attack
#c.execute("INSERT INTO employees VALUES (?,?,?)", (emp_1.first,emp_1.last,emp_1.pay)) #right way1, tuple
#c.execute("INSERT INTO employees VALUES (:first,:last,:pay)", {'first':emp_2.first,'last':emp_2.last,'pay':emp_2.pay}) #right way2, dictionary

#old method of fetching
# c.execute("SELECT * FROM employees WHERE last='Doe'")
# rows=c.fetchall() #get all remaining rows in a list
# print(rows)
# c.execute("SELECT * FROM employees WHERE last='Schafer'")
# rows=c.fetchall() #get all remaining rows in a list
# print(rows)

#new fetching method1
c.execute("SELECT * FROM employees WHERE last=?",('Schafer',)) #follow by tuple
print(c.fetchall())
#new fetching method2
c.execute("SELECT * FROM employees WHERE last=:last",{'last':'Doe'}) #follow by dict
print(c.fetchall())

conn.commit() #commit to submit current change
conn.close()
