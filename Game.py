import pygame
from playerKaiju import playerKaiju
from enemyJaeger import enemyJaeger

pygame.init()

clock = pygame.time.Clock()

height = 800
width = 600
size = width, height

screen = pygame.display.set_mode(size)

player = p([width/2, height/2])

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)
