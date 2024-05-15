import turtle
import pandas

screen = turtle.Screen()
screen.title("State_Finding Game")
image = "TN_map_2.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("TN_Districts.csv")
all_districts = data.Districts.to_list()
guess = []

while len(guess) < 32:
    answer = screen.textinput(title=f"{len(guess)}/32 Guess the state", prompt="what's the next state? ").title()
    print(answer)

    if answer == "Exit":
        break
    if answer in all_districts:
        tut = turtle.Turtle()
        tut.hideturtle()
        tut.penup()
        district_data = data[data.Districts == answer] 
        tut.goto(int(district_data.x), int(district_data.y))
        tut.write(answer, align = "center")
        guess.append(answer)



