import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="s1")

mycursor = mydb.cursor()

sql_st = ''' insert into employee
             values (1,'Sathish','Banglour',45000.00) '''

mycursor.execute(sql_st)
mydb.commit()

mycursor.close()

mydb.close()