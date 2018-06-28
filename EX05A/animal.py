"""Drawing an animal using turtle module."""


import turtle


turtle.colormode(255)
turtle.hideturtle()
turtle.speed("fast")
distance = 25  # pixels
x, y = -50, 0

turtle.pensize(0.5)
turtle.pencolor(11, 1, 0)
turtle.fillcolor(245, 245, 245)

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.pu()
turtle.up()



def legs(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 0, 13)
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

legs(-50, 0)
legs(50, 0)



def ears(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 4, 13)
    turtle.begin_fill()
    turtle.circle(22)
    turtle.end_fill()

ears(-55, 180)
ears(55, 180)



def paws(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 0, 13)
    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

paws(-40, 60)
paws(40, 60)


def paw_insides(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(255, 251, 253)
    turtle.begin_fill()
    turtle.circle(13)
    turtle.end_fill()

paw_insides(-52, 5)
paw_insides(52, 5)


# Draw bears head
turtle.goto(0, 90)

turtle.pendown()
turtle.pensize(1)
turtle.pencolor(11, 1, 0)
turtle.fillcolor(245, 245, 245)

turtle.begin_fill()
turtle.circle(70)
turtle.end_fill()

turtle.penup()
turtle.pu()
turtle.up()


size = 18
def eyes(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 4, 13)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

eyes(22, 155)
eyes(-22, 155)
size = 22
eyes(34, 144)
eyes(-34, 144)


dot_size = 8
def nose(x, y):

    turtle.goto(x, y)
    turtle.dot()
    turtle.dot(size=dot_size)

nose(-4, 138)
nose(4, 138)
nose(0, 138)
dot_size = 6
nose(-2.5, 136)
nose(2.5, 136)
dot_size = 7
nose(0, 134)


# Draw mouth
turtle.pendown()
turtle.setheading(270)
turtle.forward(20)
turtle.colormode(255)
turtle.color(255, 4, 0)

turtle.begin_fill()
turtle.dot()
turtle.dot(size=10)

turtle.setheading(180)
turtle.forward(5)
turtle.setheading(0)
turtle.forward(10)

turtle.pendown()
turtle.pd()
turtle.up()


def tale(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(25, 4, 90)

    turtle.pendown()
    turtle.setheading(120)
    turtle.forward(20)
    turtle.setheading(90)
    turtle.forward(30)
    turtle.setheading(190)
    turtle.forward(60)
    turtle.setheading(120)
    turtle.forward(20)

    turtle.begin_fill()
    turtle.dot()
    turtle.dot(size=10)

    turtle.pd()
    turtle.up()

tale(-54, 52)
tale(-53, 50)


turtle.done()
