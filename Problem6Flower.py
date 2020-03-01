import turtle
def hexagon (t, sz):
    for i in range(6):
        t.forward(sz)
        t.left(60)
wn = turtle.Screen()
wn.bgcolor("yellow")

jordan = turtle.Turtle()
jordan.color("red")

hexagon(jordan,30)

for i in range(1):
    jordan.penup()
    jordan.forward(10)
    jordan.pendown()

hexagon(jordan,30)

for i in range(1):
    jordan.penup()
    jordan.forward(10)
    jordan.pendown()

hexagon(jordan,30)

for i in range(1):
    jordan.penup()
    jordan.left(30)
    jordan.pendown()

hexagon(jordan,30)

for i in range(1):
    jordan.penup()
    jordan.left(30)
    jordan.pendown()
hexagon(jordan,30)

