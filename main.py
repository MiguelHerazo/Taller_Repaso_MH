from dataclasses import dataclass
from typing import List

@dataclass

class Elemento:
    nombre : str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False

class Conjunto:
    contador = 0
    def __init__(self):
        self.elementos = List[Elemento] = []
        nombre: str = ""
        self._id = self.__class__.contador
        self.contador += 1

    @property
    def id(self):
        return self._id

    def contiene(self, elemento : Elemento) -> bool:
        for e in self.elementos:
            if e.nombre == elemento.nombre:
                return True
        return False

    def agregar_elemento(self, elemento: Elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elemento in otro_conjunto.elementos:
            self.agregar_elemento(elemento)

    def __add__(self, otro_conjunto: 'Conjunto'):
        resultado = Conjunto([], f"{self.nombre} UNION {otro_conjunto.nombre}")
        resultado.unir(self)
        resultado.unir(otro_conjunto)
        return resultado

    @classmethod
    def intersectar(cls, conjunto1: 'Conjunto', conjunto2: 'Conjunto') -> 'Conjunto':
        elementos_interseccion = [elemento for elemento in conjunto1.elementos if conjunto2.contiene(elemento)]
        nombre_conjunto = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = cls(elementos_interseccion, nombre_conjunto)
        return resultado

    def __str__(self):
        nombres_elementos = ", ".join([elemento.nombre for elemento in self.elementos])
        return f"Conjunto {self.nombre}: ({nombres_elementos})"


