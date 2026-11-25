"""Tarifas, excepciones y cálculos del servicio Bicis de la Campiña.

Parte 1 del examen. Este módulo NO debe importar alquiler.py: sus funciones
trabajan con cualquier objeto que tenga .cliente, .tipo, .estacion,
.minutos y .devuelto.
"""

from datetime import date

# --- Constantes del dominio (no las modifiques) ---------------------------

TARIFAS = {             # euros por hora o fracción
    "urbana": 2.5,
    "electrica": 4.0,
    "infantil": 1.5,
}

EXTRAS = {              # euros, una vez por alquiler
    "casco": 1.5,
    "candado": 1.0,
    "sillita": 2.0,
}

DESCUENTO_ABONADO = 0.20            # 20 % sobre el total
INICIO_FERIA = date(2027, 5, 8)     # Feria del Caballo: recargo
FIN_FERIA = date(2027, 5, 15)
RECARGO_FERIA = 2.0                 # euros


# --- 3.1 Excepciones propias ------------------------------------------------
# Completa las tres hijas (apartado 3.1). RegistroInvalidoError
# también va en este módulo (apartado 7.1).

class ErrorAlquiler(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class TipoInvalidoError(ErrorAlquiler):
    def __init__(self, tipo):
        text = f'| TipoInvalidoError | {tipo} | el tipo no está en {", ".join(TARIFAS.keys())} | Tipo de bici no reconocido: {tipo} |'
        super().__init__(text)


class ExtraInvalidoError(ErrorAlquiler):
    def __init__(self, extra):
        self.extra = extra
        text = f'| ExtraInvalidoError | {self.extra} | el extra no está en {", ".join(EXTRAS.keys())} | Extra no disponible: {self.extra}. Disponibles: {", ".join(EXTRAS.keys())} |'
        super().__init__(text)


class DuracionInvalidaError(ErrorAlquiler):
    def __init__(self, minutos):
        text = f'| DuracionInvalidaError | {minutos} | una duración es cero o negativa | La duración debe ser positiva: {minutos} |'
        super().__init__(text)


# --- 3.2 Duraciones -----------------------------------------------------------

def horas_minutos(minutos:int) -> tuple[int, int]:
    if minutos < 0:
        raise DuracionInvalidaError(minutos)
    
    temp_hours = minutos // 60
    temp_minutes = minutos - (temp_hours * 60)

    return (temp_hours, temp_minutes)



def formato_duracion(minutos:int) -> str:
    temp_hours, temp_minutes = horas_minutos(minutos)

    return f'{temp_hours}:{str(temp_minutes).zfill(2)}'


def horas_facturables(minutos:int) -> int:
    temp_hours, temp_minutes = horas_minutos(minutos)

    return temp_hours if temp_minutes == 0 else temp_hours + 1


# --- 3.3 Precio ------------------------------------------------------------------

def precio_alquiler(tipo:str, minutos:int, *extras:str, abonado:bool=False, fecha:date|None=None):
    if tipo not in TARIFAS:
        raise TipoInvalidoError(tipo)
    
    base_price = TARIFAS[tipo] * horas_facturables(minutos)

    for extra in extras:
        if extra not in EXTRAS:
            raise ExtraInvalidoError(extra)
        base_price += EXTRAS[extra]
    
    if INICIO_FERIA <= date.today() <= FIN_FERIA:
        base_price += RECARGO_FERIA
    
    if abonado:
        base_price = base_price - (base_price * DESCUENTO_ABONADO)
    
    return round(base_price, 2)


# --- 3.4 Resumen y ranking ----------------------------------------------------------

def resumen(alquileres, tipo:str|None=None):
    total = len(alquileres)
    times = [alquiler.minutos for alquiler in alquileres]
    devueltos = len(times)
    media_min = round(sum(times) / len(times))
    maximo_min = max(times)
    
    return (total, devueltos, media_min, maximo_min)


def ranking(alquileres, tipo:str|None=None, top:int|None=None):
    result = []

    alquileres_filtered = list(filter(lambda alquiler: alquiler.devuelto, alquileres))

    for i, alquiler in enumerate(alquileres_filtered, 1):
        if top and i > top:
            break

        temp_rank = {}
        temp_rank['pos'] = i
        temp_rank['cliente'] = alquiler.cliente
        temp_rank['estacion'] = alquiler.estacion
        temp_rank['duracion'] = formato_duracion(alquiler.minutos)

        result.append(temp_rank)
    
    return result
