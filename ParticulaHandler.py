from pyray import *


class ParticulaHandler:
    def __init__(self, particulas: list) -> None:
        self.particulas = particulas

    def debugAll(self) -> None:
        draw_text(f"")

    def atualizaTodas(self) -> None:
        for particula in self.particulas:
            particula.atualiza()

    def desenhaTodas(self) -> None:
        for particula in self.particulas:
            particula.desenha()
