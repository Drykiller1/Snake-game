from turtle import *
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

highest_score = Scoreboard()
highest_score.highest_score_board_location()
scoreboard = Scoreboard()
scoreboard.score_board_location()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

snake_head = snake.x_list[0]

game_is_on = True
while game_is_on:
    scoreboard.update_scoreboard()
    snake.move()
    screen.update()
    snake.allow_key_press = 1
    time.sleep(0.1)
    if snake_head.distance(food) < 15:
        scoreboard.ate_apple()
        snake.add_seg()
        food.refresh(snake.x_list)

    if snake_head.xcor() >= 300 or snake_head.ycor() >= 300 or snake_head.ycor() <= -300 or snake_head.xcor() <= -300:
        game_is_on = False
        scoreboard.game_over()

    for seg in snake.x_list:
        if seg == snake_head:
            pass
        elif snake_head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()
highest_score.keep_score(scoreboard.score)
screen.exitonclick()
