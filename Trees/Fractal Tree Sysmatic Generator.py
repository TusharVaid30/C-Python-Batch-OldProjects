from turtle import *
from random import *
from random import randint as r
from random import choice as c
def mod(a):
    return a*2/3
def nod(b):
    return b+bb
def col(lv):
    if lv >5 :
        t.color(c3)
    elif lv > 3 :
        t.color(c2)
    elif lv > 1 :
        t.color(c1)
#-------------------------------------------------
w = Screen()
w.bgcolor("black")
w.tracer(0)
t = Turtle();t.speed(0);t.ht();t.lt(90);t.pu();t.goto(0,-300);t.pd()
#++++++++++++++++++++++++++++++
def treel(x,y,lv=0) :
    t.write(lv)
    t.fd(x)
    t.rt(y)
    u = mod(x)
    v = nod(y)   
    if u > mx :
        treel(u,v,lv+1)   
    t.lt(2*y)
    if u > mx :
        treel(u,v,lv+1)
    t.rt(y)
    col(lv)
    t.bk(x)
    w.update()
#############
def treer(x,y,lv=0) :
    #t.write(lv)
    t.fd(x)
    t.lt(y)
    u = mod(x)
    v = nod(y)   
    if u > mx :
        treer(u,v,lv+1)   
    t.rt(2*y)
    if u > mx :
        treer(u,v,lv+1)
    t.lt(y)
    col(lv)
    t.bk(x)
    w.update()
#++++++++++++++++++++++++++++++
#--------------------------------------------------------------------------------------------------------------------------
colors=("lightgreen","blue","pink","red")
mmm=(2/3,3/4,4/5,5/6)
c1 = c(colors)
c2 = c(colors)
c3 = c(colors)

bb=r(1,5)
mm = 2/3
mx= 15
treel(100,30)
exitonclick()
while True :
    c1 = c(colors)
    c2 = c(colors)
    c3 = c(colors)

    bb=r(1,5)
    mx=r(10,20)
    mm=c(mmm)
    p = r(100,150)
    q = r(15,45)
    arrr = r(1,2)
    if  arrr == 1 :
        treel(p,q)
    if arrr == 2 :
        treer(p,q)
        
    












    

