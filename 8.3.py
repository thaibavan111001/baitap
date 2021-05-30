import turtle
colors=["red","blue","yellow"]
painter=turtle.Turtle()
painter.pensize(3)
for i in range(100):
    for i in colors:
        painter.pencolor(i)
        painter.circle(100)
        painter.left(30)
