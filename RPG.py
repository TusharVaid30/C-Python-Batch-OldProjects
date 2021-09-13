from turtle import *
import random , math 
colorpallet  = ["red"  ,"green","blue"  ,"yellow","orange","lightblue" ,"magenta","violet"
               ,"brown","cyan" ,"pink"  ,"white" ,"maroon","lightgreen","gold"   ,"silver"
               ,"black" ]
S_X = 1200
S_Y = 700
Max_Y = 1.8
w = Screen()
w.bgcolor("black")
w.tracer(0)
w.setup(S_X , S_Y)
Player = Turtle()
Player.color("white")
Player.pu()
Orign = Turtle()
Orign.pu()
Orign.ht()

Buildings = []
Edge_x = S_X*2
Edge_y = S_Y*2
def bg(strr) : w.bgcolor(strr)
for _ in range(150) :
    Buildings.append(Turtle())
for _ in Buildings :
    _.naem = random.choice(colorpallet)
    Pos_x = random.randint( - Edge_x , Edge_x ) 
    Pos_y = random.randint( - Edge_y , Edge_y )
    _.shape("square")
    _.shapesize(random.randint(10,40)/5)
    _.color(_.naem)
    _.pu() 
    _.goto(Pos_x,Pos_y)
    
Map_Movements = 50
Map_Movement = 0 
Map_Mod = 1
Map_Rotate = 0 
def Mein() :
    global Map_Movement , tilted_tower 
    Map_Movement = Map_Movements
    Player.tilt(-tilted_tower)
    tilted_tower = 0 
def Fein() :
    global Map_Mod
    Map_Mod += 0.01
def Left()  :
    Player.setheading(180) ; Map_Move = 0   ; Mein() ;
    for _ in Buildings : _.setheading(Map_Move) 
def Right() :
    Player.setheading(0)   ; Map_Move = 180 ; Mein() ;
    for _ in Buildings : _.setheading(Map_Move)
def Up()    :
    Player.setheading(90)  ; Map_Move = 270 ; Mein() ;
    for _ in Buildings : _.setheading(Map_Move)
def Down()  :
    Player.setheading(270) ; Map_Move = 90  ; Mein() ;
    for _ in Buildings : _.setheading(Map_Move)

def Big() :
    global Edge_x , Edge_y , Map_Movements
    if Edge_y <= S_Y*Max_Y:
        Fein()
        Edge_x *= Map_Mod
        Edge_y *= Map_Mod
        Map_Movements *= Map_Mod 
        Player.shapesize( Player.shapesize()[0]*Map_Mod, Player.shapesize()[1]*Map_Mod )
        for _ in Buildings :
            _.setx( _.xcor()*Map_Mod)
            _.sety( _.ycor()*Map_Mod)
            _.shapesize(_.shapesize()[0]*Map_Mod , _.shapesize()[1]*Map_Mod)
def Small() :
    global Edge_x , Edge_y , Map_Movements
    if Edge_y >= S_Y/Max_Y :
        Fein() 
        Edge_x /= Map_Mod
        Edge_y /= Map_Mod
        Map_Movements /= Map_Mod 
        Player.shapesize( Player.shapesize()[0]/Map_Mod , Player.shapesize()[1]/Map_Mod )
        for _ in Buildings :
            _.setx( _.xcor()*(1/Map_Mod))
            _.sety( _.ycor()*(1/Map_Mod))
            _.shapesize(_.shapesize()[0]/Map_Mod , _.shapesize()[1]/Map_Mod)

def Interact() :
    X = Player.xcor() 
    Y = Player.ycor() 
    for _ in Buildings :
        XX  = int(_.xcor())
        YY  = int(_.ycor())
        XXX = int(_.shapesize()[0]*10) + 10
        YYY = int(_.shapesize()[1]*10) + 10
        if X in range (XX - XXX , XX + XXX ) :
            if Y in range (YY - YYY , YY + YYY ) :
                bg(_.naem)
def Rotate_Left() :
    global Map_Rotate
    Map_Rotate = - 2
    
def Rotate_Right() :
    global Map_Rotate
    Map_Rotate = 2

    
dillu = False  
def Dillu() :
    global dillu ;
    if dillu : dillu = False
    else : dillu = True 
def Move_Nein()   : global Map_Movement ; Map_Movement = 0
def Size_Nein()   : global Map_Mod      ; Map_Mod = 1
def Rotate_Nein() : global Map_Rotate   ; Map_Rotate = 0
def Nein() : pass
Moves = { Up : "w" , Left : "a" , Down : "s" , Right : "d" , Big : "+" , Small : "-" , 
          Interact : "e" , Rotate_Left : "Left" , Rotate_Right : "Right" , Dillu : "q" }
def Move() :
    for _ in Moves :
        onkeypress( _ , Moves[_] )
        if _ in [ Up , Down , Left , Right ] :  F = Move_Nein 
        elif _ in [ Big , Small ] : F = Size_Nein 
        elif _ in [ Rotate_Left , Rotate_Right ] : F = Rotate_Nein 
        else : F = Nein
        onkeyrelease( F , Moves[_] )
Everything = [ Player ] + Buildings
#for _ in Buildings : Everything.append(_)
listen()
tilted_tower = 0

String_temp  = "Controls.\n"
String_temp += "Move Up    : " + Moves[Up]    + "\n"
String_temp += "Move Down  : " + Moves[Down]  + "\n"
String_temp += "Move Left  : " + Moves[Left]  + "\n"
String_temp += "Move Right : " + Moves[Right] + "\n"
String_temp += "Get Drunk  : " + Moves[Dillu] + "\n"
String_temp += "Interact   : " + Moves[Interact]     + "\n"
String_temp += "Tilt Left  : " + Moves[Rotate_Left]  + "\n"
String_temp += "Tilt Right : " + Moves[Rotate_Right] + "\n" 
Orign.color("white") 
Orign.write(String_temp , font = "Courier")



while True :
    tilted_tower += Map_Rotate 
    Move()
    if dillu : Map_Rotate += random.randint(1,6)*random.choice((-1,1))/25
    for _ in Buildings  :
        _.fd(Map_Movement)
    #for _ in Everything :
        if _.xcor() > Edge_x  : _.setx(-Edge_x)
        if _.xcor() < -Edge_x : _.setx(Edge_x)
        if _.ycor() > Edge_y  : _.sety(-Edge_y)
        if _.ycor() < -Edge_y : _.sety(Edge_y)
    for _ in Everything :
        if Map_Rotate != 0 :
            temp_r = (_.xcor()**2 + _.ycor()**2)**0.5
            _.goto( temp_r*math.cos(math.radians(Orign.towards(_) + Map_Rotate ))  ,
                    temp_r*math.sin(math.radians(Orign.towards(_) + Map_Rotate )) )
            _.tilt(Map_Rotate) 


    w.update()
   
