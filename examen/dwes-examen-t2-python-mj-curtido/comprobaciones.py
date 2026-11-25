"""Comprobaciones del examen. Ejecuta: python comprobaciones.py

Compara la salida con la «Salida esperada» de cada parte del enunciado.
Una parte sin terminar se indica y no impide comprobar las demás.
No hace falta entregar cambios en este fichero.
"""

import json
from datetime import date
from pathlib import Path
from types import SimpleNamespace


def parte1():
    from tarifas import (
        ErrorAlquiler, ExtraInvalidoError, formato_duracion,
        horas_facturables, horas_minutos, precio_alquiler,
    )

    print(horas_minutos(125), formato_duracion(125), formato_duracion(45),
          formato_duracion(600))
    print(horas_facturables(60), horas_facturables(61), horas_facturables(45))
    print(precio_alquiler("urbana", 45))
    print(precio_alquiler("electrica", 125, "casco", "candado"))
    print(precio_alquiler("urbana", 90, "sillita", abonado=True))
    print(precio_alquiler("infantil", 30, fecha=date(2027, 5, 10)))
    print(precio_alquiler("electrica", 61, "casco", abonado=True,
                          fecha=date(2027, 5, 15)))

    try:
        precio_alquiler("tandem", 30)
    except ErrorAlquiler as e:
        print(f"Capturado por la base: {e}")

    try:
        precio_alquiler("urbana", 30, "cesta")
    except ExtraInvalidoError as e:
        print(f"Capturado: {e} (extra={e.extra!r})")


def parte2():
    from alquiler import Alquiler, AlquilerAbonado, recaudacion
    from tarifas import ErrorAlquiler

    nerea = Alquiler("Nerea Campos", "urbana", "Plaza del Arenal", 45)
    print(nerea)
    print(nerea.devuelto, nerea.importe())

    irene = Alquiler.desde_registro(
        {"cliente": "Irene Valle", "bici": "urbana", "estacion": "Estación de tren"})
    print(irene, "| devuelto:", irene.devuelto, "| importe:", irene.importe())

    try:
        Alquiler("Jesús Marín", "tandem", "Plaza del Arenal")
    except ErrorAlquiler as e:
        print(f"Capturado: {e}")

    try:
        nerea.minutos = -5
    except ErrorAlquiler as e:
        print(f"Capturado: {e}")

    tomas = AlquilerAbonado("Tomás Herrera", "electrica", "Alameda Cristina", 125)
    print(tomas)
    print("¿Es un Alquiler?", isinstance(tomas, Alquiler))
    print(tomas.importe())

    mixto = [
        nerea,
        tomas,
        irene,
        Alquiler("Diego Lozano", "urbana", "Alameda Cristina", 190),
    ]
    print(f"Recaudación: {recaudacion(mixto):.2f} €")


def parte3():
    # resumen y ranking son de la parte 1, pero necesitan la lista de
    # alquileres que construye cargar_alquileres (parte 3).
    from app import REGISTROS, cargar_alquileres, guardar_informe
    from tarifas import ranking, resumen

    alquileres = cargar_alquileres(REGISTROS)
    print(len(alquileres), type(alquileres[1]).__name__)
    print(resumen(alquileres))
    print(resumen(alquileres, tipo="electrica"))
    for puesto in ranking(alquileres, tipo="urbana"):
        print(puesto)
    print(ranking(alquileres, top=1))

    guardar_informe(alquileres, "informe.json")
    informe = json.loads(Path("informe.json").read_text(encoding="utf-8"))
    print(informe["recaudacion"], len(informe["ranking"]))


def parte4():
    from app import REGISTROS_IMPORTADOS, importar_registros
    from tarifas import ranking

    alquileres, errores = importar_registros(REGISTROS_IMPORTADOS)
    print(len(alquileres), len(errores), type(alquileres[1]).__name__)
    for error in errores:
        print(f"{error} | causa: {type(error.__cause__).__name__}")

    # Empates en la duración: se ordenan por cliente.
    def alq(cliente, minutos):
        return SimpleNamespace(cliente=cliente, tipo="urbana", estacion="Plaza del Arenal",
                               minutos=minutos, devuelto=True)

    empates = [alq("Yago Fuentes", 60), alq("Carla Pastor", 90),
               alq("Marta Ibáñez", 60), alq("Adrián Gallego", 60)]
    for puesto in ranking(empates):
        print(puesto["pos"], puesto["cliente"], puesto["duracion"])


if __name__ == "__main__":
    for numero, parte in ((1, parte1), (2, parte2), (3, parte3), (4, parte4)):
        print(f"--- Parte {numero} ---")
        try:
            parte()
        except NotImplementedError:
            print(f"(parte {numero} sin terminar: hay funciones sin implementar)")
        except Exception as e:
            print(f"(parte {numero} con errores: {type(e).__name__}: {e})")
