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
		self._stock = units

	def vender(self, unidades: int):
		if unidades > self.stock:
			raise ValueError(f"No enough stock of {self.nombre}")
		self.stock -= unidades

	def __str__(self):
		return f"{self.nombre} - {self.precio} € (Stock: {self.stock} units)"

	def __repr__(self):
		return f"Producto('{self.nombre}', {self.precio}, {self.stock})"

if __name__ == '__main__':
	try:
		product1 = Producto("Keyboard", 25.50, 10)
		product2 = Producto("Mouse", 15.00, 2)

		product1.vender(3)
		print(f"Product: {product1}")

		product2.vender(5) # Provoca un error, ya que no hay stock suficiente
		print(f"Product: {product2}")
	except ValueError as e:
		print(e)
