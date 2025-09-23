import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1000))

def draw_sky(x, y, size=1.0):
    
    # небо
    screen.fill((135, 206, 235))
    # трава
    rect(screen, (34, 139, 34), (0, 500, 800, 500))
def draw_bunny(x, y, size=1.0):
    
    # Хвостик
    circle(screen, (240, 240, 240), (int(x + 200*size), int(y + 450*size)), int(25*size))
    circle(screen, (0, 0, 0), (int(x + 200*size), int(y + 450*size)), int(25*size), 1)
 
    # Передние лапки
    ellipse(screen, (240, 240, 240), (x + 120*size, y + 400*size, 50*size, 80*size))
    ellipse(screen, (0, 0, 0), (x + 120*size, y + 400*size, 50*size, 80*size), 1)
    
    ellipse(screen, (240, 240, 240), (x + 230*size, y + 400*size, 50*size, 80*size))
    ellipse(screen, (0, 0, 0), (x + 230*size, y + 400*size, 50*size, 80*size), 1)
    
    # Задние лапки
    ellipse(screen, (240, 240, 240), (x + 80*size, y + 350*size, 60*size, 100*size))
    ellipse(screen, (0, 0, 0), (x + 80*size, y + 350*size, 60*size, 100*size), 1)
    
    ellipse(screen, (240, 240, 240), (x + 260*size, y + 350*size, 60*size, 100*size))
    ellipse(screen, (0, 0, 0), (x + 260*size, y + 350*size, 60*size, 100*size), 1)
    
    # Левое ухо
    ellipse(screen, (240, 240, 240), (x + 150*size, y + 10*size, 40*size, 120*size))
    ellipse(screen, (0, 0, 0), (x + 150*size, y + 10*size, 40*size, 120*size), 1)
    ellipse(screen, (255, 182, 193), (x + 160*size, y + 30*size, 20*size, 80*size))
    
    # Правое ухо
    ellipse(screen, (240, 240, 240), (x + 210*size, y + 10*size, 40*size, 120*size))
    ellipse(screen, (0, 0, 0), (x + 210*size, y + 10*size, 40*size, 120*size), 1)
    ellipse(screen, (255, 182, 193), (x + 220*size, y + 30*size, 20*size, 80*size))
    
    # Тело зайца
    ellipse(screen, (240, 240, 240), (x + 100*size, y + 150*size, 200*size, 300*size))
    ellipse(screen, (0, 0, 0), (x + 100*size, y + 150*size, 200*size, 300*size), 1)
    
    # Голова
    circle(screen, (240, 240, 240), (int(x + 200*size), int(y + 100*size)), int(80*size))
    circle(screen, (0, 0, 0), (int(x + 200*size), int(y + 100*size)), int(80*size), 1)

    
    # Глаза
    # Левый глаз
    ellipse(screen, (255, 255, 255), (x + 170*size, y + 80*size, 25*size, 35*size))
    ellipse(screen, (0, 100, 0), (x + 177*size, y + 90*size, 15*size, 20*size))
    ellipse(screen, (0, 0, 0), (x + 182*size, y + 95*size, 8*size, 10*size))
    ellipse(screen, (255, 255, 255), (x + 184*size, y + 97*size, 3*size, 4*size))
    
    # Правый глаз
    ellipse(screen, (255, 255, 255), (x + 205*size, y + 80*size, 25*size, 35*size))
    ellipse(screen, (0, 100, 0), (x + 212*size, y + 90*size, 15*size, 20*size))
    ellipse(screen, (0, 0, 0), (x + 217*size, y + 95*size, 8*size, 10*size))
    ellipse(screen, (255, 255, 255), (x + 219*size, y + 97*size, 3*size, 4*size))
    
    # Нос
    polygon(screen, (255, 182, 193), [
        (x + 200*size, y + 120*size),
        (x + 190*size, y + 130*size),
        (x + 210*size, y + 130*size)
    ])
    
    # Рот
    arc(screen, (0, 0, 0), (x + 195*size, y + 135*size, 20*size, 10*size), 3.14, 6.28, 2)

draw_sky(200, 200, 1.2)
draw_bunny(200, 200, 1.2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True