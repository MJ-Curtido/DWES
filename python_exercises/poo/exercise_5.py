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

	def precio_con_iva(self):
		return round(self.precio * 1.21, 2)

	def __str__(self):
		return f"{self.nombre} - {self.precio} € (Stock: {self.stock} units)"

	def __repr__(self):
		return f"Producto('{self.nombre}', {self.precio}, {self.stock})"

""" Clase ProductoRebajado que hereda de Producto con descuento sobre el precio """
class ProductoRebajado(Producto):
	def __init__(self, name: str, price: float, stock: int, discount: float):
		super().__init__(name, price, stock)
		self._descuento = discount

	@property
	def descuento(self):
		return self._descuento
	@descuento.setter
	def descuento(self, discount: float):
		self._descuento = discount

	@property
	def precio(self):
		return round(self._precio * (1 - self.descuento / 100), 2)

	def __str__(self):
		return f"{self.nombre} - {self.precio} € ({self.descuento}% discount) (Stock: {self.stock} units)"

	def __repr__(self):
		return f"ProductoRebajado('{self.nombre}', {self.precio}, {self.stock}, {self.descuento})"

""" Clase Formacion con nombre y precio """
class Formacion:
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

	def precio_con_iva(self):
		return round(self.precio * 1.21, 2)

	def __str__(self):
		return f"{self.nombre} - {self.precio} €"

	def __repr__(self):
		return f"Formacion('{self.nombre}', {self.precio})"

""" Clase ServicioPremium sin el método precio_con_iva """
class ServicioPremium:
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
			return f"ServicioPremium('{self.nombre}', {self.precio})"

""" Función para calcular el total con IVA """
def total_con_iva(products: list):
	total = 0

	for element in products:
		total += element.precio_con_iva()

	return round(total, 2)

if __name__ == '__main__':
	product = Producto("Keyboard", 25.5, 10)
	product_sale = ProductoRebajado("Mouse", 15, 5, 20)
	training = Formacion("Python Course", 80)

	products = [product, product_sale, training]

	print(f"Total: {total_con_iva(products)} €")

	""" Añado el servicio premium para comprobar el error """
	premium_service = ServicioPremium("Chirigota", 50)
	products.append(premium_service)

	try:
		print(f"Total: {total_con_iva(products)} €")
	except AttributeError as e:
		print(e)
