from turtle import *
w = Screen()
w.bgcolor("black")

t = Turtle()
t.color("white")
t.begin_poly() 
for _ in range(4) : 
    t.fd(100)
    t.rt(90) 
w.register_shape("A" , t.get_poly() ) 
t.shape("A")
t.color("white")
t.fillcolor("black") 
