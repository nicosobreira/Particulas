from pyray import *

from Particula import Particula
from ParticulaHandler import ParticulaHandler


WIN_W = 640
WIN_H = 360


class Game:
    def __init__(self) -> None:
        init_window(WIN_W, WIN_H, "Particulas")
        set_target_fps(60)

        self.state = True
        
        self.font_size = 14
        
        self.pause = False
        self.pause_text = "Press P to Continue"

        self.debug = False
        self.debug_pos = 0

        self.particulas = ParticulaHandler([Particula.cria_aleatorio()])

    def inputTeclado(self) -> None:
        if is_key_pressed(KEY_Q) or is_key_pressed(KEY_ESCAPE):
            self.state = False
        elif get_key_pressed() == KEY_P:
            self.pause = not self.pause
        elif get_key_pressed() == KEY_B:
            self.debug = not self.debug
    
    def atualizaFrame(self) -> None:
        self.inputTeclado()
        if not self.pause:
            self.particulas.atualizaTodas()

    def desenhaFrame(self) -> None:
        begin_drawing()

        clear_background(BLACK)
        self.particulas.desenhaTodas()
        if self.pause:
            draw_text(self.pause_text,
                      get_screen_width()//2 - measure_text(self.pause_text, self.font_size)//2,
                      get_screen_height() // 2,
                      self.font_size, WHITE)
        if self.debug:
            draw_text("")

        end_drawing()

    def Loop(self) -> None:
        while self.state:
            self.inputTeclado()
            self.atualizaFrame()
            self.desenhaFrame()


if __name__ == "__main__":
    game = Game()
    game.Loop()
