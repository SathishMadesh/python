import mysql.connector
db = None
mycur = None

try:
    db = mysql.connector.connect(host="localhost",user="root",password="admin",database="s1")
    mycur = db.cursor()

    sql_st = ''' insert into user(uid,uname,uloc,usal)
                values(%s,%s,%s,%s) 
                '''
    
    data = [
            (101,'Sathish','Salem',45000.00),
            (102,'Sarathy','Banglour',55000.00),
            (103,'Naga','Madurai',50000.00)
           ]
    mycur.executemany(sql_st,data)
    db.commit()

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur :
        mycur.close()
    if db :
        db.close()
    