import turtle

def draw_equilateral_triangle(side_length):

    for x in range(3):

        turtle.forward(side_length)

        turtle.left(120)

draw_equilateral_triangle(100)

turtle.done()

