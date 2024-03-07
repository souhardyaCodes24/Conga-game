from os import walk
import pygame
from settings import player_height,player_width

def import_images(path):
    surfaces = []

    for _,__,images in walk(path):
        for img in images:
            img_surf=pygame.transform.scale(pygame.image.load(path+'/'+img),(player_width,player_height))
            surfaces.append(img_surf)
    return surfaces