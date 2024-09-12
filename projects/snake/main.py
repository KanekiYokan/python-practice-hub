import time
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

## screen parameters
screen = turtle.Screen()
screen.setup(width = 1.0, height = 1.0) # max res
screen.bgcolor("black")
screen.title("My Snake Game")


## removing window buttons
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(True)

screen.tracer(0)

## Game Objects
snake = Snake()
food = Food()
score = Scoreboard()

## Game Keybinds
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.02)
    snake.move()

    #  Collision Detection with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add()
        snake.grow()

    # Collision Detection with Wall
    if snake.head.xcor() > 945 or snake.head.xcor() < -945 or snake.head.ycor() > 537 or snake.head.ycor() < -537:
        game_on = False
        score.gameover()

    #  Collision Detection with Tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.gameover()


screen.exitonclick()