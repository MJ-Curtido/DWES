# Ternaria rara para hacer for en una línea
precios = {"manzana": 2, "pera": 4, "piña": 1}

precios_con_iva = {k: v * 1.21 for k, v in precios.items()}

print(precios_con_iva)

# Los conjuntos no tienen orden
conj = {"manzana", "pera", "piña"}

print(conj.pop())
