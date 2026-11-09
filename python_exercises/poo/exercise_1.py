""" Clase Producto con nombre y precio """
class Producto:
	def __init__(self, name: str, price: float):
		self._nombre = name
		self._precio = price

	@property
	def nombre(self):
		return self._nombre
	@nombre.setter
	def nombre(self, name: str):
		self._nombre = name

	@property
	def precio(self):
		return round(self._precio, 2)
	@precio.setter
	def precio(self, price: float):
		self._precio = price

	def __str__(self):
		return f"{self.nombre} - {self.precio} €"

	def __repr__(self):
		return f"Producto('{self.nombre}', {self.precio})"

""" Clase LineaPedido con producto (objeto de la clase anterior) y unidades """
class LineaPedido:
	def __init__(self, producto: Producto, unidades: int):
		self._producto = producto
		self._unidades = unidades

	@property
	def producto(self):
		return self._producto
	@producto.setter
	def producto(self, product: Producto):
		self._producto = product

	@property
	def unidades(self):
		return self._unidades
	@unidades.setter
	def unidades(self, units: int):
		self._unidades = units

	def subtotal(self):
		return self.producto.precio * self.unidades

	""" Creo el __str__ mostrando la información de la línea de pedido """
	def __str__(self):
		return f"{self.producto.nombre} x {self.unidades} units = {self.subtotal()} €"

	def __repr__(self):
		return f"LineaPedido({repr(self.producto)}, {self.unidades})"

if __name__ == '__main__':
	product1 = Producto("Keyboard", 25.5)
	product2 = Producto("Mouse", 15)
	product3 = Producto("Screen", 150)

	line1 = LineaPedido(product1, 2)
	line2 = LineaPedido(product2, 1)
	line3 = LineaPedido(product3, 1)

	order = [line1, line2, line3]
	total = 0

	for line in order:
		total += line.subtotal()

	print(f"Order total: {total} €")

	# Usos de __str__ para mostrar cuál se usa en cada caso
	print(f"__str__: {product1}")
	print(f"__str__: {line1}")

	# Usos de __repr__ para mostrar cuál se usa en cada caso de las 2 formas
	print(f"__repr__: {repr(product1)}")
	print(f"__repr__: {repr(line1)}")

	# No sé cómo comprobar este, con ipithon se mostraba directamente el __repr__ si no me equivoco, pero por consola no me lo muestra 
	product1
	line1
