import turtle
wn=turtle.Screen()
wn.screensize(1100,700)
ball=turtle.Turtle("square")
ball.penup()
ball.speed(0)
ball.setheading(90)
def rest():
    ball.teleport(0,0)
def ballmove():
    ballcolide()
    ball.fd(20)
    wn.ontimer(ballmove,20)
def ballcolide():
    if abs(ball.ycor()) > 300:
        ball.setheading(ball.heading()-230)
    if abs(ball.xcor())>500:
        rest()
ballmove()


wn.onkeypress(rest,"r")
wn.listen()
wn.mainloop()