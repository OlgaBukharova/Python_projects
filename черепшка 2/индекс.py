import turtle

turtle.shape('turtle')

def dr(num, a=40):
    turtle.penup()
    x0, y0 = turtle.pos()

    coords = [(x0, y0), (x0 + a, y0), (x0, y0 - a), (x0 + a, y0 - a), (x0, y0 - 2 * a), (x0 + a, y0 - 2 * a)]

    def where(b):
        turtle.goto(*coords[b - 1])

    where(num[0])
    turtle.pendown()

    for i in num:
        where(i)

    turtle.penup()
    where(1)
    turtle.pendown()

shape= [(1, 2, 6, 5, 1), (3, 2, 6), (1, 2, 4, 5, 6), (1, 2, 3, 4, 5), (1, 3, 4, 2, 6), (2, 1, 3, 4, 6, 5), (2, 3, 5, 6, 4, 3), (1, 2, 3, 5), (1, 5, 6, 2, 1, 3, 4), (4, 3, 1, 2, 4, 5)]   

num = list(map(int,list(input())))

for i in num:
    dr(shape[i])
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
