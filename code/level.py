import pygame
from settings import *
from player import Player

from extra_buddy import Buddy
import random
pygame.init()

font=pygame.font.Font('freesansbold.ttf',30)
class Level:
    def __init__(self,window) -> None:
        # making buddies list
        self.buddies=[]
        self.random_buddies=[pygame.sprite.GroupSingle()]
        self.random_buddies[0].add(Buddy((150,100)))
        self.buddy_collided=False
        self.make_map()
        

        self.score=0

        self.display_suface = window
        self.world_shift=0
        self.shift_x_axis=False
        self.shift_y_axis=False
       
        
        pass

    def check_buddy_collision(self):
        for buddy in self.random_buddies:
            if pygame.Rect.colliderect(self.player.sprite.rect,buddy.sprite.rect) and not self.buddy_collided:
                
              
                self.buddy_collided=True
                self.random_buddies.clear()
                # ADDING RANDOM BUDDY
                self.random_buddies.append(pygame.sprite.GroupSingle())
                if self.random_buddies!=[]:
                    self.random_buddies[0].add(Buddy((random.randrange(100,600),random.randrange(100,700))))
                    
                return True
        return False
        pass

    def make_map(self):
        self.tile= pygame.sprite.Group()
        self.player= pygame.sprite.GroupSingle()

        for row_index,row in enumerate(map):
            for col_index,col in enumerate(row):
                x=col_index  * tile_size
                y  = row_index * tile_size
                if col=="P":
                    self.player.add(Player((x,y)))
                elif col=="X":
                    pass

    def display_score(self):

        text = font.render(f'Score: {self.score}',True,'red','green')
        score_rect=text.get_rect()
        score_rect.center=(90,50)

        self.display_suface.blit(text,score_rect)
        pass

    def add_buddy(self):
        
        
        if  self.check_buddy_collision():
                self.buddies.append(pygame.sprite.GroupSingle())
                self.score+=1
                
        
                # checking if first buddy
                if len(self.buddies)==1:
                    
                    self.buddies[-1].add(Buddy((self.player.sprite.rect.x+MIN_DIST,self.player.sprite.rect.y)))
                    self.buddies[-1].sprite.direction=self.player.sprite.direction
               
                else:
                    
                    second_last_buddy=self.buddies[len(self.buddies)-2]

                    
                    self.buddies[-1].add(Buddy((second_last_buddy.sprite.rect.x+MIN_DIST,second_last_buddy.sprite.rect.y)))
                    self.buddies[-1].sprite.direction=self.player.sprite.direction

                    
                self.buddy_collided=False
                

                pass
        pass

    def move_buddies(self):
        prev=self.player.sprite
        for buddy in self.buddies:
            # making all parameters same
           
           buddy.sprite.status=self.player.sprite.status
           buddy.sprite.speed=self.player.sprite.speed
           buddy.sprite.direction=self.player.sprite.direction
           print(buddy.sprite.status,self.player.sprite.status)

           # BASED ON THE DIRECTION MAKING CHAIN OF BUDDIES

           # IF PREV IS DOWN BUT CURRENT IN LEFT DIRECTION --> move to left then face down
           if prev.direction.y==-1 and buddy.sprite.direction.x==-1:
               buddy.sprite.rect.x+=buddy.sprite.direction.x * buddy.sprite.speed
               buddy.sprite.direction.y==-1
               

               pass
           
            # IF PREV IS DOWN BUT CURRENT IN right DIRECTION --> move to right then face down
           if prev.direction.y==-1 and buddy.sprite.direction.x==1:
               buddy.sprite.rect.x+=buddy.sprite.direction.x * buddy.sprite.speed
               buddy.sprite.direction.y==-1

               pass
           
           # IF PREV IS UP BUT CURRENT IN RIGHT DIRECTION --> move to right then face up
           if prev.direction.y==1 and buddy.sprite.direction.x==1:
               buddy.sprite.rect.x+=buddy.sprite.direction.x * buddy.sprite.speed
               buddy.sprite.direction.y==1

               pass
           
           # IF PREV IS UP BUT CURRENT IN left DIRECTION --> move to left then face up
           if prev.direction.y==-1 and buddy.sprite.direction.x==-1:
               buddy.sprite.rect.x+=buddy.sprite.direction.x * buddy.sprite.speed
               buddy.sprite.direction.y==1

               pass
           
           # IF PREV AND CURRENT ARE UP
           if prev.direction.y==-1 and buddy.sprite.direction.y==-1:
               buddy.sprite.rect.y=prev.rect.y + MIN_DIST
               buddy.sprite.rect.x=prev.rect.x
               
               
               

           # IF PREV AND CURRENT ARE DOWN
           if prev.direction.y==1 and buddy.sprite.direction.y==1:
               buddy.sprite.rect.y=prev.rect.y -MIN_DIST
               buddy.sprite.rect.x=prev.rect.x
               
               

            # IF PREV AND CURRENT ARE LEFT
           if prev.direction.x==-1 and buddy.sprite.direction.x==-1:
               buddy.sprite.rect.x=prev.rect.x + MIN_DIST
               buddy.sprite.rect.y=prev.rect.y
               
               
           # IF PREV AND CURRENT ARE RIGHT
           if prev.direction.x==1 and buddy.sprite.direction.x==1:
               buddy.sprite.rect.x=prev.rect.x -MIN_DIST
               buddy.sprite.rect.y=prev.rect.y
               
               




          

           prev=buddy.sprite
        pass

    def move_buddies_2(self):
        prev=self.player.sprite
        for buddy in self.buddies:
            buddy.rect.x=prev.rect.x
            
            pass
        pass

   



    def player_moving(self):
        player=self.player.sprite

        if player.direction.y==-1:
            player.rect.y-=MOVE_SQUARE
            pass
        elif player.direction.y==1:
            player.rect.y+=MOVE_SQUARE
            pass
        elif player.direction.x==-1:
            player.rect.x-=MOVE_SQUARE
            pass
        elif player.direction.x==1:
            player.rect.x+=MOVE_SQUARE
            pass
        player.rect.y+=player.direction.y * player.speed
        player.rect.x+=player.direction.x * player.speed
   

        pass
    

    def check_if_collided(self):
        for buddy in self.random_buddies:
            for buddy1 in self.buddies:
                if pygame.Rect.colliderect(buddy.sprite.rect,buddy1.sprite.rect):
                    print("COLLIDE GAME OVER")
                    
                    return True
                   
        return False
        pass

        pass
    def run(self,key_pressed):
       
        # PLAYER COLLSIONS
        self.player_moving()
        self.add_buddy()
        game_over=self.check_if_collided()
        if self.player.sprite.player_is_moving and key_pressed!=False:
            self.move_buddies()
        
        for buddy in self.buddies:
            buddy.update()
        
        key_pressed=self.player.update(key_pressed)
        self.display_score()

        # PLAYER DRAW
        #self.tile.draw(self.display_suface)
        self.player.draw(self.display_suface)

        # BUDDY DRAW
        for buddy in self.buddies:
            buddy.draw(self.display_suface)

        for buddy in self.random_buddies:
            buddy.draw(self.display_suface)
        
        return key_pressed,game_over
    


