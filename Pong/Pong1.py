import turtle

wn = turtle.Screen()
wn.title("Pong by Leila")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)  # no automatic updates - makes game faster

# Main game loop
while True:
    wn.update() # update the screen for each loop run
    