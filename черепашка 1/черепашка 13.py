import turtle
from math import pi

turtle. shape ('turtle')

def duga (r,a):
    l=2*pi*r
    if a>=0:
        for i in range (a):
            turtle.forward (l/a)
            turtle.left (1)
    else:
        for i in range (abs(a)):
            turtle.forward (l/abs(a))
            turtle.right (1)

turtle.color ('yellow')
turtle.begin_fill()
duga (100,360)
turtle.end_fill()
turtle.penup()
turtle.left (90)
turtle.forward (150)
turtle.left(90)
turtle.forward (20)
turtle.right(90)
turtle.pendown()
turtle.color('blue')
turtle.begin_fill()
duga (15,360)
turtle.end_fill ()
turtle.penup()
turtle.right(90)
turtle.forward(40)
turtle.right (90)
turtle.pendown()
turtle.begin_fill ()
duga(15,360)
turtle.end_fill()
turtle.penup()
turtle.left (90)
turtle.forward (20)
turtle.right(90)
turtle.forward (70)
turtle.pendown()
turtle.color('red')
turtle.width(10)
duga(20,-180)
turtle.penup()
turtle.right (90)
turtle.forward (40)
turtle.left(90)
turtle.pendown()
turtle.color('black')
turtle.forward (20)





