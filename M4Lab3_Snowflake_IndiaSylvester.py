# A program that draws my intials
# 6-20-17
#  CTI-110 M4LAB3 - Snowflake
# India Sylvester
#


#intialize and import turtle
import turtle
wn = turtle.Screen()
t = turtle.Turtle()

# change the pen size
t.pensize(2)

#change color
t.pencolor("cyan")

#show shape of marker
t.shape("turtle")

def branch():
    for i in range(2):
        for i in range(2):
            t.forward(50)
            t.backward(50)
            t.right(45)
        t.right(90)
        t.backward(50)
        t.right(45)
    t.right(90)
    t.forward(90)

for i in range(5):
    branch()
    t.left(108)

wn.mainloop()
