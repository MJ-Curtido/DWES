"""Programa principal del servicio Bicis de la Campiña.

Parte 3 del examen. Se ejecuta con: python app.py
"""

# Importa aquí lo que necesites.
from alquiler import Alquiler, AlquilerAbonado, recaudacion
from tarifas import ranking, TARIFAS, EXTRAS

# --- Datos (no los modifiques) ----------------------------------------------

REGISTROS = [
    {"cliente": "Nerea Campos", "bici": "urbana",
     "estacion": "Plaza del Arenal", "minutos": 45},
    {"cliente": "Tomás Herrera", "bici": "electrica",
     "estacion": "Alameda Cristina", "minutos": 125, "abonado": True},
    {"cliente": "Irene Valle", "bici": "urbana",
     "estacion": "Estación de tren"},
    {"cliente": "Pablo Serrano", "bici": "infantil",
     "estacion": "Plaza del Arenal", "minutos": 30, "abonado": False},
    {"cliente": "Sara Rubio", "bici": "electrica",
     "estacion": "Plaza del Arenal", "minutos": 61},
    {"cliente": "Diego Lozano", "bici": "urbana",
     "estacion": "Alameda Cristina", "minutos": 190},
    {"cliente": "Celia Navarro", "bici": "infantil",
     "estacion": "Estación de tren", "minutos": 75},
    {"cliente": "Mario Castro", "bici": "electrica",
     "estacion": "Estación de tren", "abonado": False},
    {"cliente": "Rubén Ortega", "bici": "urbana",
     "estacion": "Plaza del Arenal", "minutos": 120, "abonado": True},
    {"cliente": "Lorena Díaz", "bici": "electrica",
     "estacion": "Alameda Cristina", "minutos": 240, "abonado": True},
]

# Registros recibidos de otra estación: algunos vienen mal (parte 4).
REGISTROS_IMPORTADOS = [
    {"cliente": "Lucía Peña", "bici": "urbana",
     "estacion": "Plaza del Arenal", "minutos": 50},
    {"cliente": "Marcos Díaz", "bici": "tandem",
     "estacion": "Alameda Cristina", "minutos": 30},
    {"cliente": "Nuria Gil", "bici": "electrica",
     "estacion": "Estación de tren", "minutos": 95, "abonado": True},
    {"cliente": "Óscar León", "bici": "infantil",
     "estacion": "Plaza del Arenal", "minutos": 0},
    {"cliente": "Paula Ríos", "bici": "urbana", "minutos": 20},
    {"cliente": "Raúl Vera", "bici": "electrica",
     "estacion": "Alameda Cristina"},
]

RUTA_INFORME = "informe.json"


# --- 5.1 Carga y persistencia -def ranking(alquileres, tipo:str|None=None, top:int|None=None):------------------------------------------------

def cargar_alquileres(registros):
    result = []
    for registro in registros:
        if registros['abonado']:
            result.append(AlquilerAbonado(registro['cliente'], registro['bici'], registro['estacion'], registro['minutos'], registro['abonado']))
        else:
            result.append(Alquiler(registro['cliente'], registro['bici'], registro['estacion'], registro['minutos']))
    
    return result

def guardar_informe(alquileres, ruta):
    with open(ruta, 'w', encoding="utf-8") as file:
        content = {}
        content['recaudacion'] = recaudacion(alquileres)
        content['ranking'] = ranking(alquileres)

        json.dump(content, file, indent=2, ensure_ascii=False)


# --- 5.2 Entrada por teclado ------------------------------------------------------
# pedir_entero ya está hecha: úsala, no la cambies.

def pedir_entero(mensaje, minimo, maximo):
    while True:
        texto = input(f"{mensaje} ({minimo}-{maximo}): ")
        try:
            valor = int(texto)
        except ValueError:
            print("Eso no es un número entero.")
            continue
        if minimo <= valor <= maximo:
            return valor
        print(f"Debe estar entre {minimo} y {maximo}.")


def pedir_tipo():
    while True:
        tipo = input(f'Tipo ({', '.join(TARIFAS.keys())} o Intro para todos): ')
        tipo = tipo.strip().lower()
        if not Alquiler.es_tipo_valido(tipo):
            print('Tipo no reconocido.')
            continue
        return tipo if tipo else None

def pedir_extras():
    result = []
    for key, value in EXTRAS.items():
        print('Estras:')
        print(f'- {key}: {value} €')
    while True:
        extra = input(f'Extras o Intro para terminar): ')
        extra = extra.strip().lower()
        if not extra:
            break

        if extra not in EXTRAS:
            print('extra no reconocido.')
            continue

        result.append(extra)
    
    return result

def pedir_abonado():
    while True:
        result = input('¿Abonado? (s/n): ')

        if result == 's':
            return True
        else:
            if result == 'n':
                return False
            else:
                print('Respuesta incorrecta')

def pedir_fecha():
    result = input('Fecha AAAA-MM-DD: ')

    try:
        fecha = date.fromisoformat(result)

        return fecha
    except:
        return None
        print('Fecha incorrecta')

def ranking_option(alquileres):
    tipo = pedir_tipo()
    clasificacion = ranking(alquileres, tipo)

    for element in clasificacion:
        print(f'{element['pos']}. {element['cliente']} — {element['duracion']} — {element['estacion']}')

def precio_option():
    tipo = pedir_tipo()
    minutos = pedir_entero("Minutos", 1, 1440)
    extras = pedir_extras()
    abonado = pedir_abonado()
    fecha = pedir_fecha()

    print(f'Precio: {round(precio_alquiler(tipo, minutos, *extras, abonado, fecha), 2)} €')

def informe_opcion(alquileres):
    guardar_informe(alquileres, RUTA_INFORME)

    print('Informe guardado')

# --- 5.3 Menú ------------------------------------------------------------------------

def main():
    alquileres = cargar_alquileres(REGISTROS)

    while True:
        print('=== BICIS DE LA CAMPIÑA ===')
        print('1) Ranking de alquileres')
        print('2) Calcular precio')
        print('3) Guardar informe')
        print('0) Salir)')

        pedir_entero("Opción", 0, 3)

        match option:
            case 1:
                ranking_option(alquileres)
            case 2:
                precio_option()
            case 3:
                informe_opcion(alquileres)
            case 0:
                print('Hasta luego!')
                break
            case _:
                print('Opción no válida')


# --- 7.1 Para nota: importación de registros -----------------------------------

def importar_registros(registros):
    raise NotImplementedError


if __name__ == "__main__":
    main()
