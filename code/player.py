import pygame
from settings import *

from import_files import import_images


class Player(pygame.sprite.Sprite):
    def __init__(self,pos) -> None:
        super().__init__()

        # self.image = pygame.Surface((64,64))
        # self.image.fill('red')

     
        self.direction=pygame.Vector2()
        self.speed= PLAYER_VEL

        self.player_is_moving=False

        # FOR ANIMATION
        self.get_frames()

        self.frame_index=0

        # PLAYER STATUS
        self.status='front_idle'
        self.left=False
        self.front=True
        self.on_x = False
        self.on_y=True

        self.image=self.frames[self.status][self.frame_index]
        
        self.rect = self.image.get_rect(topleft=pos)

        
    def move_player(self,key_pressed):
        #keys=pygame.key.get_pressed()

        if key_pressed=="d":
            self.direction.x= 1
            self.direction.y=0
            self.player_is_moving=True
            self.status='walk_right'

            self.left = False

            self.on_y =False
            self.on_x=True


        elif key_pressed=="a":
            self.direction.x=-1
            self.direction.y=0
            self.player_is_moving=True
            self.status = 'walk_left'

            self.left = True

            self.on_y =False
            self.on_x=True

        elif key_pressed=="w":
            self.direction.y=-1
            self.direction.x=0
            self.player_is_moving=True
            self.status = 'walk_back'

            self.front = False
            self.on_y=True
            self.on_x= False

        elif key_pressed=="s":
            self.direction.y=1
            self.direction.x=0
            self.player_is_moving=True
            self.status='walk_front'

            self.front=True
            self.on_y = True
            self.on_x=False
        else:
            self.direction.y=0
            self.direction.x=0
            self.player_is_moving=False

            if self.left and self.on_x:
                self.status='left_idle'
            elif not self.left and self.on_x:
                self.status='right_idle'
            elif self.front and self.on_y:
                self.status = 'front_idle'
            elif not self.front and self.on_y:
                self.status='back_idle'


        return False
    

    def get_frames(self):
        self.frames={'walk_right':[],'walk_front':[],'walk_left':[],'walk_back':[],'right_idle':[],'front_idle':[],'back_idle':[],'left_idle':[]}
        path='./graphics/character/'

        for folder in self.frames.keys():
            self.frames[folder] = import_images(path+folder)
        
        

    def animate(self):
        self.frame_index+=0.5

        if self.frame_index>=len(self.frames[self.status]): self.frame_index=0

        self.image=self.frames[self.status][int(self.frame_index)]


    def update(self,key_pressed) -> None:
        self.animate()
        
        f=self.move_player(key_pressed)
        return f
       
        

