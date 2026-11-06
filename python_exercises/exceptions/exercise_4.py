catalogo = [
	{"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
	{"nombre": "Lápiz", "precio": 0.8, "stock": 0},
	{"nombre": "Mochila", "precio": 18.9, "stock": 3},
]

def buscar_producto(catalogo, nombre):
	try:
		product = None

		for element in catalogo:
			if element['nombre'] == nombre:
				product = element

		if product:
			return product
		else:
			raise ValueError("Product not found.")
	except ValueError as e:
		print(e)
	except Exception as e:
		print(e)
	
print(buscar_producto(catalogo, 'Cuaderno'))
print(buscar_producto(catalogo, 'prueba'))
