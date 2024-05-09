import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

mikkey = Player()
cars_manage = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(mikkey.moving, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars_manage.create_car()
    cars_manage.move_cars()

    # collision of car 
    for car in cars_manage.cars:
        if car.distance(mikkey) < 27:
            game_is_on = False
            score_board.game_over()

    # finishing line

    if mikkey.ycor() > 280:
        mikkey.goto(0, -280)
        cars_manage.level_up()
        score_board.score_increase()
        

screen.exitonclick()