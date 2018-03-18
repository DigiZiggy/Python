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



def turtle_goto4(x, y):

    turtle.goto(x, y)

    turtle.colormode(255)
    turtle.color(11, 0, 13)

    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

turtle_goto4(-50, 0)
turtle_goto4(50, 0)



def turtle_goto1(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 4, 13)

    turtle.begin_fill()
    turtle.circle(22)
    turtle.end_fill()

turtle_goto1(-55, 180)
turtle_goto1(55, 180)



def turtle_goto2(x, y):

    turtle.goto(x, y)

    turtle.colormode(255)
    turtle.color(11, 0, 13)

    turtle.begin_fill()
    turtle.circle(15)
    turtle.end_fill()

turtle_goto2(-40, 60)
turtle_goto2(40, 60)


def turtle_paws(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(255, 251, 253)

    turtle.begin_fill()
    turtle.circle(13)
    turtle.end_fill()

turtle_paws(-52, 5)
turtle_paws(52, 5)


x, y = 0, 90

turtle.goto(x, y)

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



def turtle_goto5(x, y):

    turtle.goto(x, y)

    turtle.colormode(255)
    turtle.color(11, 4, 13)

    turtle.begin_fill()
    turtle.circle(18)
    turtle.end_fill()

turtle_goto5(22, 155)
turtle_goto5(-22, 155)



def turtle_goto3(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(11, 4, 13)

    turtle.begin_fill()
    turtle.circle(22)
    turtle.end_fill()

turtle_goto3(34, 144)
turtle_goto3(-34, 144)


def turtle_dot(x, y):

    turtle.goto(x, y)
    turtle.dot()
    turtle.dot(size=8)

turtle_dot(-4, 138)
turtle_dot(4, 138)
turtle_dot(0, 138)

x, y = -2.5, 136

turtle.goto(x, y)

turtle.dot()
turtle.dot(size=6)

x, y = 2.5, 136

turtle.goto(x, y)
turtle.dot()
turtle.dot(size=6)

x, y = 0, 134

turtle.goto(x, y)

turtle.dot()
turtle.dot(size=7)

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
turtle.begin_fill()
turtle.dot()
turtle.dot(size=10)

turtle.setheading(0)
turtle.forward(10)
turtle.begin_fill()
turtle.dot()
turtle.dot(size=10)


turtle.pendown()
turtle.pd()
turtle.up()


def turtle_tale(x, y):

    turtle.goto(x, y)
    turtle.colormode(255)
    turtle.color(25, 4, 90)


    turtle.pendown()
    turtle.setheading(120)
    turtle.forward(20)

    turtle.colormode(255)
    turtle.color(25, 4, 90)

    turtle.setheading(90)
    turtle.forward(30)

    turtle.colormode(255)
    turtle.color(25, 4, 90)

    turtle.setheading(190)
    turtle.forward(60)

    turtle.colormode(255)
    turtle.color(25, 4, 90)

    turtle.setheading(120)
    turtle.forward(20)

    turtle.colormode(255)
    turtle.color(25, 4, 90)

    turtle.begin_fill()
    turtle.dot()
    turtle.dot(size=10)


    turtle.pendown()
    turtle.pd()
    turtle.up()

turtle_tale(-54, 52)
turtle_tale(-53, 50)


turtle.done()
