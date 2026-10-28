# Ejemplo función lambda para método sorted (ordenar array por alguna propiedad)

productos = [
    {"nombre": "Mochila", "precio": 18.9},
    {"nombre": "Cuaderno", "precio": 2.5},
    {"nombre": "Lápiz", "precio": 0.8},
]

ordenados = sorted(productos, key=lambda p: p["precio"], reverse=True)

print(ordenados)

# Ejemplo map en Python

res = map(lambda x: x*2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

print(list(res))

# Importaciones de librerías

import math
# from math import sqrt# as sqrt_mates # (por si quieres ponerle otro nombre, por ejemplo si difieren con otros o algo así)

print(math.sqrt(16))
# print(sqrt(16))

# Ejemplo de archivo de scripting real

def main():
	print('Se va a ejecutar luego')

if __name__ == '__main__':
	print('Se debe de ejecutar primero')
	main()
