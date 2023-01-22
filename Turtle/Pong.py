# Importing turtle

import turtle

# Window

window = turtle.Screen()
window.title("Pong")

window.bgcolor("black")
window.setup(width=800, height=600)

# User input
name = turtle.textinput("Name", "Enter a name")
if name == "":
    turtle.clear()
    ply_or_not = turtle.textinput()

# score
Score = 0

# player1

player1 = turtle.Turtle()
player1.shape("square")
player1.shapesize(stretch_wid=5, stretch_len=1)
player1.color("white")
player1.penup()
player1.speed(0)
player1.goto(-350, 0)

# player2

player2 = turtle.Turtle()
player2.shape("square")
player2.shapesize(stretch_wid=5, stretch_len=1)
player2.color("white")
player2.penup()
player2.speed(0)
player2.goto(350, 0)

# Pen
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("white")
pen.speed(0)
pen.goto(0, 260)
pen.write( name + "'s score:" + str(Score), align="center", font=("Courier", 24, "normal"))
pen2 = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color("white")
pen.speed(0)
pen.goto(0, 260)
pen.write( name + "'s score:" + str(Score), align="center", font=("Courier", 24, "normal"))

# functions
def player1_up():
    y = player1.ycor()
    y += 10
    player1.sety(y)

def player1_down():
    y = player1.ycor()
    y -= 10
    player1.sety(y)

def player2_up():
    y = player2.ycor()
    y += 10
    player2.sety(y)

def player2_down():
    y = player2.ycor()
    y -= 10
    player2.sety(y)

def play():
    player1.showturtle()
    player2.showturtle()
    ball.showturtle()
    ball.goto(0, 0)
    ball.dx *= -1
    pen.clear()
    pen.penup()
    pen.goto(0, 260)
    pen.write( name + "'s score:" + str(Score), align="center", font=("Courier", 24, "normal"))
    

# key binds
window.listen()
window.onkeypress(player1_up, "w")
window.onkeypress(player1_down, "s")
window.onkeypress(player1_up, "W")
window.onkeypress(player1_down, "S")
window.onkeypress(player2_up, "Up")
window.onkeypress(player2_down, "Down")
window.onkeypress(play, "p")


# ball
ball = turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.speed(0)
ball.dx = 3.5
ball.dy = 3.5

# main game loop
while True:
    window.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("white")
        ball.hideturtle()
        player1.hideturtle()
        player2.hideturtle()
        pen.goto(0, 0)
        pen.write("Game over", align="center", font=("Courier", 24, "normal"))
    
    if ball.xcor() < -390:
        pen2 = turtle.Turtle()
        pen2.hideturtle()
        pen2.color("white")
        ball.hideturtle()
        player1.hideturtle()
        player2.hideturtle()
        pen2.write("Game over", align="center", font=("Courier", 24, "normal"))
    # player and ball colision
    if  ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < player2.ycor() + 50 and ball.ycor() > player2.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        Score += 5
        
    if  ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < player1.ycor() + 50 and ball.ycor() > player1.ycor() - 50:
        ball.setx(-340)
        ball.dx *= -1
        Score += 5