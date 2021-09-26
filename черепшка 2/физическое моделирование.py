import turtle
import time

turtle.shape('turtle')

x = 0
y = 0
vx = 30
vy = 30
dt = 0.1
g = -10
w = 0.9
q = 0.9
k = -0.02
turtle.penup()
turtle.goto(1000,0)
turtle.pendown()
turtle.goto(x,y)
while True:
    x += vx * dt
    y += vy * dt + g * dt**2 /2
    vy += g * dt + k * vy * dt
    vx += k * vx * dt
    if y <= 0:
        y = 0
        vy *= -q
        vx *= w
    turtle.goto(x, y)
