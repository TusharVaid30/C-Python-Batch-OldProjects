from turtle import *
import random
colorpallet  = ["red"  ,"green","blue"  ,"yellow","orange","lightblue" ,"magenta","violet"
               ,"brown","cyan" ,"pink"  ,"white" ,"maroon","lightgreen","gold"   ,"silver"
               ,"black" ]
w = Screen()
w.bgcolor("black")
w.tracer(0)
w.setup(1200,700)
Player = Turtle()
Player.color("white")
Player.pu()
dismod = (2/3,3/4,3/5,7/8)  
minpix = 4
maker = Turtle() 
#w = Screen()      ; w.bgcolor("black") ; w.tracer(0) ; w.setup(800, 1000, 600, 0)
#t = Turtle()      ; t.color  ("white") ; t.lt(90)    ; t.speed(0) ; 
#t.pu()            ; t.bk(305)          ; t.pd()      ; t.ht()     ;
def DESIGN(self , homePos , scale): 
    def design():
        self.up()
        for i in range(5):
            self.forward(64.65 * scale)
            self.down()
            wheel(self , self.position(), scale)
            self.up()
            self.backward(64.65 * scale)
            self.right(72)
        self.up()
        self.goto(homePos)
        self.right(36)
        self.forward(24.5 * scale)
        self.right(198)
        self.down()
        centerpiece(self , 46 * scale, 143.4, scale)

    def wheel(self, initpos, scale):
        self.right(54)
        for i in range(4):
            pentpiece(self , initpos, scale)
        self.down()
        self.left(36)
        for i in range(5):
            tripiece(self , initpos, scale)
        self.left(36)
        for i in range(5):
            self.down()
            self.right(72)
            self.forward(28 * scale)
            self.up()
            self.backward(28 * scale)
        self.left(54)

    def tripiece(self, initpos, scale):
        oldh = self.heading()
        self.down()
        self.backward(2.5 * scale)
        tripolyr(self , 31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.down()
        self.backward(2.5 * scale)
        tripolyl(self , 31.5 * scale, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)

    def pentpiece(self, initpos, scale):
        oldh = self.heading()
        self.up()
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        pentr(self , 18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.forward(29 * scale)
        self.down()
        for i in range(5):
            self.forward(18 * scale)
            self.right(72)
        pentl(self , 18 * scale, 75, scale)
        self.up()
        self.goto(initpos)
        self.setheading(oldh)
        self.left(72)


    def pentl(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.left(ang)
        pentl(self , side - (.38 * scale), ang, scale)

    def pentr(self, side, ang, scale):
        if side < (2 * scale): return
        self.forward(side)
        self.right(ang)
        pentr(self , side - (.38 * scale), ang, scale)

    def tripolyr(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.right(111)
        self.forward(side / 1.78)
        self.right(111)
        self.forward(side / 1.3)
        self.right(146)
        tripolyr(self , side * .75, scale)

    def tripolyl(self, side, scale):
        if side < (4 * scale): return
        self.forward(side)
        self.left(111)
        self.forward(side / 1.78)
        self.left(111)
        self.forward(side / 1.3)
        self.left(146)
        tripolyl(self , side * .75, scale)

    def centerpiece(self, s, a, scale):
        self.forward(s); self.left(a)
        if s < (7.5 * scale):
            return
        centerpiece(self , s - (1.2 * scale), a, scale)
    design() 

def tree(t,x,y) :
    zz = random.randint(30,45)  ; z  = x*0.8 # random.choice(dismod)*x  
    t.fd(1*x) 
    if z > minpix : tree(t,z*1.1,zz*0.9) 
    t.rt(y) 
    if z > minpix : tree(t,z,zz) 
    t.lt(2*y)
    if z > minpix : tree(t,z,zz)
    t.rt(y)
    t.bk(x)       ;     #w.update()
def grass(t,x,y) :
    xx = t.xcor()
    yy = t.ycor() 
    for _ in range(7) :
        le = random.randint(10,20)*x/50
        lt = random.randint(-y,y)
        lm = []
        t.lt(lt) 
        t.fd(le) 
        t.bk(le)
        t.rt(lt) 
        t.setx(t.xcor() + x/100) 
##        for __ in range(int(le)) :
##            lf = random.randint(1,10)/100
##            t.fd(lf)
##            t.lt(lt)
##            lm.append(lf)
##        for __ in range(int(le)) :
##            t.bk(lm[__])
##            t.rt(lt) 
def makee() :
    maker.begin_poly()
    maker.setheading(90)
    DESIGN(maker , maker.position() , 0.05)
    maker.shapesize(random.randint(10,40)/1)
    w.register_shape("Hub" , maker.get_poly() )
    for _ in range(4) :
        maker.clear()
        maker.begin_poly()
        maker.setheading(90)
        grass( maker , random.randint(9,11)/10 , 30)
        w.register_shape("Grass" + str(_),maker.get_poly() )
Buildings = []
Bui = 0 
Edge_x = 400#1250
Edge_y = 400
makee() 
def bg(strr) : w.bgcolor(strr)
for _ in range(20) :
    Buildings.append(Turtle())
    Buildings[_].num = _
    
for _ in Buildings :
    _.color("white","black")
    _.begin_poly()
    _.setheading(90)
    if _.num < 2  :
        #DESIGN(_ , _.position() , 0.05)
        _.shapesize(random.randint(10,40)/1)
        #w.register_shape("Hub" + str(Bui) , _.get_poly() )
        _.shape("Hub")
    else :
        #tree(_,random.randint(90,110)/10,random.randint(20,45))
        #_.shapesize(random.randint(10,40)/10)
        #grass( _ , random.randint(9,11)/10 , 30)
        #w.register_shape("Grass" + str(Bui),_.get_poly() )
        _.shapesize(random.randint(10,20))
        _.shape("Grass" + str(Bui%4) )
    _.setheading(90)
    _.pu()
    #_.naem = random.choice(colorpallet)
    
    Pos_x = random.randint( - Edge_x , Edge_x ) 
    Pos_y = random.randint( - Edge_y , Edge_y )
    _.goto(Pos_x,Pos_y)
    #w.update()
    Bui += 1
    
Map_Movements = 5
#Map_Movement = 0
Map_Movement_x = 0
Map_Movement_y = 0 
Map_Mod = 1

def Mein(Ar) :
    global Map_Movement_x , Map_Movement_y
    if Ar == 0 : Map_Movement_y = -Map_Movements 
    if Ar == 1 : Map_Movement_y = Map_Movements 
    if Ar == 2 : Map_Movement_x = Map_Movements 
    if Ar == 3 : Map_Movement_x = -Map_Movements 
def Fein() :
    global Map_Mod
    Map_Mod += 0.01
def Left()  :
    Player.setheading(180)
    if False and Player.xcor() > - 50 : Player.fd(Map_Movements) ; w.update() ; 
    else : Map_Move = 0 ; Mein(2) ;
def Right() :
    Player.setheading(0)   
    if False and Player.xcor() <  50 : Player.fd(Map_Movements); w.update() ;  
    else : Map_Move = 180 ; Mein(3) ;
def Up()    :
    Player.setheading(90)   
    if False and Player.ycor() <  50 : Player.fd(Map_Movements) ; w.update() ; 
    else : Map_Move = 270 ; Mein(0) ;
def Down()  :
    Player.setheading(270)  
    if False and Player.ycor() > - 50 : Player.fd(Map_Movements) ; w.update() ; 
    else : Map_Move = 90  ; Mein(1) ; 
def Nein() :
    global Map_Movement_x , Map_Movement_y , Map_Mod
    Map_Movement_x = Map_Movement_y = 0
    Map_Mod = 1
def Big() :
    Fein()
    Player.shapesize( Player.shapesize()[0]*Map_Mod, Player.shapesize()[1]*Map_Mod ) 
    global Edge_x , Edge_y , Map_Movements
    Edge_x *= Map_Mod
    Edge_y *= Map_Mod
    Map_Movements *= Map_Mod 
    for _ in Buildings :
        _.setx( _.xcor()*Map_Mod)
        _.sety( _.ycor()*Map_Mod)
        _.shapesize(_.shapesize()[0]*Map_Mod , _.shapesize()[1]*Map_Mod)
def Small() :
    Fein()
    Player.shapesize( Player.shapesize()[0]/Map_Mod , Player.shapesize()[1]/Map_Mod ) 
    global Edge_x , Edge_y , Map_Movements 
    Edge_x /= Map_Mod
    Edge_y /= Map_Mod
    Map_Movements /= Map_Mod 
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
Moves = { Up : "w" , Left : "a" , Down : "s" , Right : "d" , Big : "+" , Small : "-" , 
          Interact : "e" }
def Move() :
    for _ in Moves :
        onkeypress( _ , Moves[_] )
        onkeyrelease(Nein , Moves[_])

Everything = [ Player ]
for _ in Buildings : Everything.append(_)
listen()
Move()
fps = 0 
while True :
    sad = 0
    Buildings[0].lt(3)
    Buildings[1].rt(1) 
    for _ in Buildings  :
        _.setx(Map_Movement_x + _.xcor())
        _.sety(Map_Movement_y + _.ycor())
        if sad > 1 :
            if fps%4 == 0 : _.shape("Grass" + str(random.randint(0,3))) 
        sad += 1 
    for _ in Everything :
        if _.xcor() > Edge_x  : _.setx(-Edge_x)
        if _.xcor() < -Edge_x : _.setx(Edge_x)
        if _.ycor() > Edge_y  : _.sety(-Edge_y)
        if _.ycor() < -Edge_y : _.sety(Edge_y)
    fps += 1    
    w.update()
   
