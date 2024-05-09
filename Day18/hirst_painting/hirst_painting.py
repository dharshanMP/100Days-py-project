import turtle as tut
import random

mikkey = tut.Turtle()
mikkey.shape("turtle")
tut.colormode(255)
mikkey.penup()
mikkey.hideturtle()
mikkey.setheading(225)
mikkey.forward(300)
mikkey.setheading(0)
mikkey.speed("fastest")


color_list = [(233, 233, 236), (233, 232, 229), (234, 230, 233), (225, 233, 229), (45, 95, 147), (179, 46, 75), (227, 207, 101), (208, 156, 91), 
              (179, 169, 34), (118, 177, 207), (136, 89, 63), (199, 77, 122), (212, 131, 172), (228, 70, 50), (92, 104, 188), (47, 165, 120), 
              (124, 217, 208), (23, 156, 85), (52, 55, 91), (119, 47, 36), (121, 42, 71), (226, 171, 187), (40, 184, 195), (123, 188, 161), 
              (175, 186, 218), (232, 172, 163), (155, 207, 216), (212, 206, 40), (53, 52, 72), (46, 75, 79)]


for dot_count in range(1, 100-1):
    mikkey.dot(20, random.choice(color_list))
    mikkey.forward(50)

    if dot_count % 10 == 0:
        mikkey.setheading(90)
        mikkey.forward(50)
        mikkey.setheading(180)
        mikkey.forward(500)
        mikkey.setheading(0)
        


screen = tut.Screen()
screen.exitonclick()