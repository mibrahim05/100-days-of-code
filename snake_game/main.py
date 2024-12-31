from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()

screen.setup(width=600,height=500)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard: Scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right,"Right")


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.xcor() > 300:
        snake.head.setx(-300)
    elif snake.head.xcor() < -300:
        snake.head.setx(300)
    if snake.head.ycor() > 250:
        snake.head.sety(-250)
    elif snake.head.ycor() < -250:
        snake.head.sety(250)


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 235 or snake.head.ycor() < -235:
       scoreboard.reset()
       snake.reset()

    #Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()

