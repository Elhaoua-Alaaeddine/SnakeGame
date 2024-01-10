from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover
import time

s = Screen()
s.listen()
f = Food()
score = Scoreboard()
s.setup(600, 600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)
snake = Snake(s)
s.onkey(snake.left, "a")
s.onkey(snake.right, "d")
s.onkey(snake.up, "w")
s.onkey(snake.down, "s")

done = False
score.write_score()
while not done:
    snake.move()
    s.update()
    time.sleep(0.1)
    if snake.head.distance(f) < 15:
        snake.add()
        f.refresh()
        score.refresh()
    if snake.head.xcor() > 270 or snake.head.xcor() < -270 or snake.head.ycor() > 270 or snake.head.ycor() < -270:
        done = True
        g = Gameover()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            done = True
            g = Gameover()
s.exitonclick()
