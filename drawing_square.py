import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    windows = turtle.Screen()
    #window.bgcolor("red")
    # create the turtle brad that draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    windows.exitonclick()

draw_art()

"""
def draw_square():
    # screen in which turtle works 
    windows = turtle.Screen()
    #windows.bgcolor("red")
    
    # to draw we need use below command assigned to brad 
    brad = turtle.Turtle()
    # move forward 100 is digit or steps 
    brad.forward(100)
    # repeat this for other sides trun 90 degrees angle
    brad.right(90)
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(2)


    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    brad.forward(100)
    brad.right(90)

    # draw a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("red")
    angie.circle(100)


    # close the whindow when clicked on it
    windows.exitonclick()


draw_square()
"""
