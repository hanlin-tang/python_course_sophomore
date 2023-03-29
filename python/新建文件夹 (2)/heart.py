import turtle

turtle.bgcolor("black")

turtle.pensize(2)
sizeh =1.2

def curve():
    for ii in range(200):
        turtle.right(1)
        turtle.forward(1* sizeh)

turtle.speed(0)
turtle.color("red","black")
turtle.begin_fill()
turtle.left(140)
turtle.forward(116.5* sizeh)
curve()
turtle.left(120)

curve()
turtle.forward(116.5* sizeh)
turtle.end_fill()
turtle.hideturtle

input('Press<Enter>')
