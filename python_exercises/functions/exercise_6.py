#Escribe maximo(*numeros), que devuelva el mayor de los argumentos recibidos y lance ValueError("No ha llegado ningún número") si la llaman sin argumentos.
#Comprueba después que maximo(*[3, 1, 4]) se comporta igual que maximo(3, 1, 4) y explica por qué.

def maximo(*numeros):
	try:
		if len(numeros) == 0:
			raise ValueError("There is no value.")

		max_num = int(numeros[0])

		for element in numeros:
			if not isinstance(element, int):
				raise TypeError("Every elements must be integers.")
			
			if element > max_num:
				max_num = element
		
		return max_num
	except ValueError as e:
		print(e)
	except TypeError as e:
			print(e)

# Se comportan igual porque el asterisco extrae los elementos por separado
if __name__ == '__main__':
	print(maximo(7, 8, "podsafj", 65, 4567, 6, 6, 6))
	print(maximo(*[3, 1, 4]))
	print(maximo(3, 1, 4))
