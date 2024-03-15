import pygame as pyg
from constante import *
from sys import exit
from time import time
from player import Player


class Game:

    def __init__(self):
        self.tela = pyg.display.set_mode((WIDTH,HEIGHT))
        self.jogo_ativo = True
        self.fps = pyg.time.Clock()
        self.delta_time = 0
        self.last_time = time()
        self.player = Player(STATES_PLAYER,(20,20))
    

    def draw_game(self):
        self.player.draw(self.tela)

    def  update_game(self):
        for evento in pyg.event.get():

            if evento.type == pyg.QUIT:
                exit()
                pyg.quit()
        
        self.update_delta_time()
    
    def update_delta_time(self):

        self.delta_time =  time() - self.last_time

        self.last_time = time()

    def main_loop(self):

        self.fps.tick(FPS_GAME)

        while  self.jogo_ativo:

            self.update_game()
            self.draw_game()

            pyg.display.update()
            self.tela.fill("#000000")
    

if __name__ == "__main__":
    game_object = Game()
    game_object.main_loop()