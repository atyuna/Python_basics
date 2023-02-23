
products = [
    {'id': 1, 'name': 't-shirt', 'price': 12.99, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': 22.45, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': 43.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': 14.99, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': 32.50, 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': 150.00, 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

print("Solution for ex 1: Print names of products with price > 25 ")
for i in products:
    if i['price'] > 25:
        print(i['name'])

print ('______________')

print('Solution for ex 2: Print price and name of product if it is on sale')

for i in products:
    # if i['is_on_sale'] is True:
    if i['is_on_sale']:  #Pythonic way (truethiness)
        print(i['name'], i['price'])
print('____________')

print('Solution for ex 3: Print product if it is on sale and no price')

no_sale_price_list = []
for i in products:
    # if i["is_on_sale"] is True and i["sale_price"] is None:
    if i["is_on_sale"] and not i["sale_price"]:         #the same statementas abowe
        no_sale_price_list.append(i["name"])
print(no_sale_price_list)

print('_________')
print("Solution for : Write all product names, that have price > 25 (when price is string) ")
products2 = [
    {'id': 1, 'name': 't-shirt', 'price': '$12.99', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 2, 'name': 'shoes', 'price': '$22.45', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 3, 'name': 'dress-shirt', 'price': '$43.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
    {'id': 4, 'name': 'socks', 'price': '$14.99', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': 7.99},
    {'id': 5, 'name': 'trousers', 'price': '$32.50', 'created_date': '2022-01-01', 'is_on_sale': True, 'sale_price': None},
    {'id': 6, 'name': 'jacket', 'price': '$150.00', 'created_date': '2022-01-01', 'is_on_sale': False, 'sale_price': None},
]

for i in products2:
    # tmp_price = i["price"].replace('$', '')
    tmp_price = i['price'][1:]  # same result as line above
    price = float(tmp_price)
    if price < 25:
        print(i["name"])

