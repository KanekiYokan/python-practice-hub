import time
import turtle
from snake import Snake
from food import Food

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
## Game
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right , "Right")


game_on = True

while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    # Colision Detection
    if snake.head.distance(food) < 15:
        food.refresh()



screen.exitonclick()