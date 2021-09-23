import turtle
from math import pi

turtle.shape ('turtle')

def circle (r):
    l=2*pi*r
    for i in range (360):
        turtle.forward (l/360)
        turtle.left (1)

r=100
d=3
for i in range (d):
    circle (r)
    turtle.left (180)
    circle(r)
    turtle.left (180/d)
