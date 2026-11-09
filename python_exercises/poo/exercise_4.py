""" Clase Producto con nombre, precio y stock """
class Producto:
	def __init__(self, name: str, price: float, stock: int):
		self._nombre = name
		self._precio = price
		self._stock = stock

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

	@property
	def stock(self):
		return self._stock
	@stock.setter
	def stock(self, units: int):
		if units < 0:
			raise ValueError("Stock can't be negative")
		self._stock = units

	@property
	def total(self):
		return round(self.precio * self.stock, 2)

	@classmethod
	def desde_fila(cls, element: str):
		name, price, stock = element.split(",")
		return cls(name, float(price), int(stock))

	def vender(self, unidades: int):
		if unidades > self.stock:
			raise ValueError(f"No enough stock of {self.nombre}")
		self.stock -= unidades

	def __str__(self):
		return f"{self.nombre} - {self.precio} € (Stock: {self.stock} units)"

	def __repr__(self):
		return f"Producto('{self.nombre}', {self.precio}, {self.stock})"

if __name__ == '__main__':
	product = Producto.desde_fila("Mochila, 18.9, 3")

	print(f"Product: {product}")
	print(f"Total: {product.total} €")
	print(f"Stock before change: {product.stock} units")

	try:
		product.stock = -5
	except ValueError as e:
		print(e)

	print(f"Stock after change: {product.stock} units")
