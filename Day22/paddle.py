from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position) :
        super().__init__()
        self.shape("square")
        self.color("gray")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(position)


    def upward(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def downward(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)    