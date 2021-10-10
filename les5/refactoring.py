import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill((50, 210, 250))

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
    
#рандомайзер цвета гривы
def hair_color():
    x = randint(1, 5)
    if x == 1 :
        haircolor = (210, 150, 220)
    if x ==2 :
        haircolor = (230, 230, 150)
    if x ==3 :
        haircolor = (180, 240, 220)
    if x==4 :
        haircolor = (210, 70, 230)
    if x==5 :
        haircolor = (210, 220, 80)
    return(haircolor)

#грива, хвост
#на вход: количество элипсов, координаты левого верхнего угла, ширина и высота прямоугольной зоны рисования элпсов, х координата левой верхней точки элипса, ширина, аналогично для у 
def hair_sector( number,sector_x, sector_y, sector_length, sector_hight, elipse_min_x,rand_x,elipse_min_y,rand_y):
    for i in range(number):
        elipse_x=randint(sector_x, sector_x+sector_length)
        elipse_y=randint(sector_y, sector_y+sector_hight)
        ellipse( screen, hair_color(), (elipse_x, elipse_y, randint(elipse_min_x,elipse_min_x+rand_x),randint(elipse_min_y,elipse_min_y+rand_y)))
#солнце
#на вход: координаты центра солнца, радиус        
def sun (sun_x, sun_y, sun_rad):
    circle(screen, (255, 255, 0), (sun_x, sun_y), sun_rad)
    
#небо, трава    
#на вход: высота неба
def grass(sky_hight):
    screen.fill((50, 210, 250))
    rect(screen, (50, 255, 50), (0, sky_hight, 500, 400))
#дерево 
#на вход: координаты левой верхней точки, ширина и высота дерева
def tree(tree_x, tree_y, tree_width, tree_hight):
    dh=tree_hight-420
    dl=tree_width-250
    #ствол
    rect(screen, (255, 255, 255), (tree_x+115, tree_y+220, 20+dl//5, 200+dh//4))
    #крона средний овал
    ellipse(screen, (0, 110, 0), (tree_x, tree_y+120, 250+dl, 130+dh//4))
    #крона нижний овал
    ellipse(screen, (0, 110, 0), (tree_x+60, tree_y+220, 130+dl, 100+dh//4))
    #крона верхний овал
    ellipse(screen, (0, 110, 0), (tree_x+80, tree_y, 90+dl, 150+dh//4))
    #плоды
    ellipse(screen, (220, 150, 255), (tree_x+200, tree_y+180, 40, 30))
    ellipse(screen, (220, 150, 255), (tree_x+35, tree_y+170, 40, 35))
    ellipse(screen, (220, 150, 255), (tree_x+140, tree_y+270, 35, 40))
    ellipse(screen, (220, 150, 255), (tree_x+110, tree_y+30, 45, 40))

#единорог 
#на вход: координаты левого верхнего угла без хвоста и рога, ширина, высота туловища
def unicorn(unicorn_x, unicorn_y,unicorn_width, unicorn_hight):
    u_dl=unicorn_width-200 #разница длины тела
    u_dh=unicorn_hight-100 #разница ширины тела
    #тело
    ellipse(screen, (255, 255, 255), (unicorn_x, unicorn_y+70, 200+u_dl, 100+u_dh))
    #лоб
    ellipse(screen, (255, 255, 255), (unicorn_x+140, unicorn_y, 60+u_dl//2, 40+u_dh//2))
    #голова
    ellipse(screen, (255, 255, 255), (unicorn_x+150, unicorn_y+15, 80+u_dl//2, 30+u_dh//2))
    #шея
    rect(screen, (255, 255, 255), (unicorn_x+140, unicorn_y+20, 50+u_dl//4, 100+u_dh//2))
    #ноги
    rect(screen, (255, 255, 255), (unicorn_x+20, unicorn_y+120, 13+u_dl//7, 110+u_dh))
    rect(screen, (255, 255, 255), (unicorn_x+50, unicorn_y+120, 16+u_dl//7, 100+u_dh))
    rect(screen, (255, 255, 255), (unicorn_x+135, unicorn_y+130, 18+u_dl//7, 110+u_dh))
    rect(screen, (255, 255, 255), (unicorn_x+160, unicorn_y+120, 14+u_dl//7, 105+u_dh))
    #глаз
    circle(screen, (160, 90, 180), (unicorn_x+180, unicorn_y+20), 10+u_dl//10)
    #зрачок
    circle(screen, (0, 0, 0), (unicorn_x+182, unicorn_y+20), 4+u_dl//11)
    #блик в глазу
    draw_ellipse_angle(screen, (255, 255, 255), [unicorn_x+172, unicorn_y+13, 10, 4], -30, 0)
    #рог
    polygon(screen, (220, 150, 255), ((unicorn_x+170, unicorn_y+2), (unicorn_x+178, unicorn_y+6), (unicorn_x+182, unicorn_y-60)))
    #грива
    hair_sector( 17+u_dl//15+u_dh//10, unicorn_x+110, unicorn_y-10, 20+u_dl, 80+u_dh, 30, 15, 10, 10)
    hair_sector( 17+u_dl//15+u_dh//10, unicorn_x+70, unicorn_y+60, 70+u_dl, 20+u_dh, 40, 10, 10, 5)
    #хвост
    hair_sector( 10+u_dl//15+u_dh//10, unicorn_x-10, unicorn_y+90, 10+u_dl, 40+u_dh, 25, 10, 10, 5)
    hair_sector( 10+u_dl//15+u_dh//10, unicorn_x-20, unicorn_y+125, 15+u_dl, 35+u_dh, 30, 5, 10, 5)
    hair_sector( 10+u_dl//15+u_dh//10, unicorn_x-10, unicorn_y+160, 10+u_dl, 30+u_dh, 30, 5, 10, 5)
    hair_sector( 10+u_dl//15+u_dh//10, unicorn_x-30, unicorn_y+160, 20+u_dl, 30+u_dh, 20, 15, 10, 5)

#небо/трава
grass(300)

#дерево
tree(-50,80,250,420)

#единорог
unicorn(200,430,200,100)

#солнце
sun(490, 60, 100)
        
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
