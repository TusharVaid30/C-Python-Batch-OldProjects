from turtle import *
t =  Turtle() ; t.lt(90)
t.pensize(20)
def  fo(x) :
    for z in range(x) :
        t.fd(1)
        if t.pensize() > 0.5 :
            t.pensize(t.pensize()- 0.1)
fo(1000)
