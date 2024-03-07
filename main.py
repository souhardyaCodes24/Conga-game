import pygame
from level import Level
from settings import *
screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Congo Congo Congo!")

pygame.init()

font=pygame.font.Font('freesansbold.ttf',30)
level = Level(screen)


bg=pygame.transform.scale(pygame.image.load('./graphics/map/bg.jpg'),(WIDTH,HEIGHT))

key_pressed=False
while True:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                key_pressed="s"
            if event.key==pygame.K_w:
                key_pressed="w"
            if event.key==pygame.K_a:
                key_pressed="a"
            if event.key==pygame.K_d:
                key_pressed="d"
            
    

    key_pressed,game_over=level.run(key_pressed)

    if game_over:
        text = font.render(f'GAME OVER ! Score: {level.score}',True,'red','green')
        over_rect=text.get_rect()
        over_rect.center=(500,500)

        screen.blit(text,over_rect)
        level.buddies.clear()

 
    pygame.display.update()
    pygame.time.Clock().tick(60)
    if game_over:
        pygame.time.delay(2000)