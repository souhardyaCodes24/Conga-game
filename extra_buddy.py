import pygame
from settings import *

from import_files import import_images


class Buddy(pygame.sprite.Sprite):
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

        
    def move_player(self):
        keys=pygame.key.get_pressed()

        # if keys[pygame.K_d]:
        #     self.direction.x= 1
        #     self.player_is_moving=True
        #     self.status='walk_right'

        #     self.left = False

        #     self.on_y =False
        #     self.on_x=True


        # elif keys[pygame.K_a]:
        #     self.direction.x=-1
        #     self.player_is_moving=True
        #     self.status = 'walk_left'

        #     self.left = True

        #     self.on_y =False
        #     self.on_x=True

        # elif keys[pygame.K_w]:
        #     self.direction.y=-1
        #     self.player_is_moving=True
        #     self.status = 'walk_back'

        #     self.front = False
        #     self.on_y=True
        #     self.on_x= False

        # elif keys[pygame.K_s]:
        #     self.direction.y=1
        #     self.player_is_moving=True
        #     self.status='walk_front'

        #     self.front=True
        #     self.on_y = True
        #     self.on_x=False
        # else:
        #     self.direction.y=0
        #     self.direction.x=0
        #     self.player_is_moving=False

        #     if self.left and self.on_x:
        #         self.status='left_idle'
        #     elif not self.left and self.on_x:
        #         self.status='right_idle'
        #     elif self.front and self.on_y:
        #         self.status = 'front_idle'
        #     elif not self.front and self.on_y:
        #         self.status='back_idle'
    

    def get_frames(self):
        self.frames={'walk_right':[],'walk_front':[],'walk_left':[],'walk_back':[],'right_idle':[],'front_idle':[],'back_idle':[],'left_idle':[]}
        path='./graphics/character2/'

        for folder in self.frames.keys():
            self.frames[folder] = import_images(path+folder)
        
        

    def animate(self):
        self.frame_index+=0.5

        if self.frame_index>=len(self.frames[self.status]): self.frame_index=0

        self.image=self.frames[self.status][int(self.frame_index)]


    def update(self) -> None:
        self.animate()
        
        self.move_player()
       
        

