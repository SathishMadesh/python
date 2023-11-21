import requests
import json

response = requests.get('https://dummyjson.com/products')
data = response.json()['products']

fp = open('data.json','w')
new_list = []

for product in data:
    new_list.append({"Name":product['title'],"Brand":product['brand'],"Price":product['price'],"Stock":product['stock']})

print(new_list)
json.dump(new_list,fp)

fp.close()