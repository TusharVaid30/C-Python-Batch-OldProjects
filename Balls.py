from turtle import *
import random
w = Screen()
w.bgcolor("black")
w.tracer(0)
Xwall = 200
Ground = -150
Grav = 0.02
Wind = 0#0.005
Balls = []
Ball = 0 
def Add(x , y) :
    if x > Xwall or x < -Xwall : return
    if y < Ground or y > -Ground : return 
    global Ball 
    Balls.append(Turtle())
    Balls[Ball].color("darkgreen")
    Balls[Ball].shape("circle")
    Balls[Ball].pu()
    Balls[Ball].goto(x,y)
    if False : #Ball == 0 :
        Balls[Ball].dx = 0
        Balls[Ball].dy = 0 #int(input())#0.001
        Balls[Ball].cc = False
    else :
        Balls[Ball].dx = random.randint(-50,50)/100
        Balls[Ball].dy = random.randint(-50,50)/100
        Balls[Ball].cc = True
    Balls[Ball].nn = Ball 
    Ball += 1
#for _ in range(1) : Add( random.randint(-Xwall , Xwall) , random.randint(0,200) ) 
#Add( 0 , 0 )
#Add( 100 , 0 )
listen()
onscreenclick(Add)
def com( A , B ) :
    B_x = int(B.xcor())
    B_y = int(B.ycor())
    B_w = int(B.shapesize()[0]*10)
    if int(A.xcor()) in range (B_x - B_w , B_x + B_w ) :
        if int(A.ycor()) in range ( B_y - B_w , B_y + B_w ) : 
            return 1
    return 0
while True :
    #Wind = 0.005*random.randint(-10,10)
    for _ in Balls :
        _.sety(_.ycor() - _.dy)
        _.setx(_.xcor() - _.dx)
        if _.cc :
            _.dy += Grav
            _.dx += Wind
        if _.ycor() <= Ground : _.dy *= -1
        if _.xcor() <= -Xwall : _.dx *= -1
        if _.xcor() >= Xwall  : _.dx *= -1
        for __ in Balls :
            if _.nn != __.nn :
                if com(_ , __) : _.dy *= -1 ; _.dx *= -1
    w.update()
    
        
