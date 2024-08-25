import turtle
import random

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("Catch The Turtle")

score = 0
level_cath_turtle=0
score_display = turtle.Turtle()
score_display.penup()
score_display.goto(0, 250)
score_display.color("dark blue")
score_display.hideturtle()
score_display.write(f"SCORE: {score}",move=False,align="center", font=("Arial", 16, "normal"))
score_display.speed(0)

turtle_object = turtle.Turtle()
turtle_object.penup()
turtle_object.shape("turtle")
turtle_object.color("DarkGreen")
turtle_object.shapesize(stretch_wid=2, stretch_len=2, outline=2)
turtle_object.speed(0)

level_display = turtle.Turtle()
level_display.color("red")
level_display.penup()
level_display.goto(0, 280)
level_display.hideturtle()
level_display.write(f"LEVEL: {1}",move=False,align="center" ,font=("Arial", 16, "normal"))

message_display=turtle.Turtle()
message_display.penup()
message_display.hideturtle()

def turtle_draw():
    x = random.randint(-210, 210)
    y = random.randint(-210, 210)
    turtle_object.goto(x, y)
    turtle_object.showturtle()

def update_score(x, y):
    global score
    global level_cath_turtle
    if turtle_object.distance(x, y) < 20:
        score += 1
        score_display.clear()
        score_display.goto(0, 250)
        score_display.write(f"SCORE: {score}",move=False,align="center", font=("Arial", 16, "normal"))
        level_cath_turtle+=1

def end_game(message):
    turtle_object.hideturtle()
    message_display.penup()
    message_display.goto(0, 220)
    message_display.color("black")
    message_display.hideturtle()
    turtle_draw()
    message_display.write(message,move=False,align="center", font=("Arial", 16, "normal"))
    drawing_board.onscreenclick(None)

def game_level(message):
    turtle_object.hideturtle()
    level_display.goto(0, 280)
    level_display.clear()
    turtle_draw()
    level_display.write(message,move=False,align="center", font=("Arial", 16, "normal"))
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
    if level_cath_turtle == 10:
        end_game("CONGRATULATIONS")
        level_cath_turtle=0
        message_display.clear()
    elif level_cath_turtle < 10:
        end_game("GAME OVER")
        level_cath_turtle=0
        break
turtle.mainloop()

