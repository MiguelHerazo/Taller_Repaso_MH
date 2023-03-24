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
    def __init__(self):
        self.elementos = list[Elemento] = []
        nombre: str = ""

