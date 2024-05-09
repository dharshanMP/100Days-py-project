from turtle import Turtle, Screen

mikkey = Turtle()
mikkey.shape("turtle")
screen = Screen()


def move():
    #mikkey.forward(30)
    mikkey.circle(30)

screen.listen()
#screen.onkey(key ="space" ,fun = move )
screen.onkey(key = "space", fun= move)
screen.exitonclick()