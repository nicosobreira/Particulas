from pyray import *

from opcoes import *
from Particula import Particula
from ParticulaHandler import ParticulaHandler


class Game:
    def __init__(self) -> None:
        
        init_window(WIN_W, WIN_H, "Particulas")
        set_target_fps(60)

        self.state = True
        self.particulas = ParticulaHandler([Particula.cria_aleatorio()])

    def inputTeclado(self) -> None:
        if is_key_pressed(KEY_Q) or is_key_pressed(KEY_ESCAPE):
            self.state = False
    
    def atualizaFrame(self) -> None:
        self.inputTeclado()

    def desenhaFrame(self) -> None:
        begin_drawing()

        clear_background(BLACK)
        self.particulas.desenhaTodas()

        end_drawing()

    def Loop(self) -> None:
        while self.state:
            self.atualizaFrame()
            self.desenhaFrame()


if __name__ == "__main__":
    game = Game()
    game.Loop()
