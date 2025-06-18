import turtle

t = turtle.Turtle()

t.speed(1)

t.forward(100) 
t.right(90) 

t.forward(100)
t.right(90)

t.forward(100) 
t.right(90)  

t.forward(100)
t.right(90)

t.penup()
t.goto(30, -30)
t.pendown()

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)


t.penup()
t.goto(0, 0)
t.pendown()
t.goto(30, -30)

t.penup()
t.goto(100, 0)
t.pendown()
t.goto(130, -30)

t.penup()
t.goto(100, -100)
t.pendown()
t.goto(130, -130)

t.penup()
t.goto(0, -100)
t.pendown()
t.goto(30, -130)

t.hideturtle()
turtle.done()
