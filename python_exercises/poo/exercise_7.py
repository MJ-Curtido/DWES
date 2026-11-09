# from dataclasses import dataclass

# @dataclass
# class Articulo:
# 	nombre: str
# 	precio: float
# 	stock: int = 0

# 	def valor_stock(self):
# 		return round(self.precio * self.stock, 2)

""" Clase Articulo creada manualmente """
class Articulo:
	def __init__(self, nombre: str, precio: float, stock: int = 0):
		self.nombre = nombre
		self.precio = precio
		self.stock = stock

	def valor_stock(self):
		return round(self.precio * self.stock, 2)

	def __repr__(self):
		return f"Articulo(nombre={self.nombre}, precio={self.precio}, stock={self.stock})"

	def __eq__(self, other):
		if isinstance(other, Articulo):
			return (self.nombre, self.precio, self.stock) == (other.nombre, other.precio, other.stock)
		else:
			return False

# Te ahorras de hacer los métodos por defecto (si no quieres modificarlos a tu forma), es mucho más rápido y corto

if __name__ == '__main__':
	article1 = Articulo("Keyboard", 25.5, 10)
	article2 = Articulo("Mouse", 15, 5)
	article3 = Articulo("Keyboard", 25.5, 10)

	print(f"Article 1 == Article 2: {article1 == article2}")
	print(f"Article 1 == Article 3: {article1 == article3}")

	print(f"valor_stock: {article1.valor_stock()} €")
