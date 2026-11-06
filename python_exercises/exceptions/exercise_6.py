class ErrorProducto(Exception):
	def __init__(self, text):
		super().__init__(text)

class NombreVacioError(ErrorProducto):
	def __init__(self, text):
		super().__init__(text)

class PrecioInvalidoError(ErrorProducto):
	def __init__(self, text):
		super().__init__(text)

def crear_producto(nombre, precio):
	try:
		if not nombre:
			raise NombreVacioError('Debe de introducir un nombre para crear un producto.')

		if precio <= 0:
				raise PrecioInvalidoError('El precio debe de ser positivo.')

		return {'nombre': nombre, 'precio': precio}
	except ErrorProducto as e:
			print(e)
			print('Excepción propia')
	except Exception as e:
		print('Excepción general')

print(crear_producto('prueba', 7))
print(crear_producto('', 7))
print(crear_producto('prueba', -13))
