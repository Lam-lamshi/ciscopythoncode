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

# Draw X's and O's on the board
def draw_x(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.left(45)
    pen.forward(70.7)
    pen.penup()
    pen.goto(x, y)
    pen.right(90)
    pen.pendown()
    pen.forward(70.7)

def draw_0(x, y):
    pen.penup()
    pen.goto(x, y-70.7)
    pen.pendown()
    pen.circle(35.35)

# Set up the game loop
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player = "X"
draw_board()

def get_square(x, y):
    col = (int(x) + 100) // 100
    row = 3 - (int(y) + 100) // 100
    return row * 3 + col

def click(x, y):
    global player
    square = get_square(x, y)
    if board[square] == " ":
        if player == "X":
            draw_x((col -1)*100, (row-1)*100)
            board[square] = "X"
            player = "O"
        else:
            draw_0:((col-1)*100, (row-1)*100)
            board[square] = "O"
            player = "X"

turtle.onscreenclick(click)

turtle.mainloop()
my_dict= {'key1':17,'key2':19,'key3':22}
print(my_dict["key3"])
print(my_dict.get("key2"))
mylist=[1,2,3,4,5]
mylist.append(7)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(0)
print(mylist)
mylist=[1,2,3,4]
mylist.reverse()
print(mylist)
my_dict={'key1':'value1','key2':'value2'}
print(my_dict)
my_dict.keys()
print(my_dict)
my_dict.values()
print(my_dict)
my_dict.items()
print(my_dict)
