from turtle import Turtle
POSITION = (-235, 270)
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(POSITION)
        self.color("black")
        self.level = 0
        self.updateLevel()

    def showLevel(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def updateLevel(self):
        self.showLevel()
        self.level += 1

    def gameOver(self):
        self.home()
        self.write(arg="GAME OVER!", align=ALIGNMENT, font=FONT)