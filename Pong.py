from turtle import *
from random import *
from time   import *
from funCCC import space
#---------------------------------------
ground      = -  300
roof        = -  ground
leftwall    = -  400
rightwall   = -  leftwall
safe0       =    100
safe1       =    60 # bat Max movement till roof or ground

groundmult  = 1
roofmult    = groundmult

leftplayer  = "AI HITLER"
rightplayer = "Player"

if len(leftplayer) > len(rightplayer) :
    rightplayer   += space(leftplayer,rightplayer) 
else :
    leftplayer    += space(rightplayer,leftplayer)
player = rightplayer

movement            = 100
Lbatup_key          = "w"
Lbatdown_key        = "s"
Rbatup_key          = "Up"
Rbatdown_key        = "Down"
byebye_key          = "q"
colorchange_key     = "e"
xspeedincrease_key  = "+"
xspeeddecrease_key  = "-"
yspeedincrease_key  = "8"
yspeeddecrease_key  = "2"

defaultballx = 0.3

frames       = 0
sec          = 0
tim          = time()
#---------------------------------------
colorpallet  = ["red"  ,"green","blue"  ,"yellow","orange","lightblue" ,"magenta","violet"
               ,"brown","cyan" ,"pink"  ,"white" ,"maroon","lightgreen","gold"   ,"silver"]

w = Screen()     ;  w.listen() ; w.tracer(0)
p = Turtle()     ;  p.ht()     ; p.pu()

pframes         = Turtle()     ; pframes.ht()   ; pframes.pu()
pkeyboard       = Turtle()     ; pkeyboard.ht() ; pkeyboard.pu()


Lbat            = Turtle()     ; Lbat.pu()      ; Lbat.shape("square")
Lbat.dm         = movement
Lbat.score      = 0
Lbat.multiplyer = 1
Lbat.safew      = 18  # bat width/2 ( -  2 for inward bounce )
Lbat.safeh      = 50 # bat height/2
Lbat.shapesize((2*Lbat.safeh/20),1)


Rbat            = Turtle() ; Rbat.pu() ; Rbat.shape("square")
Rbat.dm         = movement
Rbat.score      = 0
Rbat.multiplyer = 1
Rbat.safew      = 18  # bat width/2 ( -  2 for inward bounce )
Rbat.safeh      = 50 # bat height/2
Rbat.shapesize((2*Rbat.safeh/20),1)

yredumultiplyer = (1/10,1/9,1/4,1/5,1/6,1/7,1/8)
yincrmultiplyer = (4/3,5/4,6/5)
yholdmultiplyer = (1.1,0.9,0.7,1,0.8)
ball            = Turtle() ; ball.shape("circle") ; ball.pu()
ball.dy         = float(randint(10,40))/100
ball.dx         = float(randint(20,50))/100
#---------------------------------------

#FUNCTIONS------------------------------------------------------------------------------------------------------------

#AI----------------------------------------------------------------------
def Lai() :
    if ball.ycor() > Lbat.ycor() + Lbat.safeh and ball.dx < 0 and ball.xcor() < - 2*safe0 :
        Lbatup()
    if ball.ycor() < Lbat.ycor() - Lbat.safeh and ball.dx < 0 and ball.xcor() < - 2*safe0 :
        Lbatdown()

def Rai() :
    if ball.ycor() > Rbat.ycor() + Rbat.safeh and ball.dx > 0 and ball.xcor() >  2*safe0  :
        Rbatup()
    if ball.ycor() < Rbat.ycor() - Rbat.safeh and ball.dx > 0 and ball.xcor() >  2*safe0  :
        Rbatdown()
#CONTROLS----------------------------------------------------------
def Lbatup():
    if Lbat.ycor() < (roof)   :# - safe1) :
        Lbat.sety(Lbat.ycor() + Lbat.dm)        
def Lbatdown():
    if Lbat.ycor() > (ground) :# + safe1) :
        Lbat.sety(Lbat.ycor() - Lbat.dm)
        
def Rbatup():
    if Rbat.ycor() < (roof)   :# - safe1) :
        Rbat.sety(Rbat.ycor() + Rbat.dm)      
def Rbatdown():
    if Rbat.ycor() > (ground) :# + safe1) :
        Rbat.sety(Rbat.ycor() - Rbat.dm)

def byebye() :
    bye()

def xspeedincrease() :
    ball.dx *= 2   
def xspeeddecrease() :
    ball.dx *= 0.5

def yspeedincrease() :
    ball.dy += 0.2
def yspeeddecrease() :
    ball.dy -= 0.2
#COLLISIONS--------------------------------------------------------
def wallcollisions(ball) :
    if ball.ycor() > roof :
        ball.dy *= -roofmult
        ball.sety(roof)
    if ball.ycor() < ground :
        ball.dy *= -groundmult
        ball.sety(ground)
#------------------------------------
def scorecollisions(ball) :
    if ball.xcor() > rightwall :
        ball.goto(0,0)
        ball.dx *= -1
        Lbat.score += 1
        writescore()
    if ball.xcor() < leftwall :
        ball.goto(0,0)
        ball.dx *= -1
        Rbat.score += 1
        writescore()
#------------------------------------
def batcollisions(ball) :
    if (ball.xcor() <= Lbat.xcor() + Lbat.safew) and (ball.xcor() >= Lbat.xcor() - Lbat.safew):
        if ball.ycor() >= Lbat.ycor() - Lbat.safeh :
            if ball.ycor() <= Lbat.ycor() + Lbat.safeh :
                ball.setx(Lbat.xcor()+Lbat.safew)
                ball.dx *= -Lbat.multiplyer
                if ball.dy < 3 and ball.dy > -3 :
                    ball.dy *= choice(yincrmultiplyer)
                elif ball.dy > 7 or ball.dy < -7 :
                    ball.dy *= choice(yredumultiplyer)
                else :
                    ball.dy *= choice(yholdmultiplyer)
    if (ball.xcor() >= Rbat.xcor() - Rbat.safew) and (ball.xcor() <= Rbat.xcor() + Rbat.safew):
        if ball.ycor() >= Rbat.ycor() - Rbat.safeh :
            if ball.ycor() <= Rbat.ycor() + Rbat.safeh :
                ball.setx(Rbat.xcor()-Rbat.safew)
                ball.dx *= -Rbat.multiplyer
                if ball.dy < 3 and ball.dy > -3 :
                    ball.dy *= choice(yincrmultiplyer)
                elif ball.dy > 10 or ball.dy < -10 :
                    ball.dy *= choice(yredumultiplyer)
                else :
                    ball.dy *= choice(yholdmultiplyer)
#------------------------------------
def colcheck(ball) :
    wallcollisions(ball)
    scorecollisions(ball)
    batcollisions(ball)  
#OTHER------------------------------------------------------------------
def move(ball) :
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    #toofast(ball)
    #tooslow(ball)
    w.update()

#----------------
def toofast(ball) :
    if ball.dx > 5 :
        ball.goto(0,0)
        ball.write("<RESETTING : IM TOO FAST>\n",align = "center")
        for i in range(200) :
            w.update()
            ball.color("pink")
            w.update()
            ball.color("red")
        ballreset()
#----------------
def tooslow(ball) :
    if ball.dx < 0.1 and ball.dx > -0.1 :
        ball.goto     (0,0)
        ball.write    ("<RESETTING : IM TOO SLOW>\n",align = "center")
        for i in range(200) :
            w.update  ()
            ball.color("blue")
            w.update  ()
            ball.color("lightblue")
        ballreset()
def ballreset() :
    ball.clear()
    ball.color    ("white")
    ball.dx = defaultballx
#----------------
        
#WRITING AND SETTING------------------------------------------------------------------
def writescore():
    scorestring1 = leftplayer   + " Score: " + str(Lbat.score) + "\n"
    scorestring2 = rightplayer  + " Score: " + str(Rbat.score)
    scorestring  = scorestring1 + scorestring2
    
    p.clear()
    p.write(scorestring , align = "center" , font = "Courier")
#--------------------------------
def settingup():
    w.setup(2*rightwall + safe0,2*roof+ safe0)
    #COLORING ALL DEFAULTS
    p.color         ("white")  
    pframes.color   ("white")  
    pkeyboard.color ("white")
    w.bgcolor       ("black")
    Lbat.color      ("white")
    Rbat.color      ("white")
    ball.color      ("white")
    #POSITIONING
    p.goto(0,roof-safe0)
    pframes.goto(leftwall + safe0 , roof - safe0)
    pkeyboard.goto(rightwall - safe0/2 , ground + safe0)
    Lbat.goto(leftwall + safe0 , 0)
    Rbat.goto(rightwall - safe0 , 0)
    #WRITING DEFAULTS
    p.write("<SCORE>\n",align ="center")
#--------------------------------
lfps = 0
def framespen():
    global lfps
    sec         =  int(time() - tim)
    if  sec     == 0 :
        sec     =  1    
    fps         =  int(frames/sec)
    if  frames%2== 0 :
        frames0 =  frames
    if  frames%2== 1 :    
        frames1 =  frames
        lfps    =  int(frames1 - frames0)
    mystring1   =  "Total Frames:"   + str(frames)+ "\nTime: "       + str(sec) + " s"
    mystring2   =  "\nFps (global):" + str(fps)   + "\nFps(local): " + str(lfps)
    mystring    =  mystring1 + mystring2
    pframes.clear()
    pframes.write(mystring)
def colorchange() :
    for xyz in w.turtles() :
        xyz.color(choice(colorpallet))
    writescore()
    keyboardpen()
    #pc = choice(colorpallet) ; p.color(pc)
    #pframesc = choice(colorpallet) ; pframes.color(pframesc)
    #Lbatc = choice(colorpallet) ; Lbat.color(Lbatc)
    #Rbatc = choice(colorpallet) ; Rbat.color(Rbatc)
    #wc = choice(colorpallet) ; w.bgcolor(wc)
#--------------------------------

def keyboardpen() :
    pkeyboard.clear()
    keyboardstring0 = "<Controls>\n"
    spaces          = len(player)     + 5
    keyboardstring1 = leftplayer      + " UP   > "       + Lbatup_key        + "\n"   
    keyboardstring2 = leftplayer      + " DOWN > "       + Lbatdown_key      + "\n\n" 
    keyboardstring3 = rightplayer     + " UP   > "       + Rbatup_key        + "\n"  
    keyboardstring4 = rightplayer     + " DOWN > "       + Rbatdown_key      + "\n"
    keyboardstring5 = "Quit"          + space(spaces- 4) + " > "+ byebye_key + "\n"
    keyboardstring6 = "Colorshift"    + space(spaces- 10)+ " > "+ colorchange_key
    keyboardstrings1= keyboardstring0 + keyboardstring1  + keyboardstring2   + keyboardstring3
    keyboardstrings2= keyboardstring4 + keyboardstring5  + keyboardstring6
    keyboardstrings = keyboardstrings1+ keyboardstrings2
    pkeyboard.write(keyboardstrings,font=("Courier",9),align = "center")
#--------------------------------

#---------------------------------------------------------------------------------------------------------------------
#==========================
settingup  ()
keyboardpen()
while True :
    #w.update()
    #KEYBOARD BINDINGS --------------
    onkey(Lbatup        , Lbatup_key ) ; onkey(Lbatdown , Lbatdown_key)
    onkey(Rbatup        , Rbatup_key ) ; onkey(Rbatdown , Rbatdown_key)
    onkey(byebye        , byebye_key )
    onkey(colorchange   , colorchange_key    )
    onkey(xspeedincrease, xspeedincrease_key )
    onkey(xspeeddecrease, xspeeddecrease_key )
    onkey(yspeedincrease, yspeedincrease_key )
    onkey(yspeeddecrease, yspeeddecrease_key )
    #--------------------------------
##    for ball in balls :
    move    (ball)
    colcheck(ball)
    #framespen()
    frames += 1
    Lai()
    Rai()
    #xspeedincrease()
    listen()
    
