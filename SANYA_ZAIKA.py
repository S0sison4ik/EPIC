import pygame
import pygame.math
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1800, 800))

polygon (screen, (255, 150, 128), [(0, 0), (800, 0), (1800, 800), (0, 1800)], 2000)
polygon (screen, (255, 0, 128), [(0, 270), (1800, 270), (1800, 800), (0, 800)])
math.sin (screen, "orange", [(0, 1), (1800, 800)], 1)
circle (screen, "yellow", (900, 220), 90)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            
            https://cs.mipt.ru/gertsev/fbmf/lessons/intro_python/pictures_1.html