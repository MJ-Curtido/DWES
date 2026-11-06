def aplicar_descuento(precio, porcentaje):
	try:
		if not 0 <= porcentaje <= 100:
			raise ValueError("El porcentaje debe estar entre 0 y 100")

		if precio <= 0:
			raise ValueError("El precio debe de ser positivo")
		
		return precio * (1 - porcentaje / 100)
	except ValueError as e:
		print(f'ValueError: {e}')
	except Exception as e:
		print(f'Error: {e}')

""" Ejemplos de ValueError por precio y por porcentaje """
print(f'Precio: {aplicar_descuento(7, 70)} €')
print(f'Precio: {aplicar_descuento(-13, 100)} €')
print(f'Precio: {aplicar_descuento(7, 107)} €')
