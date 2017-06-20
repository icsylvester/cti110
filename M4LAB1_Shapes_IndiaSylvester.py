import turtle
wn = turtle.Screen()
t = turtle.Turtle()

t.pensize(2)
t.pencolor("teal")
t.shape("turtle")

for i in (1,2,3):
  t.forward(120)
  t.left(120)

t.penup()
t.backward(200)
t.pendown()

for i in(1,2,3,4):
 t.forward(90)
 t.left(90)
 
wn.mainloop()
