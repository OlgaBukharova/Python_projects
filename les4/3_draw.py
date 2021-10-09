import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255,255,255,0),(0,0,400,400))
circle(screen, (0, 0, 0, 0),(200,200), 101)
circle(screen, (255, 249, 0, 0),(200,200), 100)
circle(screen, (0, 0, 0, 0), (150,170), 21)
circle(screen, (255, 0, 0, 0), (150,170), 20)
circle(screen, (0, 0, 0, 0), (250,170), 16)
circle(screen, (255, 0, 0, 0), (250,170), 15)
circle(screen, (0, 0, 0, 0), (150,170), 10)
circle(screen, (0, 0, 0, 0), (250,170), 7)
polygon(screen, (0,0,0,0), [(90,120),(180,150),(175,160),(85,130)])
polygon(screen, (0,0,0,0), [(220,150),(310,130),(312,140),(222,160)])
rect(screen, (0,0,0,0), (150,250,100,20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
