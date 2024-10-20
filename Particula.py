from pyray import *
from random import randint, choice

from opcoes import *

VELOCIDADES = (-1, 1)


def corAleatoria() -> int:
    return randint(0, 255)

class Particula:
    def __init__(self, centro: Vector2, velocidade: Vector2, raio: float, cor: Color) -> None:
        self.centro = centro
        self.velocidade = velocidade
        self.raio = raio
        self.cor = cor

    @classmethod
    def cria_aleatorio(cls, raio_min: float = 10, raio_max: float = 20):
        raio = randint(raio_min, raio_max)    
        # centro = Vector2(randint(WIN_W + raio, WIN_W - raio),
        #                  randint(WIN_H - raio, WIN_H + raio))
        centro = Vector2(WIN_W / 2, WIN_H / 2)
        velocidade = Vector2(choice(VELOCIDADES), choice(VELOCIDADES))
        cor = Color(corAleatoria(), corAleatoria(), corAleatoria(), 255)

        return cls(centro, velocidade, raio, cor)
    
    def atualiza(self) -> None:
        ...

    def desenha(self, escala: float = 2) -> None:
        draw_circle_v(vector2_multiply(self.centro, Vector2(escala, escala)),
                      self.raio, self.cor)

