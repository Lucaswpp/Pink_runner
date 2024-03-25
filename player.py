import pygame as pyg
from constante import *


class Player:

    def __init__(self,pos):

        self.sprite_list = self.load_assets(STATES_PLAYER)
        self.state = "Run"
        self.sprites = self.sprite_list[self.state]
        self.pos = self.sprites[0].get_rect(topleft=pos)
        self.index_frame = 0
        self.delay = SPEED_ANIMATION_FRAME
        self.cont = 0
        self.mask = pyg.mask.from_surface(self.sprites[0])
        


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
        self.animate_player(tela)

    
    def animate_player(self,tela):

        tot_frames = len(self.sprites)

        if tot_frames * self.delay <= self.index_frame:
            self.cont = 0

        self.index_frame = (int(self.cont/self.delay)) % tot_frames
        print(self.index_frame)
        frame_surface = self.sprites[self.index_frame]

        tela.blit(frame_surface,self.pos)

        self.cont += 1