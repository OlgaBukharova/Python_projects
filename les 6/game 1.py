import pygame
from pygame.draw import *
from random import randint
pygame.init()

SIZE=[30,60,90]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
BLACK = (0,0,0)
COLORS = [RED,GREEN, BLUE]

FPS = 30
screen = pygame.display.set_mode((1200, 800))

result=0

k=10

number_popped=0

A=[]

class Number:
    def __init__(self, sign_pos,  n): # sign_pos: координаты левого верхнего угла, ширина и высота надписи; n: количество очков
        self.n = n
        self.sign_pos = sign_pos
        
    def count(self):
        rest = self.n
        h = 0
        while rest>0:
            rest //=10
            h += 1
        return h
    
    def what(self):
        rest = self.n
        N = []
        for i in range(self.count()):
            b = rest % 10
            rest //=10
            N.insert (0,b)
        return N
        
    def draw(self):
        G = self.what()
        x = self.sign_pos[0]+10
        y = self.sign_pos[1]+10
        h = self.sign_pos[3]-20
        if ((self.sign_pos[2]-10)//self.count()-10)>50:
            l=50
        else:
            l = (self.sign_pos[2]-10)//self.count()-10
        for i in range (self.count()):
            if G[i] == 0:
                rect(screen, (0, 0, 0), (x, y, l, h), 5)
            if G[i] == 1:
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
            if G[i] == 2:
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x+l, y+h//2), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x, y+h), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
            if G[i] == 3:
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
            if G[i] == 4:
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 5:
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x, y), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x+l, y+h//2), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x+l, y+h), (x, y+h), 5)
            if G[i] == 6:
                line(screen, (0, 0, 0), (x, y), (x, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                rect(screen, (0, 0, 0), (x, y+h//2, l, h-h//2), 5)
            if G[i] == 7:
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x+l//2, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 8:
                rect(screen, (0, 0, 0), (x, y, l, h), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 9:
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
                rect(screen, (0, 0, 0), (x, y, l, h//2), 5)

            x +=l+10


def score(a):
    rect(screen, (0,255,255), (300,300,600,200))
    S = Number([300, 300, 600, 200], a)
    S.draw()
    

class Ball:
    def __init__(self,wall_coord, coord, velocity, color, r):
                 self.coord = coord
                 self.velocity = velocity
                 self.color = color
                 self.r = r
                 self.wall_coord=wall_coord
    
    def draw(self):
        circle(screen, self.color, (self.coord[0], self.coord[1]), self.r)

    def wall(self):
        if self.coord[0]<=self.wall_coord[0]: #левая стена
            self.velocity[0] *= -1
        if self.coord[1]>=self.wall_coord[1]: #нижняя стена
            self.velocity[1] *= -1
        if self.coord[0]>=self.wall_coord[2]: #правая стена
            self.velocity[0] *= -1
        if self.coord[1]<=self.wall_coord[3]: #верхняя стена
            self.velocity[1] *= -1
        
    def move(self):
        v0_x, v0_y = self.velocity
        self.coord[0] += v0_x
        self.coord[1] += v0_y
        self.wall()
        self.draw()

    
        
for i in range(k):
    f = randint(0,2)
    a=Ball([0,800,1200,0],[randint(0,1200),randint(0,800)],[randint(1,20),randint(1,20)],COLORS[f],SIZE[f])
    A.append(a)

    
pygame.display.update()
clock = pygame.time.Clock()
finished = False

number_popped = 0
result = 0
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for y in range (k):
                bb=A[y]
                if (event.pos[0]<=bb.coord[0]+bb.r) and (event.pos[0]>=bb.coord[0]-bb.r) and (event.pos[1]<=bb.coord[1]+bb.r) and (event.pos[1]>=bb.coord[1]-bb.r):
                    bb.r=0
                    number_popped += 1
                    if bb.color == RED:
                        result += 30
                    if bb.color == GREEN:
                        result += 20
                    if bb.color == BLUE:
                        result += 10
        if (number_popped==k):
            score(result)
        if (event.type == pygame.QUIT):
            finished = True
            print(result)
    
        
    for u in range (k):
        aa=A[u]
        aa.move()
        
    
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()
