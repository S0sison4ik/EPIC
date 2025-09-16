import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

polygon (screen, "white", [(0,0),(0, 800),(800, 800), (0, 800)], 10000)
circle (screen,"yellow", (400, 400), 400)
circle (screen, "red", (190, 330), 80)
circle (screen, "red", (600, 330), 80)
circle (screen, "black", (190, 330), 40)
circle (screen, "black", (600, 330), 40)
polygon (screen, "black", [(80, 200), (350, 250), (350, 260), (90, 220)], 20)
polygon (screen, "black", [(450, 250), (650, 200), (650, 210), (450, 270)], 20)
polygon (screen, "black", [(250, 600), (600, 600), (600, 670), (250, 670)], 30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True