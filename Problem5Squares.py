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

#To get the same shape of concentric squares try this
#import turtle
#def drawSquare(t, sz):
#   """Get turtle t to draw a square of sz side"""
#   for i in range(4):
#       t.forward(sz)
#        t.left(90)
        
#wn = turtle.Screen()

#alex = turtle.Turtle()
#alex.color("blue")

#size = [20, 40, 60, 80, 100]

#for x in size:
#    drawSquare(alex,x)
#    alex.penup()
#    alex.backward(10)       # move alex to the starting position for the next square
#    alex.right(90)
#    alex.forward(10)
#    alex.left(90)
#    alex.pendown()

#wn.exitonclick()



