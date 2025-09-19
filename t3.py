import turtle as t


t.shape("turtle")

t.bgcolor('yellow')
t.color('blue')
t.pensize(5)
t.penup()

angle = 49.9

t.goto(100, 100)

t.pendown()

for x in range(80) :
    t.forward(x)
    t.left(angle)

t.done()
