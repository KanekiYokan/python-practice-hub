from turtle import Turtle
ALIGNMENT= "center"
SCORE_FONT= ("Arial", 25, "normal")
GO_FONT= ("Arial", 32, "normal")
PATH = "..\snake-game\data.txt"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_hs()
        self.color("White")
        self.penup()
        self.goto(0,480)
        self.hideturtle()
        self.speed(0)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}. High Score: {self.high_score}", align=ALIGNMENT, font=SCORE_FONT)

    def add(self):
        self.score+=1
        self.write_score()

    def gameover(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.write_hs(self.high_score)
        self.score = 0
        self.write_score()

    def read_hs(self):
        with open(PATH, "r") as file:
            hs = file.read()
        return str(hs)

    def write_hs(self, hs):
        with open(PATH, "w") as file:
            file.write(str(hs))
