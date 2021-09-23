import turtle
from math import pi, sin 

turtle.shape ('turtle')

def storona(n, r):
    return (2*r*sin(pi/n))

def vn_ugol (n):
    return (360/n)

def fig(n, r):
    s=storona (n, r)
    a=vn_ugol(n)
    turtle.left (a+(180-a)/2)
    for i in range(n):
        turtle.forward (s)
        turtle.left (a)
    turtle.right (a+(180-a)/2)

last_r=0
n=3
for r in range (10, 200, 10):
    turtle.penup ()
    turtle.forward(r-last_r)
    turtle.pendown()
    fig (n, r)
    n=n+1
    last_r=r
