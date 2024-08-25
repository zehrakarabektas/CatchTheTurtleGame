import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")

score = 0
score_display = turtle.Turtle()
score_display.penup()
score_display.goto(-40, 250)
score_display.color("dark blue")
score_display.hideturtle()
score_display.write(f"SCORE: {score}",move=False, font=("Arial", 16, "normal"))

turtle_object = turtle.Turtle()
turtle_object.penup()
turtle_object.shape("turtle")
turtle_object.color("DarkGreen")
turtle_object.shapesize(stretch_wid=2, stretch_len=2, outline=2)
turtle_object.speed(0)

level_display = turtle.Turtle()
level_display.color("red")
level_display.penup()
level_display.goto(-40, 280)
level_display.hideturtle()
level_display.write(f"LEVEL: {1}",move=False, font=("Arial", 16, "normal"))

def turtle_draw():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    turtle_object.goto(x, y)
    turtle_object.showturtle()

def update_score(x, y):
    global score
    if turtle_object.distance(x, y) < 20:
        score += 1
        score_display.clear()
        score_display.write(f"SCORE: {score}",move=False, font=("Arial", 16, "normal"))

def end_game(message):
    turtle_object.hideturtle()
    score_display.goto(-50, 220)
    score_display.color("black")
    turtle_draw()
    score_display.write(message,move=False, font=("Arial", 16, "normal"))

def game_level(message):
    turtle_object.hideturtle()
    level_display.goto(-40, 280)
    turtle_draw()
    level_display.write(message,move=False, font=("Arial", 16, "normal"))
drawing_board.onscreenclick(update_score)

level=5
turtle_num=20
turtle_speed=400
turtle_next_speed=50
for i in range(1, level + 1):
    for j in range(turtle_num):
        turtle_draw()
        drawing_board.update()
        turtle.delay(turtle_speed)
    game_level(f"LEVEL: {i}")
    turtle.delay(500)
    turtle_speed-=turtle_next_speed
    if score == 10:
        end_game("CONGRATULATIONS")
    elif score < 10:
        end_game("GAME OVER")
        break
turtle.mainloop()

