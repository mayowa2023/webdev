import turtle
turtle.Screen().bgcolor("pink")

sc= turtle.Screen()
sc.setup(400,300)

turtle.title("Welcome to the turtle window")

board = turtle.Turtle()

for i in range(4):
    board.forward(100)
    board.left(90)

turtle.done()