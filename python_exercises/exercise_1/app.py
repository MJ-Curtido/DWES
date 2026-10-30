vinos_jerez = [
    "Sherry Classic",
    "Vino Blanco",
    "Fino SHERRY",
    "Moscatel",
    "ShErry Cream"
]

FILTER_WORD = 'Sherry'

#Requisitos
#1. Define una función que reciba como parámetro una lista de nombres de vinos.
#2. La función debe generar un diccionario en el que:
#3. Las claves sean los nombres de los vinos.
#4. Los valores sean True si el nombre contiene "Sherry" y False en caso contrario.
#5. Utiliza la función incorporada filter() de Python para obtener una segunda lista que contenga únicamente los vinos cuyo nombre incluya "Sherry".
#6. La búsqueda no debe distinguir entre mayúsculas y minúsculas. Por ejemplo, "SHERRY", "sherry" y "ShErry" deben considerarse equivalentes.
#7. La función debe devolver el diccionario y la lista filtrada.
#8. Incluye una docstring que documente el propósito de cada función, sus parámetros y los valores que devuelve.

def filter_list(wines_list: list) -> {'wines_dict': dict, 'wines_filtered': list}:
	""" Esta función requiere de una lista por parámetro y devuelve un diccionario con 2 propiedades:
	 - 'wines_dict': diccionario de la lista pasada por parámetro con valor True o False según si contiene 'Sherry' el nombre
	 - 'wines_filtered': lista pasada por parámetro filtrada para que solo aparezan los que contienen 'Sherry' el nombre """
	wines_dict = {}
	for wine in wines_list:
		wines_dict[wine] = FILTER_WORD.lower() in wine.lower()
	
	""" Utilizo la función filter para hacer un filtrado de la lista que viene por parámetro, esta función requiere de en primer parámetro la función que designa el filtrado y en segundo parámetro la lista a filtrar """
	wines_filtered = filter(lambda w: FILTER_WORD.lower() in w.lower(), wines_list)

	return {'wines_dict': wines_dict, 'wines_filtered': wines_dict}

print(filter_list(vinos_jerez))