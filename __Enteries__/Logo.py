from turtle import *
from random import *
from particles import make_parti,move_parti
import math
w = Screen()
w.bgcolor("black")
w.tracer(0)
siz = 30
psiz = 2
xwall = 500
ywall = xwall
safe = xwall/10
make_parti()
treem = ref = 0
ax = ay = 0
def multitask(rlm = 0):
    global ref
    if rlm == 0:
        if ref >= 5 : w.update() ; ref = 0
    elif rlm == 2 :
        if ref >= 7  : w.update() ; ref = 0
    else : w.update()
    move_parti()
    ref += 1
def turset(t) :
    t.pu()
    t.color("white")
    t.ht()
    t.pensize(psiz)


#treedetail
a = 30   ; b = 45  ; minpix = 5 ;
wmod = 3/5 ; dismod = (2/3,3/5) 
#######
def tree(x,y,s,st = 0,ax=-1,ay=-1,t = Turtle())   :
    global treem
    zzz = s*wmod  ; zz = randint(a,b)  ; z  = choice(dismod)*x
    if st == 1: t.seth(90)  ; turset(t) ; treem += 5    
    if not( ax == -1 and ay == -1):t.goto(ax,ay) ; treem += 1
    t.pd() ; t.width(s)    ; t.fd(x) ; t.lt(y)
    if z > minpix : tree(z,zz,zzz) ; treem += 1#LEFT   BRANCHING 
    t.rt(2*y) 
    if z > minpix : tree(z,zz,zzz) ; treem += 1#RIGHT  BRANCHING
    t.lt(y)
    if z > minpix : tree(z,zz,1.5*zzz) ; treem += 1#CENTER BRANCHING
    t.pu() ; t.bk(x)       ;     multitask(2)
    treem += 7
    if st == 1 :
        t.clear()
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
def Y(x=0,y=0,t = Turtle(),tt = Turtle(),z = siz) :
    T = (t,tt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(t.towards(x+z/2,y))
    tt.goto(x+z,y+z)   ; tt.setheading(tt.towards(x+z/2,y))
    for _ in T       : _.pd()
    for _ in range(int(9*z/8)):
        t.fd(1)
        tt.fd(2)
##        if _ < z*math.sin(math.radians(t.towards(x,y))) : t.fd(1)
##        if _ < 2*z*math.sin(math.radians(tt.towards(x,y))) : tt.fd(1)
        multitask()
#T R A N Q U I L L I T Y
#^ ^ ^ ^ ^ ^ ^ ^       ^
def tranquillity():
    global ax,ay
    logo = [T,R,A,N,Q,U,I,L,L,I,T,Y]
    z = siz*3/2
    l = 100
    x = -3*l
    y = 0
    for _ in logo :
        _(x,y)
        if   _ == T : x += z/2
        elif _ == N : x +=8*z/7 ; ax = x ; ay = y
        elif _ == Q : x +=8*z/7 
        else : x += z
tranquillity()
while True :
    ang = randint(20,45)
    dis = randint(siz,3*siz)
    tree(dis,ang,psiz,1,ax,ay+siz+psiz )


def B(x=0,y=0,t = Turtle(),tt = Turtle(),ttt = Turtle(),z = siz) :
    T = (t,tt,ttt)
    for _ in T       : turset(_)
    t.goto(x,y+z)    ; t.setheading(-90)
    tt.goto(x,y+z)   ; tt.setheading(0)
    ttt.goto(x,y)    ; ttt.setheading(ttt.towards(x+(3*z/4),y-z))
    for _ in T       : _.pd()
    for _ in range(360) :
        t.fd(z/180)
        if _ < 90 or _ > 270 : tt.circle(-z/2,3)
        else : tt.fd(z/180)
        if math.sin(math.radians(ttt.towards(x+(3*z/4),y-z)))*_ <= z : 
            ttt.fd(z/180)
        w.update()

