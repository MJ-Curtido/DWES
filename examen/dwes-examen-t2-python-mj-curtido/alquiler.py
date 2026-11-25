"""Alquileres del servicio Bicis de la Campiña.

Parte 2 del examen. Importa de tarifas.py lo que necesites.
"""

from tarifas import TARIFAS, formato_duracion, DESCUENTO_ABONADO, DuracionInvalidaError, TipoInvalidoError

class Alquiler():
    """Un alquiler de bici, en curso (minutos None) o ya devuelto."""

    def __init__(self, cliente:str, tipo:str, estacion:str, minutos:int|None=None):
        self._cliente = cliente

        if tipo not in TARIFAS:
            raise TipoInvalidoError(tipo)
        self._tipo = tipo

        self._estacion = estacion

        if minutos <= 0:
            raise DuracionInvalidaError(minutos)    
        self._minutos = minutos
    
    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, value:str):
        self._cliente = value
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, value:str):
        if value in TARIFAS:
            self._tipo = value
        raise TipoInvalidoError(value)
    
    @property
    def estacion(self):
        return self._estacion
    
    @estacion.setter
    def estacion(self, value:str):
        self._estacion = value
    
    @property
    def minutos(self):
        return self._minutos
    
    @minutos.setter
    def minutos(self, value:int|None):
        if value == None or (isinstance(value, int) and value > 0):
            self._minutos = value
        raise DuracionInvalidaError(value)
    
    @property
    def devuelto(self):
        return True if self.minutos else False
    
    @staticmethod
    def es_tipo_valido(value:str):
        return value in TARIFAS

    @classmethod
    def desde_registro(cls, registro):
        minutos = None
        if registro['minutos']:
            minutos = registro['minutos']
        return cls(registro['cliente'], registro['bici'], registro['estacion'], minutos)

    def importe(self):
        if self.devuelto:
            return TARIFAS[self.tipo]
        
        return 0.0
    
    def __str__(self):
        return f'{self.cliente} [{self.tipo}] — {self.estacion} ({'en curso' if not self.devuelto else formato_duracion(self.minutos)})'

class AlquilerAbonado(Alquiler):
    def __init__(self, cliente:str, tipo:str, estacion:str, minutos:int|None=None, abonado:bool=False):
        super().__init__(cliente, tipo, estacion, minutos)
        self._abonado = abonado
    
    @property
    def abonado(self):
        return self._abonado
    
    @abonado.setter
    def abonado(self, value:bool):
        self._abonado = value
    
    def importe(self):
        if self.devuelto:
            price = TARIFAS[self.tipo]
            return price - (price * DESCUENTO_ABONADO)
        
        return 0.0

    @classmethod
    def desde_registro(cls, registro):
        minutos = None
        abonado = False
        if registro['minutos']:
            minutos = registro['minutos']
        if registro['abonado']:
            abonado = registro['abonado']
        return cls(registro['cliente'], registro['bici'], registro['estacion'], minutos, abonado)

    def __str__(self):
        return f'{self.cliente} [{self.tipo}{', abonado' if self.abonado else ''}] — {self.estacion} ({'en curso' if not self.devuelto else formato_duracion(self.minutos)})'


def recaudacion(alquileres):
    result = 0

    for alquiler in alquileres:
        result += alquiler.importe()

    return round(result, 2)
