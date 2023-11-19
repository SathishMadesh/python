import mysql.connector

db = None
mycur = None

try:

    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="s1")
    mycur = db.cursor()

    sql_st = ''' create table PRODUCTS (
                 prId int,
                 Name varchar(255),
                 Price int,
                 Rating float,
                 Stocks int
            ) '''
    
    mycur.execute(sql_st)
    db.commit()


except mysql.connector.DatabaseError as err:
    if err:
        print (err)

finally:
    if mycur:
        mycur.close()
    if db:
        db.close()