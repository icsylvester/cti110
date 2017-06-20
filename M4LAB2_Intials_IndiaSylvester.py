import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.pensize(2)
t.pencolor("pink")
t.shape("turtle")

t.left(90)
t.forward(90)

t.penup()
t.right(90)
t.forward(200)
t.pendown()

for i in(1,2,3):
 t.backward(90)
 t.left(90)

t.penup()
t.right(90)
t.backward(100)
t.pendown()

for i in(1,1):
 t.backward(40)
 t.left(90)
 t.backward(40)
 t.right(90)
 t.forward(40)
 t.left(90)
 t.backward(40)
 t.right(90)
 t.backward(40)
 
 wn.mainloop()
