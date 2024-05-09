# Turtle

from turtle import Turtle, Screen

tut = Turtle()
print(tut)
tut.shape("turtle")
tut.color("tan3")
tut.forward(200)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
#------------------------------------------------------------------

#Table

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Team Name", ["CSK", "MI", "RCB", "DC", "GT", "SRH"])
table.add_column("Captain", ["Dhoni", "Rohit", "virat", "Pant", "Hardik", "Cummins"])

table.align = "l"

print(table)