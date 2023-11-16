import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="admin", database="s1")

dbcursor = db.cursor()

sql_st = ''' create table EMPLOYEE(
            eId int,
            eName varchar(32),
            eLoc varchar(32),
            eSal float
        ) '''
dbcursor.execute(sql_st)
db.commit()

dbcursor.close()

db.close()
