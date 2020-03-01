import turtle

def drawSquare (t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("black")

jordan = turtle.Turtle()
jordan.color("blue")

drawSquare(jordan,150)

jordan.penup()
jordan.forward(100)
jordan.left (90)
jordan.forward(130)
jordan.left(90)
jordan.pendown()

for i in range(1):
    drawSquare(jordan,90)
    jordan.penup()
    jordan.forward(80)
    jordan.left(90)
    jordan.forward(20)
    jordan.pendown()

for i in range(1):
    drawSquare(jordan,50)
    jordan.penup()
    jordan.forward(40)
    jordan.left(90)
    jordan.forward(15)
    jordan.pendown()
for i in range (1):
    drawSquare(jordan,25)
    jordan.penup()
    jordan.forward(20)
    jordan.left(90)
    jordan.forward(10)
    jordan.pendown()

for i in range(1):
    drawSquare(jordan,10)

wn.exitonclick()


