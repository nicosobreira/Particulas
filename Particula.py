from pyray import *
from random import randint, choice

VELOCIDADES = (-5, -4, 5, 1)


class Particula:
    total = 0

    def __init__(self, index: int, raio: float, centro: Vector2,
                 velocidade: Vector2,
                 cor: Color) -> None:
        self.raio = raio
        self.centro = centro
        
        self.velocidade = velocidade
        self.cor = cor

    def debug(self) -> None:
        draw_text(
            f"Raio = {self.raio}\nCen.x = {self.centro.x}\nCen.y = {self.centro.y}\nVel.x = {self.velocidade.x}\n Vel.y = {self.velocidade.y}",
            5, 5, 14, WHITE
        )
    
    @staticmethod
    def corAleatoria() -> int:
        return randint(0, 255)

    @staticmethod
    def getAceleracao(radius: float, weight: float) -> float:
        return radius // weight

    @classmethod
    def cria_aleatorio(cls, raio_min: float = 10, raio_max: float = 20):
        index = Particula.total
        raio = randint(raio_min, raio_max)    
        # centro = Vector2(randint(WIN_W + raio, WIN_W - raio),
        #                  randint(WIN_H - raio, WIN_H + raio))
        centro = Vector2(get_screen_width() / 2, get_screen_height() / 2)
        velocidade = Vector2(choice((-5, 5)) - cls.getAceleracao(raio, 10),
                             choice((-4, 4)) - cls.getAceleracao(raio, 10))
        cor = Color(cls.corAleatoria(), cls.corAleatoria(), cls.corAleatoria(), 255)

        Particula.total += 1
        return cls(index, raio, centro, velocidade, aceleracao, cor)
    
    def atualiza(self) -> None:
        self.centro.x += self.velocidade.x
        self.centro.y += self.velocidade.y

        if (    self.centro.x > get_screen_width() - self.raio or # Direita
                self.centro.x < self.raio): # Esquerda
            self.velocidade.x *= -1
        if (    self.centro.y < self.raio or # Cima
                self.centro.y > get_screen_height() - self.raio): # Baixo
            self.velocidade.y *= -1

    def desenha(self, escala: float = 2) -> None:
        draw_circle_v(self.centro, self.raio, self.cor)

