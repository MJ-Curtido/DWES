catalog = [
	{"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
	{"nombre": "Lápiz", "precio": 0.8, "stock": 0},
	{"nombre": "Mochila", "precio": 18.9, "stock": 3},
]

no_stock_list = []
sumatory = 0
expensiveProduct = catalog[0]

for product in catalog:
	if product['stock'] == 0:
		no_stock_list.append(product)
	
	sumatory += product['precio']

	if product['precio'] > expensiveProduct['precio']:
		expensiveProduct = product

print('Product with no stock:')
for product in no_stock_list:
	print(f'\t- {product['nombre']}')

print('\n\n')

print(f'Average price: {round(sumatory / len(catalog), 2)}')

print('\n\n')

print(f'The most expensive product: {expensiveProduct['nombre']}')
