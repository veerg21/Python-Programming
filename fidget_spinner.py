from turtle import *
# t=Turtle()
# s=Screen()
# s.title("Fidget Spinner")
# s.bgcolor("gold")
# t.shape("turtle")
# t.color("silver")
# done()
turn=0
def spinner():
    clear()
    angle=turn/10
    right(angle)
    forward(100)
    dot(120, "blue")
    back(100)
    right(120)
    forward(100)
    dot(120, "magenta")
    back(100)
    right(120)
    forward(100)
    dot(120, "yellow")
    back(100)
    right(120)
    update()
def animate():
    global turn
    if turn>0:
        turn=turn-0.5
    spinner()
    ontimer(animate, 10)
def flick():
    global turn
    turn+=10
    pass
setup(420, 420)
tracer(False)
width(20)
onkey(flick, "space")
listen()
animate()
done()