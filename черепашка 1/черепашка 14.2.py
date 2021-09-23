import turtle

turtle.shape ('turtle')

def star (n):
    for i in range(n):
        turtle.forward (100)
        turtle.left (180-180/n)

star(11)
