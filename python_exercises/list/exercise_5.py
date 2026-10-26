dicPrices = {"Cuaderno": 2.5, "Lápiz": 0.8, "Mochila": 18.9}
order = (('Cuaderno', 7), ('Lápiz', 5), ('Mochila', 1))
total = 0

for item in order:
	total += dicPrices[item[0]] * item[1]

print(f'Total: {total}')
