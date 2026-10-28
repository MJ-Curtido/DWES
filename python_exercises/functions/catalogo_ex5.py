def producto_mas_caro(catalogo):
    mas_caro = catalogo[0]
    for producto in catalogo:
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto
    return mas_caro


def saludar():
    print("Módulo de catálogo cargado")

def productos_agotados(catalogo):
    no_stock_products = []

    for prod in catalogo:
        if prod.stock == 0:
            no_stock_products.append(prod)
    
    return no_stock_products

if __name__ == '__main__':
    saludar()
