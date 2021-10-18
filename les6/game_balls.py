import pygame
from pygame.draw import *
import math
from random import randint
pygame.init()

SIZE=[30, 60, 90]

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0,255,0)
BLACK = (0,0,0)
COLORS = [ RED, GREEN, BLUE]

FPS = 30
screen = pygame.display.set_mode((1200, 800))

result = 0 #счетчик очков

check = 13 # контроьная цифра шаров на экране

k = 10 #количество шаров в начале

number_popped = 0 #количество шаров с нулевым радиусом

A = [] # массив шаров

check_n_new = 100 # начальный период добавления шаров

class Number: 
    def __init__(self, sign_pos,  n): # sign_pos: координаты левого верхнего угла, ширина и высота надписи; n: количество очков
        self.n = n
        self.sign_pos = sign_pos
        
    '''считает количество цифр в числе'''
    def count(self): 
        rest = self.n
        h = 0
        while rest > 0:
            rest //= 10
            h += 1
        if h == 0:
            h = 1
        return h
    
    ''' определяет какую цифру рисовать '''
    def what(self): 
        rest = self.n
        N = []
        for i in range(self.count()):
            b = rest % 10
            rest //= 10
            N.insert (0, b)
        return N

    ''' рисует на экране все число '''
    def draw(self): 
        G = self.what() # цифра для рисования
        x = self.sign_pos[0] + 10 # горизонтальная координата левого верхнего угла цифры
        y = self.sign_pos[1] + 10 # вертикальная координата левого верзнего угла цифры
        h = self.sign_pos[3] - 20 # высота цифры
        if (((self.sign_pos[2] - 10) // self.count() - 10)) < 50: # ширина цифры: не позволяет быть шире 50
            l = (self.sign_pos[2] - 10) // self.count() - 10
        else:
            l = 50
        for i in range (self.count()): # рисование цифры 
            if G[i] == 0: # 0 
                rect(screen, (0, 0, 0), (x, y, l, h), 5)
            if G[i] == 1: # 1
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
            if G[i] == 2: # 2
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x+l, y+h//2), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x, y+h), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
            if G[i] == 3: # 3
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
            if G[i] == 4: # 4
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 5: # 5
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x, y), (x, y+h//2), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
                line(screen, (0, 0, 0), (x+l, y+h//2), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x+l, y+h), (x, y+h), 5)
            if G[i] == 6: # 6
                line(screen, (0, 0, 0), (x, y), (x, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                rect(screen, (0, 0, 0), (x, y+h//2, l, h-h//2), 5)
            if G[i] == 7: # 7
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y), (x+l, y), 5)
                line(screen, (0, 0, 0), (x+l//2, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 8: # 8
                rect(screen, (0, 0, 0), (x, y, l, h), 5)
                line(screen, (0, 0, 0), (x, y+h//2), (x+l, y+h//2), 5)
            if G[i] == 9: # 9
                line(screen, (0, 0, 0), (x+l, y), (x+l, y+h), 5)
                line(screen, (0, 0, 0), (x, y+h), (x+l, y+h), 5)
                rect(screen, (0, 0, 0), (x, y, l, h//2), 5)

            x += l + 10 # сдвигает для получения промежутка между цифрами

class Ball:
    def __init__(self, wall_coord, coord, velocity, color, r): # на вход
                 self.coord = coord # координаты шара [x, y]
                 self.velocity = velocity # скорость шара по [x, y]
                 self.color = color # цвет шара (COLORS см выше)
                 self.r = r # радиус шара (SIZE см выше)
                 self.wall_coord = wall_coord # координаты стен [левая (по х), нижняя (по у), правая (по х), верхняя (по у)])


    '''вычисляет среднюю скорость'''
    def now_v (self):
        z = math.ceil(math.sqrt((self.velocity[0]) ** 2 + (self.velocity[1]) ** 2))
        return z
    
    ''' рисует шар '''
    def draw(self):  
        circle(screen, self.color, (self.coord[0], self.coord[1]), self.r) 

    ''' отражает шар от стен '''
    def wall(self): # отражает шар от стен
        if self.coord[0] <= self.wall_coord[0]: #левая стена
            self.velocity[0] *= -1
        if self.coord[1] >= self.wall_coord[1]: #нижняя стена
            self.velocity[1] *= -1
        if self.coord[0] >= self.wall_coord[2]: #правая стена
            self.velocity[0] *= -1
        if self.coord[1] <= self.wall_coord[3]: #верхняя стена
            self.velocity[1] *= -1

    ''' двигает шар с заданной скоростью '''
    def move(self):
        v0_x, v0_y = self.velocity
        self.coord[0] += v0_x
        self.coord[1] += v0_y
        self.wall()
        self.draw()
''' счет на голубом фоне (для текущего счета) '''
def score(a): 
    rect(screen, (0, 255, 255), ( 300, 300, 600, 200))
    S = Number([300, 300, 600, 200], a)
    S.draw()

''' счет на желтом фоне в розовой рамке (для финального счета) '''
def final_score(f_a): 
    rect(screen, (243, 67, 227), (0, 0, 1200, 800))
    rect(screen, (54, 108, 247), (150, 150, 900, 500),20, border_radius = 50)
    rect(screen, (255, 255, 0), (300, 300, 600, 200))
    S = Number([300, 300, 600, 200], f_a)
    S.draw()

def write_file(z, x):
    file = open('game_balls_score_file.txt','a') # имя игрока и результат записывается в файл
    file.write(z)
    file.write(': ')
    file.write(str(x))
    file.write (';   ')
    file.close()

''' создает шары'''
def add():
    p=randint (0, 2)
    vv=Ball([0, 800, 1200, 0],[randint(0, 1200),randint(0, 800)],[randint(1, 20),randint(1, 20)],COLORS[p],SIZE[p])
    A.append(vv)
    vv.draw()

''' создает начальные шары'''
for i in range(k):
    add ()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

number_popped = 0 # количество лопнувших шаров (с нулевым радиусом)
result = 0 # счетчик очков
n_new = 0 # счетчик обновления картинки для рагулярного создания новых шаров

print ('Write your name')
user_name = input()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for y in range (len(A)): # после нажатия перебирает все шары
                bb = A[y] # конкретный шар
                if ((event.pos[0] <= bb.coord[0] + bb.r) and
                    (event.pos[0] >= bb.coord[0] - bb.r) and
                    (event.pos[1] <= bb.coord[1] + bb.r) and
                    (event.pos[1] >= bb.coord[1] - bb.r)): # условие попадания по шару
                    bb.r = 0 # сужение шара
                    number_popped += 1 # увеличение количества лопнувших шаров
                    '''
                    прогрессивная шкала получения очков на основе мгновенной скорости и размера шара
                    -за маленький шар в три раза больше (мгновенная скорость * 3)
                    -за средний шар в два раза больше (мгновенная скорость * 2)
                    -за большой шар очки не увеличиваются (мгновенная скорость * 1)
                    '''
                    if bb.color == RED: 
                        result += bb.now_v() * 3
                    if bb.color == GREEN: 
                        result += bb.now_v()  * 2 
                    if bb.color == BLUE: 
                        result += bb.now_v() 
        if  len(A) - number_popped >= check: # при достижении контрольной цифры шаров на экране
            for i in range(len(A)):
                dd = A[i]
                dd.r = 0
            final_score(result) # выводится финальный результат
            finished = True
    if (len(A) > 10): # при появлении шаров на экране появляется счетчик текущего результата на заднем фоне
        score(result)
    n_new += 1 # счетчик обновлений экрана
    if (n_new % check_n_new == 0): # кажде 100 обновление экрана добавляет шар
        add()
        check_n_new -= 5

    for u in range (len(A)): #двигает каждый шар
        aa = A[u]
        aa.move()
            
    pygame.display.update()
    screen.fill(BLACK)

final_score(result) # выводится финальный результат

if event.type == pygame.MOUSEBUTTONDOWN:
    pygame.quit()
