# Turtle Crossing

# Simplified version of crossy road game, where the character has to avoid the traffic and cross the road

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.bgcolor("white")
my_screen.title("Turtle Crossing")
my_screen.setup(width=600, height=600)
my_screen.tracer(False)

my_player = Player()
my_level = Scoreboard()
my_car_manager = CarManager()

my_screen.listen()
my_screen.onkey(fun=my_player.moveTutle, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    my_screen.update()
    my_car_manager.createCar()
    my_car_manager.moveCars()
    # Detecting whether turtle has crossed the road or not
    if my_player.ycor() > 280:
        my_player.resetTurtle()
        my_car_manager.fasterCars()
        my_level.updateLevel()

    # Detecting collision of turtle with car
    # Detecting collision of snake with food
    for car in my_car_manager.all_cars:
        if my_player.distance(car) < 25:
            game_is_on = False
            my_level.gameOver()

my_screen.exitonclick()
