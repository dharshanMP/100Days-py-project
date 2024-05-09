from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_input = screen.textinput(title = "Make your bet", prompt = "Which turtle will win ? enter the color : ")
colors = (["blue", "red", "brown", "green", "purple", "black"])
y_pos = [-70, -40, -10, 20, 50, 80] 
all_turtles = []

for turtle_pos in range(0,6):
    new_turtle = Turtle(shape = "turtle",)
    new_turtle.penup()
    new_turtle.color(colors[turtle_pos])
    new_turtle.goto(x = -230, y = y_pos[turtle_pos])
    all_turtles.append(new_turtle)

if user_input:
    race_on = True


while race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input :
                print(f"You've won! the race! {winning_color} turtle is the winner.")
            else:
                print(f"Oops!... you lose! {winning_color} won turtle the race.")
        turtle.forward(random.randint(0,10))


screen.exitonclick()