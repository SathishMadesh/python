import mysql.connector
import requests

db = None
mycur = None

try:

    db = mysql.connector.connect(host="localhost", user="root",password="admin",database="s1")
    mycur = db.cursor()

    sql_st = ''' insert into PRODUCTS (prId,Product_Name,Price,Rating,Stocks)
                 values(%s,%s,%s,%s,%s)
                '''
    
    response = requests.get('https://dummyjson.com/products')
    product_dict = response.json()
    product_list = product_dict['products']
    data = []

    for product in product_list:
        data.append((product['id'],product['title'],product['price'],product['rating'],product['stock']))

    mycur.executemany(sql_st,data)
    db.commit()

except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    if mycur:
        mycur.close()
    if db:
        db.close()
