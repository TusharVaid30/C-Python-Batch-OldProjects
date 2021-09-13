from turtle import *

lwall = -500
rwall = - lwall
ground = -300
roof = - ground
w = Screen()
w.setup(2*rwall,2*roof)
w.bgcolor("black")
t = Turtle()
t.color("white")
t.speed("slowest")
s = 0
ms = 0.9
mns =-0.5
w.tracer(0)
def xfd() :
    global s
    if s < ms :
        s += 0.1
def xrt() :
    t.rt(30)
def xlt() :
    t.lt(30)
def xbk() :
    global s
    if s > mns :
        s -= 0.1
def xprint():
    t.write(str(10*s)+"Km/h")
def xclear():
    t.clear()
def xquit():
    bye()
flag = 1
def xhelp() :
    t.write("""Up for speed+, Max Speed = 10Km/h
Down for speed-, Max Reverse = 5Km/h
Left for wheel left, 30 degree
Right for wheel right, 30 degree
q to quit
e to clearscreen
r to notify current speed at position""")
xhelp()
while True :
    w.update()
    t.fd(s)
    onkey(xfd,"Up")
    onkey(xrt,"Right")
    onkey(xlt,"Left")
    onkey(xbk,"Down")
    onkey(xprint,"r")
    onkey(xclear,"e")
    onkey(xquit,"q")
    onkey(xhelp,"f")
    if t.xcor() < lwall :
        t.pu()
        t.setx(rwall)
        t.pd()
    if t.xcor() > rwall :
        t.pu()
        t.setx(lwall)
        t.pd()
    if t.ycor() < ground :
        t.pu()
        t.sety(roof)
        t.pd()
    if t.ycor() > roof :
        t.pu()
        t.sety(ground)
        t.pd()
    if flag%100000 == 0 :
        t.clear()
    flag+= 1
    listen()

