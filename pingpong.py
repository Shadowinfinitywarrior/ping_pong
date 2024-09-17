import turtle
import pygame

# Initialize Pygame's sound mixer
pygame.mixer.init()

# Load sound files
bounce_sound = pygame.mixer.Sound("bounce.wav")
paddle_hit_sound = pygame.mixer.Sound("paddle_hit.wav")

# Set up the window
window = turtle.Screen()
window.title("Ping Pong Game with Sound")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)  # Stops window from updating, we will manually update

# Score variables
score_a = 0
score_b = 0

# Paddle A (Left side)
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)  # Paddle size
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B (Right side)
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)  # Paddle size
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball movement speed
ball.dy = -0.2

# Scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function to move paddle A up
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:  # Don't let paddle go off the screen
        y += 20
    paddle_a.sety(y)

# Function to move paddle A down
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:  # Don't let paddle go off the screen
        y -= 20
    paddle_a.sety(y)

# Function to move paddle B up
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:  # Don't let paddle go off the screen
        y += 20
    paddle_b.sety(y)

# Function to move paddle B down
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:  # Don't let paddle go off the screen
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")  # Paddle A up
window.onkeypress(paddle_a_down, "s")  # Paddle A down
window.onkeypress(paddle_b_up, "Up")  # Paddle B up
window.onkeypress(paddle_b_down, "Down")  # Paddle B down

try:
    # Main game loop
    while True:
        window.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1  # Reverse direction
            pygame.mixer.Sound.play(bounce_sound)  # Play wall bounce sound

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1  # Reverse direction
            pygame.mixer.Sound.play(bounce_sound)  # Play wall bounce sound

        if ball.xcor() > 390:
            ball.goto(0, 0)  # Reset ball position
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
            ball.goto(0, 0)  # Reset ball position
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions
        if (340 < ball.xcor() < 350) and (paddle_b.ycor() - 50 < ball.ycor() < paddle_b.ycor() + 50):
            ball.setx(340)
            ball.dx *= -1  # Reverse direction
            pygame.mixer.Sound.play(paddle_hit_sound)  # Play paddle hit sound

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() - 50 < ball.ycor() < paddle_a.ycor() + 50):
            ball.setx(-340)
            ball.dx *= -1  # Reverse direction
            pygame.mixer.Sound.play(paddle_hit_sound)  # Play paddle hit sound

except turtle.Terminator:
    print("Game terminated")
