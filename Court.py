import turtle
wn=turtle.Screen()
wn.screensize(1100,700)
def drawcourt(turtle, wid,len, dashnum):
    turtle.teleport(-wid/2,-len/2)
    turtle.fd(wid)
    turtle.teleport(-wid/2,len/2)
    turtle.fd(wid)
    turtle.teleport(0,len/2)
    turtle.setheading(270)
    for i in range(dashnum):
        turtle.fd(len/(dashnum+(dashnum-1)))
        turtle.penup()
        turtle.fd(len/(dashnum+(dashnum-1)))
        turtle.pendown()
