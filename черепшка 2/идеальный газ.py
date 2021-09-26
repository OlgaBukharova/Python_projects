import random
import turtle

number_of_turtles = 50

pool = [turtle.Turtle() for i in range(number_of_turtles)]
vx = [random.random() * 100 for i in range(number_of_turtles)]
vy = [random.random() * 100 for i in range(number_of_turtles)]
x = [random.randint(0, 100)  for i in range(number_of_turtles)]
y = [random.randint(0, 100)  for i in range(number_of_turtles)]
turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)
turtle.ht()

for i, unit in enumerate(pool):
    unit.penup()
    unit.speed(0)
    unit.goto(x[i], y[i])

dt = 0.1

while True:
    
    for i in range(number_of_turtles):
        x[i] += vx[i] * dt
        y[i] += vy[i] * dt

        if x[i] >= 100 or x[i] <= 0:
            x[i] = 100 * (x[i] >= 100) 
            vx[i] *= -1

        if y[i] >= 100 or y[i] <= 0:
            y[i] = 100 * (y[i] >= 100) 
            vy[i] *= -1

        pool[i].goto(x[i], y[i])

    for i in range(number_of_turtles):
        for j in range(i, number_of_turtles):
            if (x[i] - x[j])*(x[i] - x[j]) +\
               (y[i] - y[j])*(y[i] - y[j]) <= 100:
                vx[i] *= -1
                vy[i] *= -1

                vx[j] *= -1
                vy[j] *= -1

