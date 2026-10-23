# La ficha de producto de la parte PHP mostraba nombre, precio, unidades 
# y disponible. Replica esa salida en Python con una f-string y el formato :.2f para el precio.

name = input('Introduce a name of a product: ')
price = input('Introduce a price: ')
stock = input('Introduce stock: ')
available = input('Is it available?: (yes/no)')

print(f'Product: {name} - price: {price} € - stock: {stock} - available: {available}')
