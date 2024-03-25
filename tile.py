import pygame as pyg
import csv
from constante import *

class Tile:

    def __init__(self,img,pos):
        self.img  = img
        self.rect = self.img.get_rect(topleft=pos)
        self.mask = pyg.mask.from_surface(self.img)

    def draw(self,tela):

        tela.blit(self.img,self.rect)

class Tilemap:

    def __init__(self,spritesheet):
        self.sprite_tile = pyg.image.load(f"{IMG_PATH}/{spritesheet}").convert_alpha()
        self.tile_size = 16
        self.load_csv()
        self.load_tiles()



    def load_tiles(self):
        self.list_tiles_map = []
        list_temp = []
        for row in range(0,HEIGHT // TILESIZE):
            for colunm in range(0,WIDTH // TILESIZE):
                tile_num = int(self.get_tile_num(row,colunm))

                if tile_num != -1:
                    _row = tile_num // 22
                    _colunm = tile_num - (22 * _row)

                    surface_tile = pyg.Surface((16,16))
                    spritesheet_pos_tile = (16 * _colunm,16 * _row,16,16)
                    surface_tile.blit(self.sprite_tile,(0,0),spritesheet_pos_tile)
                    pos_tile = (colunm * TILESIZE, row * TILESIZE)
                    self.list_tiles_map.append(Tile(pyg.transform.scale2x(surface_tile),pos_tile))
                    


    def load_csv(self):
        self.map = []
        with open("map.csv") as file:
            file = csv.reader(file)
            for row in file:
                self.map.append(row)
    
    

    def draw_tiles(self,tela):
        
        for i in self.list_tiles_map:

            i.draw(tela)
    

    def get_tile_num(self,row,coluna):
        return self.map[row][coluna]