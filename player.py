import pygame as pyg
from constante import *


class Player:

    def __init__(self,sprites,pos):

        self.imgs = self.load_assets(sprites)
        self.state = "Run"
        self.img = self.imgs[self.state]
        self.pos = pos


    def load_assets(self,list_spritesheet):
        list_sprite = {}
        list_temp = []
        
        for state in list_spritesheet:

            img_path = f"{IMG_PATH}/{state}.png"
            img = pyg.image.load(img_path).convert_alpha()
            length_img = img.get_width() // TILESIZE

            for i in range(0,length_img):
                surface_img = pyg.Surface((TILESIZE,TILESIZE),pyg.SRCALPHA,32)
                surface_img.blit(img,(0,0),(TILESIZE * i, 0,TILESIZE,TILESIZE))
                list_temp.append(pyg.transform.scale2x(surface_img))       


            list_sprite[state] = list_temp[:]
                
        return list_sprite
    
    def draw(self,tela):

        tela.blit(self.img[1],self.pos)