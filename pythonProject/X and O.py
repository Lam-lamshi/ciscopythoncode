import turtle

# Set up the turtle window and pen
window = turtle.Screen()
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

# Draw the game board
def draw_board():
    pen.penup()
    pen.goto(-100, 60)
    pen.pendown()
    pen.forward(200)
    pen.penup()
    pen.goto(-100, 0)
    pen.pendown()
    pen.forward(200)
    pen.penup()
    pen.goto(-60, 100)
    pen.pendown()
    pen.left(90)
    pen.forward(200)
    pen.penup()
    pen.goto(60, 100)
    pen.pendown()
    pen.forward(200)
    pen.penup()

# Set up the game loop
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
draw_board()

turtle.mainloop()
