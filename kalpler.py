import turtle,random
from random import randint
ekran=turtle.Screen()
ekran.bgcolor("black")
pen=turtle.Turtle()
pen.pensize(2)
pen.speed(0)
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
    pen.speed(0)

def draw_heart(x, y, size):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

    pen.color("white")
    pen.begin_fill()

    pen.left(140)
    pen.forward(111.65+size)
    curve()
    pen.left(120)
    curve()
    pen.forward(111.65+size)
    pen.right(120)
    pen.end_fill()
    pen.right(100)


def draw_random_hearts(num_hearts):
    for i in range(num_hearts):
        x = random.randint(-280, 280)
        y = random.randint(-100, 100)
        size = random.uniform(0.01, 1.0)
        draw_heart(x, y, size)
draw_random_hearts(4)

turtle.hideturtle()
turtle.done()
