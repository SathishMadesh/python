import mysql.connector

db = None
dbcursor = None

try:

    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="s1")
    dbcursor = db.cursor()
    sql_st = ''' create table USER (
                uid int,
                uname varchar(32),
                uloc varchar(32),
                usal float
                ) '''
    dbcursor.execute(sql_st)
    db.commit()

except mysql.connector.DatabaseError as err:
    if err:
        print (err)
        
finally:
    if dbcursor:
        dbcursor.close()
    if db:
       db.close()