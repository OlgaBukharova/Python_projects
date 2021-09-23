import turtle
from math import pi

turtle. shape ('turtle')

def circle (r):
    l=2*pi*r
    for i in range (360):
        turtle.forward (l/360)
        turtle.left (1)

for r in range (10,100,10):
    for i in range (2):
        circle (r)
        turtle.left (180)
    
    
