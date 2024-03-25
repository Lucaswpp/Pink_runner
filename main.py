import pygame as pyg
from constante import *
from sys import exit
from time import time
from player import Player
from tile import Tile,Tilemap


class Game:

    def __init__(self):
        self.tela = pyg.display.set_mode((WIDTH,HEIGHT))
        self.jogo_ativo = True
        self.fps = pyg.time.Clock()
        self.delta_time = 0
        self.last_time = time()
        self.player = Player((20,20))
        self.img_background = pyg.transform.smoothscale(pyg.image.load(f"{IMG_PATH}/back.png").convert_alpha(),(WIDTH,HEIGHT))
        self.tile_map = Tilemap("Terra.png")

    

    def draw_game(self):
        self.tela.blit(self.img_background,(0,0))
        self.tile_map.draw_tiles(self.tela)
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