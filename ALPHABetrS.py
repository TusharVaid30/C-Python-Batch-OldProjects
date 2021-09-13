from turtle import *
import math
w = Screen()
w.tracer(0)
siz = 20
def turset(t) : t.ht() ; t.color("black") ; t.pu() 
def multitask() : w.update()

def A(x=0,y=0,t = Turtle(),tt = Turtle(),ttt = Turtle(),z = siz) :
    T = (t,tt,ttt)
    for _ in T       : turset(_)
    t.goto(x,y+z)         ; t.setheading(t.towards(x+(z/2),y-z))
    tt.goto(x-(z/2),y-z)  ; tt.setheading(tt.towards(x,y+z))
    ttt.goto(x+(z/4),y)   ; ttt.setheading(ttt.towards(x-(z/4),y))
    for _ in T       : _.pd()
    for _ in range(2*z) :
        if _ == 0 or _ == z : t.fd(2.5*z/50)
        t.fd(1)
        tt.fd(1)
        if _ <= 7*z/8 : ttt.fd(1)
        multitask()
def I(x=0,y=0,t = Turtle(),tt = Turtle(),ttt = Turtle(),z = siz) :
    T = (t,tt,ttt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(-90)
    tt.goto(x-(z/2),y+z) ; tt.setheading(0)
    ttt.goto(x+(z/2),y-z); ttt.setheading(180)
    for _ in T       : _.pd()
    for _ in range(2*z):
        t.fd(1)
        if _ < z : tt.fd(1) ; ttt.fd(1)

        multitask()
def L(x=0,y=0,t = Turtle(),tt = Turtle(),z = siz) :
    T = (t,tt)
    for _ in T       : turset(_)
    t.goto(x-(z/2),y+z)    ; t.setheading(-90)
    tt.goto(x+(z/2),y-z) ; tt.setheading(180)
    for _ in T       : _.pd()
    for _ in range(2*z):
        t.fd(1)
        if _ < z : tt.fd(1)
        multitask()
def N(x=0,y=0,t = Turtle(),tt = Turtle(),ttt = Turtle(),z = siz) :
    T = (t,tt,ttt)
    for _ in T       : turset(_)
    t.goto(x-(z/2),y+z)   ; t.setheading(t.towards(x-(z/2),y-z))
    tt.goto(x+(z/2),y-z)  ; tt.setheading(tt.towards(x+(z/2),y+z))
    ttt.goto(x+(z/2),y-z) ; ttt.setheading(ttt.towards(x-(z/2),y+z))
    for _ in T       : _.pd()
    for _ in range(2*z) :
        #if _ == 0 or _ == z : t.fd(2.5*z/50)
        t.fd(1)
        tt.fd(1)
        if math.sin(math.radians(ttt.towards(x-(z/2),y+z)))*_ <= 2*z : 
            ttt.fd(1.12)
        multitask()
def Q(x=0,y=0,t = Turtle(),tt = Turtle(),z = siz) :
    T = (t,tt)
    ang = 45
    exten = z/10
    for _ in T       : turset(_)
    t.goto(x,y)      ; t.setheading(-ang)
    tt.goto(x,y-z) ; tt.setheading(0)
    for _ in T       : _.pd()
    for _ in range(360):
        if _ < 360*z*math.sin(math.radians(ang)) : t.fd(z/360) ; t.fd(siz/1000)
        tt.circle(z,1)
        if _%5 == 0 : multitask()
        
def R(x=0,y=0,t = Turtle(),tt = Turtle(),ttt = Turtle(),z = siz) :
    T = (t,tt,ttt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(-90)
    tt.goto(x,y+z)   ; tt.setheading(0)
    ttt.goto(x,y)    ; ttt.setheading(ttt.towards(x+(3*z/4),y-z))
    for _ in T       : _.pd()
    for _ in range(360) :
        t.fd(z/180)
        if _ > 90 and _ < 270 : tt.circle(-z/2,1)
        else : tt.fd(z/180)
        if math.sin(math.radians(ttt.towards(x+(3*z/4),y-z)))*_ <= z : 
            ttt.fd(z/180)
        if _%5 == 0 : multitask()

def T(x=0,y=0,t = Turtle(),tt = Turtle(),z = siz) :
    T = (t,tt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(-90)
    tt.goto(x-(z/2),y+z) ; tt.setheading(0)
    for _ in T       : _.pd()
    for _ in range(2*z):
        t.fd(1)
        if _ < z : tt.fd(1)
        multitask()


def U(x=0,y=0,t = Turtle(),z = siz) :
    turset(t) 
    t.goto(x-(z/2),y+z)      ; t.setheading(-90)
    t.pd()
    zl = z/2
    for _ in range(int(z+zl)):
        t.fd(1)
        if _%2 == 0 : multitask()
    for _ in range(180) :
        t.circle(zl,1)
        if _%5 == 0 : multitask()
    for _ in range(int(z+zl)):
        t.fd(1)
        if _%2 == 0 : multitask()

def Y(x=0,y=0,t = Turtle(),tt = Turtle(),z = siz) :
    T = (t,tt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(t.towards(x+z/2,y))
    tt.goto(x+z,y+z)   ; tt.setheading(tt.towards(x+z/2,y))
    for _ in T       : _.pd()
    for _ in range(int(9*z/8)):
        t.fd(1)
        tt.fd(2)

out = [ T , R , Y , A , L , I , N , Q , U ]
__ = - 50
for _ in out : _(__) ; __ += 45
