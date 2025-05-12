import turtle
import Court
import random as r
fontset=("Arial",80,"bold")
wn=turtle.Screen()
lines=turtle.Turtle(visible=False)
wn.screensize(1100,700)
wn.addshape("ball.gif")
ball=turtle.Turtle()
ball.shape("ball.gif")
ball.penup()
ball.speed(30)
if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))
else:
    ball.seth(r.randint(150,210))
leftpoints=0
#left player or player blue
leftPlayer = turtle.Turtle("square")
leftPlayer.color("blue")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
leftPlayer.setx(-1800/2+10)

lscore=turtle.Turtle(visible=False)
lscore.color("blue")
lscore.speed(0)
lscore.teleport(-250,250)
lscore.write(leftpoints,font=fontset)
rightpoints=0
#left player or player blue
rightPlayer = turtle.Turtle("square")
rightPlayer.color("orange")
rightPlayer.penup()
rightPlayer.speed(6)
rightPlayer.turtlesize(4,1)                   #turtlesize will stretch the turtle
rightPlayer.setx(1800/2-10)

rscore=turtle.Turtle(visible=False)
rscore.color("orange")
rscore.speed(0)
rscore.teleport(250,250)
rscore.write(rightpoints,font=fontset)
def reset():
    global rightpoints, leftpoints
    rscore.teleport(250,250)
    lscore.teleport(-250,250)
    rightpoints=0
    leftpoints=0
    ball.teleport(30)
    ball.speed(30)

def leftup():
    if leftPlayer.ycor()<420:
        leftPlayer.sety(leftPlayer.ycor()+40)
def leftdown():
    if leftPlayer.ycor()>-420:
        leftPlayer.sety(leftPlayer.ycor()-40)
def rightup():
    if ball.ycor()>rightPlayer.ycor() and ball.xcor()>0:
        rightPlayer.sety(rightPlayer.ycor()+40)
    wn.ontimer(rightup,200)
def rightdown():
    if ball.ycor()<rightPlayer.ycor() and ball.xcor()>0:
        rightPlayer.sety(rightPlayer.ycor()-40)
    wn.ontimer(rightdown,200)
def rest():
    ball.teleport(0,0)
    if r.randint(0,1)==0:
        ball.seth(r.randint(-30,30))
    else:
        ball.seth(r.randint(150,210))
    ball.speed(30)
def ballmove():
    paddlecollide()
    ballcolide()
    ball.fd(20)
    wn.ontimer(ballmove,20)
    
    
def paddlecollide():
    if ball.distance(leftPlayer)<=40 or ball.distance(rightPlayer)<=40:
        ball.seth(180-ball.heading())
        if ball.xcor()>0:
            ball.setx(ball.xcor()-5)
        else:
            ball.setx(ball.xcor()+5)
        ball.fd(10)
        fast=r.randint(0,5)
        if fast==1:
            ball.speed(60)
    
    
def ballcolide():
    global leftpoints,rightpoints
    if abs(ball.ycor()) > 475:
        ball.setheading(-ball.heading())
    if ball.xcor()>900:
        rest()
        leftpoints+=1
        lscore.clear()
        lscore.write(leftpoints,font=fontset)
        if leftpoints==7:
            ball.speed('none')
            lscore.teleport(0,0)
            lscore.write('Left wins!\n Hit space to reset.',font=fontset)
    elif ball.xcor()<-900:
        rest()
        rightpoints+=1
        rscore.clear()
        rscore.write(rightpoints,font=fontset)
        if rightpoints==7:
            ball.speed('none')
            rscore.teleport(0,0)
            rscore.write('Right wins!\n Hit space to reset.',font=fontset)
Court.drawcourt(lines,1800,950,12)
ballmove()

wn.onkeypress(leftup,"Up")
wn.onkeypress(leftdown,"Down")
wn.ontimer(rightdown,40)
wn.ontimer(rightup,40)
wn.listen()
wn.mainloop()
