import requests
import csv

response = requests.get('https://dummyjson.com/products')
data = response.json()
product_dict = data
product_list = product_dict['products']

# print(product_list)

open_csv = open('data.csv','w')
csv_obj = csv.writer(open_csv)

for product in product_list:
    print(product)
    csv_obj.writerow([product['title'],product['brand'],product['price'],product['stock']])



open_csv.close()