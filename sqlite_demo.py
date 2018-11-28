import sqlite3

#conn = sqlite3.connect(':memory:') #create connect obj, can be in memory
#in memory method each time start fresh, no need comment out create or insert code
conn = sqlite3.connect('employee.db') #create connect obj
c=conn.cursor()

# only execute this once
# c.execute("""CREATE TABLE employees (
#              first text,
#              last text,
#              pay integer
#              )""") #three quote for doc string

#check sqlite data type online

#insert statement
#c.execute("INSERT INTO employees VALUES ('Corey','Schafer',50000)")
#c.execute("INSERT INTO employees VALUES ('Marry','Schafer',50000)")


#select statement i.e. read
c.execute("SELECT * FROM employees WHERE last='Schafer'")
# row=c.fetchone() #get next row from the result and only return that row
# print(type(row))
# print(row[1])

#c.fetchmany(5) #parameter determine how many row to be read

rows=c.fetchall() #get all remaining rows in a list
print(rows[1])

conn.commit() #commit to submit current change
conn.close()
