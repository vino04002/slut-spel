import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()
width, height = 64*10, 64*8
screen=pygame.display.set_mode((width, height))
player_x = 200
player_y = 200
player = pygame.image.load("gubbe.png")
while 1:
    screen.fill((255,255,255))
    screen.blit(player, (player_x, player_y))
    pygame.display.flip() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
         
            pygame.quit() 
            exit(0)
