name = input('Introduce a name of a product: ')
price = input('Introduce a price: ')
stock = input('Introduce stock: ')
available = input('Is it available?: (y/n)')

print(f'Product: {name} - price: {price} € - stock: {stock} - {'available' if available == 'y' else 'not available'}')
