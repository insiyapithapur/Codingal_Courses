import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Drawing Shapes Using Turtle")
screen.setup(700, 500)

# Create turtle
board = turtle.Turtle()
board.speed(3)
board.pensize(3)


# Draw a triangle
board.penup()
board.goto(-250, 100)
board.pendown()

for i in range(3):
    board.forward(100)
    board.left(120)


# Draw a square
board.penup()
board.goto(-50, 100)
board.pendown()

for i in range(4):
    board.forward(100)
    board.left(90)


# Draw a rectangle
board.penup()
board.goto(150, 100)
board.pendown()

for i in range(2):
    board.forward(150)
    board.left(90)
    board.forward(80)
    board.left(90)


# Draw a star
board.penup()
board.goto(-50, -150)
board.pendown()

for i in range(5):
    board.forward(150)
    board.right(144)


# Hide turtle after drawing
board.hideturtle()

# Keep the window open
turtle.done()