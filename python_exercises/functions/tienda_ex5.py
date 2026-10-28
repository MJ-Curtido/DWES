from catalogo_ex5 import producto_mas_caro

def main():
    catalogo = [
        {"nombre": "Cuaderno", "precio": 2.5, "stock": 12},
        {"nombre": "Mochila", "precio": 18.9, "stock": 3},
    ]

    caro = producto_mas_caro(catalogo)
    print(f"El más caro es {caro['nombre']}: {caro['precio']:.2f} €")

    sorted_catalog = sorted(catalogo, key=lambda product: product['precio'])

    print(sorted_catalog)

if __name__ == '__main__':
    main()
