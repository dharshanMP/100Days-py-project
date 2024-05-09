from turtle import Turtle, Screen

mikkey = Turtle()
mikkey.shape("turtle")
screen = Screen()

def W_direction():
    mikkey.forward(100) 

def S_direction():
    mikkey.back(100)

def A_direction():
    new_heading = mikkey.heading() + 10
    mikkey.setheading(new_heading)


def D_direction():
    new_heading = mikkey.heading() - 10
    mikkey.setheading(new_heading)

def erase():
    screen.clear()

screen.listen()
screen.onkey(key = "w", fun = W_direction)
screen.onkey(key = "s", fun = S_direction)
screen.onkey(key = "a", fun = A_direction)
screen.onkey(key = "d", fun = D_direction)
screen.onkey(key = "c", fun = erase)









screen.exitonclick()