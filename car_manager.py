from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
BORDER = "black"
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.initial_speed = STARTING_MOVE_DISTANCE

    def createCar(self):
        chance = random.randint(1, 4)  # To create the cars less frequently so that there is space for turtle movement
        if chance == 1:
            new_car = Turtle()
            new_car.speed("fastest")
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(BORDER, random.choice(COLORS))
            random_y = random.randint(-230, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def moveCars(self):
        for car in self.all_cars:
            car.backward(self.initial_speed)

    def fasterCars(self):
        for car in self.all_cars:
            # This is to delete all the cars from a certain level after level is passed
            car.hideturtle()
            car.goto(-350, car.ycor())
            del car
        self.initial_speed += MOVE_INCREMENT
