from pyray import *


class ParticulaHandler:
    def __init__(self, particulas: list) -> None:
        self.particulas = particulas

    def atualizaTodos(self) -> None:
        ...

    def desenhaTodas(self) -> None:
        for particula in self.particulas:
            particula.desenha()
