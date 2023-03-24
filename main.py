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
        self.elementos = list[Elemento] = []
        nombre: str = ""
        self._id = self.__class__.contador
        self.__class__.contador += 1

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

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto
