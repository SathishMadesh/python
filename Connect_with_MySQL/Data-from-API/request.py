import requests

response = requests.get('https://dummyjson.com/products')
product_dict = response.json()
product_list = product_dict['products']
data = []

for product in product_list:
    data.append((product['id'],product['title'],product['price'],product['rating'],product['stock']))

print(data)