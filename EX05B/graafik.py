"""Draw graph of savings each month."""


import turtle


def draw_graph(pencil: turtle.Turtle, posx, posy, data_list):
    """
    Draw a bar chart-style graph and a legend describing the data.

    Arguments:
    pencil -- the turtle object used for drawing
    posx, posy -- start coordinates of the drawing
    data_list -- the data shown on the graph as a list of numeric values
    """
    turtle.pu()
    turtle.setpos(posx, posy)
    turtle.colormode(255)
    turtle.pensize(0.5)
    turtle.pencolor(11, 1, 0)
    draw_bars(pencil, data_list)
    draw_legend(pencil, data_list)
    turtle.up()


def draw_legend(pencil: turtle.Turtle, data_list):
    """
    Draw a legend box for a graph.

    The legend box contains text describing the data.
    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    month_names = ["Jaanuar", "Veebruar", "Märts", "Aprill", "Mai", "Juuni", "Juuli", "August", "September", "Oktoober", "November", "Detsember"]
    turtle.up()
    # Draw legend box
    turtle.forward(30)
    turtle.left(90)
    turtle.down()
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.forward(300)
    turtle.right(90)
    turtle.up()
    turtle.forward(285)
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    indeks = 0
    # Write months names and the according sum saved for that month
    for i in data_list:
        turtle.down()
        turtle.write("{}:   {} €".format(month_names[indeks], i))
        indeks += 1
        turtle.pu()
        turtle.back(20)
    # if enough money gathered, print the total and confirmation
    if len(data_list) == 12 and sum(data_list) >= 470:
        turtle.down()
        turtle.write("Total:   {} €".format(sum(data_list)))
        turtle.pu()
        turtle.back(20)
        turtle.pd()
        turtle.write("You can go to the concert!")
    turtle.pu()
    turtle.left(180)
    turtle.sety(-140)
    turtle.pd()


def draw_bars(pencil: turtle.Turtle, data_list):
    """
    Draw a bar chart.

    Arguments:
    pencil -- the turtle object used for drawing
    data_list -- the data as a list of numeric values
    """
    colours = ["red", "lightgreen", "orange", "blue", "yellow", "navyblue", "green", "pink", "brown", "purple", "grey", "black"]
    color = 0
    for i in data_list:
        turtle.speed("fast")
        turtle.down()
        turtle.color(colours[color])
        color += 1
        turtle.begin_fill()
        turtle.pencolor("black")
        turtle.left(90)
        turtle.forward(i)
        turtle.right(90)
        turtle.forward(30)
        turtle.right(90)
        turtle.forward(i)
        turtle.right(90)
        turtle.forward(30)
        turtle.end_fill()
        turtle.right(180)
        turtle.forward(30)
        turtle.up()


def main():
    """Set up the turtle window and start the drawing process."""
    data_list = [100, 50, 150, 300, 200, 100, 50, 150, 300, 200.9, 200, 300]
    turtle.setup(width=800, height=400)
    draw_graph(turtle, -350, -150, data_list)


if __name__ == "__main__":
    main()
    turtle.done()
