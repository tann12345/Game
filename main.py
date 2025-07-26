import turtle
import random
import time

# Set up screen
screen = turtle.Screen()
screen.title("Click the Turtle Game!")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Score and time
score = 0
time_left = 30

# Turtle for game
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Turtle for score display
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write("Score: 0  Time: 30", align="center", font=("Arial", 16, "bold"))

# Move turtle to random location
def move_turtle():
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)
    player.goto(x, y)

# On click function
def click_handler(x, y):
    global score
    score += 1
    update_display()
    move_turtle()

# Update the score and timer display
def update_display():
    score_turtle.clear()
    score_turtle.write(f"Score: {score}  Time: {time_left}", align="center", font=("Arial", 16, "bold"))

# Countdown timer
def countdown():
    global time_left
    if time_left > 0:
        time_left -= 1
        update_display()
        screen.ontimer(countdown, 1000)
    else:
        player.hideturtle()
        score_turtle.goto(0, 0)
        score_turtle.write(f"Game Over!\nFinal Score: {score}", align="center", font=("Arial", 20, "bold"))

# Start game
player.onclick(click_handler)
move_turtle()
countdown()

# Main loop
screen.mainloop()
