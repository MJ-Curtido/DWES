#Añade validación con raise a aplicar_descuento: además del porcentaje, el precio debe ser positivo.
#Escribe después las llamadas que provoquen cada error y captúralas por separado.
def aplicar_descuento(precio, porcentaje):
	if not 0 <= porcentaje <= 100:
		raise ValueError("El porcentaje debe estar entre 0 y 100")

	if precio <= 0:
		raise ValueError("El precio debe de ser positivo")
	return precio * (1 - porcentaje / 100)

try:
	print(f'Precio: {aplicar_descuento(-13, 100)} €')
except ValueError as e:
	print(f'ValueError: {e}')
except Exception as e:
	print(f'Error: {e}')
