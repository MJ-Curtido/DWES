catalog = [
	{"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
	{"nombre": "Lápiz", "precio": 0.8, "stock": 0},
	{"nombre": "Mochila", "precio": 18.9, "stock": 3},
]

def get_expensive_product(catalog: list) -> tuple[float, dict]:
	""" En esta función se calcula la media de los precios del catálogo, además de mostrar los que no tienen stock y de devolver el producto más caro """
	no_stock_list = []
	sumatory = 0
	expensive_product = catalog[0]

	for product in catalog:
		if product['stock'] == 0:
			no_stock_list.append(product)
		
		sumatory += product['precio']

		if product['precio'] > expensive_product['precio']:
			expensive_product = product

	print('Product with no stock:')
	for product in no_stock_list:
		print(f'\t- {product['nombre']}')

	average = round(sumatory / len(catalog), 2)

	return average, expensive_product

average, expensive_product = get_expensive_product(catalog)

print('\n\n')

print(f'Average price: {average}')

print('\n\n')

print(f'The most expensive product: {expensive_product['nombre']}')

print('\n\n')

print(f'Help: {help(get_expensive_product)}')
