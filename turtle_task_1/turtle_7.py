import turtle
from math import pi, sin, cos
turtle.shape ('turtle')

for i in range (400):
    t=i*pi/10
    x=t*cos(t)
    y=t*sin(t)
    turtle.goto(x,y)
