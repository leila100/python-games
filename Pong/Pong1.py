import turtle

wn = turtle.Screen()
wn.title("Pong by Leila")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # no automatic updates - makes game faster

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set speed to maximum possible speed
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # stretch the width to 5*20. Keep the len the same (20px) 
paddle_a.penup()  # don't draw movements
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set speed to maximum possible speed
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # stretch the width to 5*20. Keep the len the same (20px) 
paddle_b.penup()  # don't draw movements
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # set speed to maximum possible speed
ball.shape("square")
ball.color("white")
ball.penup()  # don't draw movements
ball.goto(0, 0)

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

# Main game loop
while True:
    wn.update() # update the screen for each loop run
