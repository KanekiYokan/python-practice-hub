from turtle import Turtle
ALIGNMENT= "center"
SCORE_FONT= ("Arial", 25, "normal")
GO_FONT= ("Arial", 32, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,480)
        self.hideturtle()
        self.speed(0)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    def add(self):
        self.score+=1
        self.clear()
        self.write_score()

    def gameover(self):
        self.goto(0,0)
        self.write(f"GAME OVER! Score: {self.score}", align=ALIGNMENT, font=GO_FONT)