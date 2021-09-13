import math , pygame as pg
from random import randint , choice
from time   import time
pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )

def sin( x ) : return math.sin( x*math.pi/180 )
def cos( x ) : return math.cos( x*math.pi/180 )
def Circle( x , y , color , size ) : pg.draw.circle( Window , color , ( int(x) , int(y) ) , int(size) )

#COLORS

#-___-^^-____
Color_Black        = (  0  ,  0  ,  0  )
Color_White        = ( 255 , 255 , 255 )
Color_Red          = ( 128 ,  0  ,  0  )
Color_Green        = (  28  , 234 , 111  )
Color_Blue         = (  28  ,  111  , 234 )
Color_Orange       = ( 255 , 100 ,  0  )
Color_Yellow       = ( 255 , 255 ,  0  )
Color_Light_Red    = ( 255 ,  0  ,  0  )
Color_Light_Green  = (  0  , 255 ,  0  )
Color_Light_Blue   = (  0  ,  0  , 255 )

# KEYBINDS
Controls_Move_Up      = pg.K_w
Controls_Move_Down    = pg.K_s
Controls_Move_Left    = pg.K_a
Controls_Move_Right   = pg.K_d
Controls_Bullet_Fired = pg.K_e
Controls_Twinkle      = pg.K_SPACE
Controls_Quit         = pg.K_ESCAPE

# VARIABLES
Gameover = False
FPS = 120
Image_Bit = 64

Spaceship_Start_x = Window_Width/2 - Image_Bit/2
Spaceship_Start_y = Window_Height - Image_Bit
Spaceship_Start_Health = 100
Spaceship_Start_dx = Spaceship_Start_dy = 3
Spaceship_Thruster_Colors = [ Color_Blue , Color_Light_Blue , Color_Green , Color_Light_Green ]
Spaceship_Image = pg.image.load("Ship.png")

Stars_Count = 50
Stars_Max_dx = 10
Stars_Max_dy = 20

Temp_Twinkle = True

Enemies_Number = 10
Enemy_Image = pg.image.load("Enemy.png")
Enemy_Start_Health = 100

class Pipe :
    def __init__ ( self , x , y , angle , size = 0 , Bps = 0 ) :
        self.x = x
        self.y = y
        self.angle = angle
        self.size = size
        self.Bps = Bps
        self.Gamma = 0

class Particle :
    def __init__( self , x , y , dx , dy ,  color,  size , dsize = 0 , theta = 0 , dtheta = 0 , radial = 0 , dradial = 0 ) :
        self.x  = x
        self.y  = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.size = size
        self.dsize = dsize
        self.theta = theta
        self.dtheta = dtheta #1.5
        self.radial = radial # 0
        self.dradial = dradial # 5
        self.ddradial = 0.01*self.dradial


    def Move( self ) :
        self.x += self.dx
        self.y += self.dy
    def Display( self ) :
        #pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , int(self.size) )
        Circle( self.x , self.y , self.color , self.size )

class Bullet :

    def __init__(self , x , y , dx , dy ):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.Speed = 5
        self.size = 3
        self.color = Color_Light_Red
        self.Type = 0
        self.Damage = 20# to be done something to this variable
    def Execute( self ) :
        self.BULLET_BOOM[self.Type]()
    def Display(self) :
        #pg.draw.circle( Window,  (255 , 0 , 0) , (int(self.x) , int(self.y)) , int(self.size) )
        Circle( self.x , self.y , self.color , self.size )
    def Move(self) :
        self.x += self.dx * self.Speed
        self.y += self.dy * self.Speed


class Ship :
    def __init__( self , x , y , Image ) :
        self.Particles = []
        self.Wisps = []
        self.Thrusters = []#yo can i get back the original bullet? i guess u aint there so i changint it
        self.Thruster_Particles = []
        self.Barrels = []
        self.Bullets = []
        self.x = x
        self.y = y
        self.Image = Image
        self.RefTheta = 0
        self.Max_Aoe_Bullet = 5
        self.Current_Aoe_Bullet = 0
        self.Aoe_Bullet_Fired = False

    def Set( self , Health , dx , dy ) :
        self.Health = Health
        self.dx = dx
        self.dy = dy
        self.Thruster_dx = 15
        self.Thruster_dy = 15
        self.Thruster_Particles_Min_Size = 2
        self.Thruster_Particles_Max_Size = 10
        self.Bullet_Speed = 3


    def Set_Thruster( self , Thrusters , Colors ) :
        for Thruster in Thrusters : self.Thrusters.append( Pipe(Thruster[0] , Thruster[1] , Thruster[2] , Thruster[3] ) )
        self.Thruster_Colors = Colors

    def Boost( self, Theta , Particle_Small )  :
        Theta %= 360
        Theta_1 = (Theta - 90)%360
        Theta_2 = (Theta_1 + 180)%360
        for Thruster in self.Thrusters :
            Flag = False
            if Theta_1 < Theta_2 :
                if Thruster.angle > Theta_1 and Thruster.angle < Theta_2 : Flag = True
            else :
                if Thruster.angle > Theta_1  or Thruster.angle < Theta_2 : Flag = True
            if Flag :
                Intensity = cos( Theta - Thruster.angle )
                self.Thruster_Particles.append( Particle( self.x + Thruster.x ,
                                                          self.y + Thruster.y ,
                                                          self.Thruster_dx*cos(Thruster.angle)*Intensity ,
                                                          self.Thruster_dy*sin(Thruster.angle)*Intensity ,
                                                          choice(self.Thruster_Colors) ,
                                                          randint( 1 , Thruster.size) ,

                                                          Particle_Small ) )


    def Set_Barrels(self, Barrels ):
        for Barrel in Barrels:
            self.Barrels.append(Pipe(Barrel[0], Barrel[1], Barrel[2] , Bps = Barrel[3] ))

    def Shoot(self):
        for Barrel in self.Barrels :
            Flag = False
            if int((time() - Barrel.Gamma)*Barrel.Bps) >= 1 :
                Flag = True
                Barrel.Gamma = time()
                self.Bullets.append( Bullet( self.x + Barrel.x, self.y + Barrel.y, cos(Barrel.angle) * self.Bullet_Speed, sin(Barrel.angle) * self.Bullet_Speed ))


    def Move( self , Theta ) :
        self.x += self.dx * cos(Theta) * 2#===========================================================================
        self.y += self.dy * sin(Theta) * 2#============================================================================
        self.Boost( (Theta + 180 + self.RefTheta )%360 , 1 )

    def Add_Wisp( self ) :
        self.Wisps.append( Particle ( self.x , self.y , 0 , 0 , ( 0 , 255 , 255) , 5 ,  0 , 0 ))
    def Move_Wisp( self ) :
        pass



    def Twinkle( self ) :
        global Temp_Twinkle
        Temp_Twinkle = False
        #Num = randint( 1, 5 )  #randint(4,10)
        Num = 5
        for _ in range(Num) :
            self.Particles.append( Particle ( self.x , self.y ,
                                              0 , 0 ,
                                              ( 200 , 0 , 200 ) ,
                                              7 ,
                                              0.005 ,
                                              _*(360/Num) ,
                                              1.5 ,
                                              16 ,
                                              Num/4 ))
        for _ in range(Num) :
            self.Particles.append( Particle ( self.x , self.y ,
                                              0 , 0 ,
                                              ( 0 ,200 , 200 ) ,
                                              7 ,
                                              0.005 ,
                                              _*(360/Num) + 180/Num,
                                              -3 ,
                                              16,
                                              Num/3 ))

    def Curl( self ) :
        for _ in self.Particles :
            _.theta += _.dtheta
            _.dtheta += 0.015
            _.radial += _.dradial
            _.dradial -= _.ddradial
            _.x = self.x + Image_Bit/2 + cos(_.theta)*_.radial
            _.y = self.y + Image_Bit/2 + sin(_.theta)*_.radial
            _.size -= _.dsize
            _.dsize += 0.0001
            if _.size <= 0 : self.Particles.remove(_)
    def Nurl( self ) :
        for _ in self.Particles :
            _.radial += _.dradial
            _.dradial += _.ddradial
            _.ddradial -= 0.005
            _.size -= _.dsize
            _.dsize += 0.005
            _.x = self.x + Image_Bit/2 + cos(_.theta)*_.radial
            _.y = self.y + Image_Bit/2 + sin(_.theta)*_.radial
            if _.size <= 0 : self.Particles.remove(_)

    def Display( self ) :
        Window.blit( self.Image , ( self.x , self.y ) )

    def Flip( self ) :
        self.RefTheta += 180
        self.RefTheta %= 360
        for Thruster in self.Thrusters :
            Thruster.x = Image_Bit - Thruster.x
            Thruster.y = Image_Bit - Thruster.y
            Thruster.angle += 180
            Thruster.angle %= 360


Spaceship_1 = Ship( Spaceship_Start_x , Spaceship_Start_y , Spaceship_Image )
Spaceship_1.Set( Spaceship_Start_Health , Spaceship_Start_dx , Spaceship_Start_dy )
Spaceship_1.Set_Thruster( [
                            (24 , 14 , 270 , 5) , (39 , 14 , 270 , 5) ,  #Up
                            (22 , 64 , 90 , 6) , (32 , 64 ,  90 , 13) , (41 , 64 , 90 , 6) , #Down
                            ( 0 , 46 , 180 , 15) , #Left
                            (64 , 46 ,  0  , 15) #Right
                           ],
                        Spaceship_Thruster_Colors )
Spaceship_1.Set_Barrels([(10, 24, 265 , 8 ) ,
                         (17, 21, 270 , 5 ) ,
                         (47, 21, 270 , 8 ) ,
                         (54, 24, 275 , 5 )
                         ])

Spaceship = Spaceship_1

Stars = []
for _ in range(Stars_Count) :
    Temp_x  = randint( 0 , Window_Width  )
    Temp_y  = randint( 0 , Window_Height )
    Temp_dx = 0#randint( 0 , Stars_Max_dx  )*choice( ( 1 , -1 ) )
    Temp_dy = randint( 1 , Stars_Max_dy  ) #choice( ( 1 , -1 ) )
    Temp_size  = randint( 1 , 5 )
    Temp_color = Color_White
    Stars.append( Particle( Temp_x , Temp_y , Temp_dx , Temp_dy , Temp_color , Temp_size  ) )


Enemies = []
for _ in range(Enemies_Number):
    Temp_x = randint( 0 , Window_Width - Image_Bit )
    Temp_y = randint( 0 , Window_Height/2 - Image_Bit )
    Enemies.append( Ship(Temp_x , Temp_y , Enemy_Image)  )

for Enemy in Enemies:
    Enemy.Set(100, 0, 0)


def Teleport_Corner( Arg ) :
    if Arg.x < 0             : Arg.x = Window_Width
    if Arg.x > Window_Width  : Arg.x = 0
    if Arg.y < 0             : Arg.y = Window_Height
    if Arg.y > Window_Height : Arg.y = 0

zz = 1

def Stuff() :
    global zz

    if Spaceship.Thrusters[5].angle > 200 or Spaceship.Thrusters[5].angle < 160  : zz *= -1

    Spaceship.Thrusters[5].angle += zz
    Spaceship.Thrusters[6].angle -= zz

def Collide(Obj1 , Obj2):#Obj1 - Spaceship, Obj2 - Bullet
    '''for int(i) in range(int(Obj2.x - Obj2.size), int(Obj2.x + Obj2.size)):
        if i in range(int(Obj1.x), int(Obj1.x + Image_Bit)):
            for int(j) in range(int(Obj2.y - Obj2.size), int(Obj2.x + Obj2.size)):
                if j in range(int(Obj1.y) , int(Obj1.y + Image_Bit)):
                    return True
    else: return False'''
    pass
    '''if Obj2.x > Obj1.x and Obj2.x < Obj1.x + Image_Bit:
        if Obj2.y < Obj1.y and Obj2.y > Obj1.y + Image_Bit:
            return True
        return False
    return False'''
Zinga = False 


def Logic() :
    global Zinga
    if len(Spaceship.Particles) == 0 : Zinga = True 
    #global zz
    #Spaceship.Boost( zz , 3 )
    #zz += 1
    if len(Spaceship.Particles) > 600 : Zinga = False
    if Zinga : Spaceship.Twinkle() 
    #Stuff()
    #Spaceship.Boost( 0 , 3 )
    #Spaceship.Boost( 180 , 3 )
    Spaceship.Curl()

    Teleport_Corner( Spaceship )
    for Star in Stars : Teleport_Corner( Star )

    for _ in Spaceship.Thruster_Particles :
        _.Move()
        _.size -= _.dsize
        if (_.x < 0 or _.x > Window_Width) or (_.y < 0 or _.y > Window_Height) or  (_.size <= 0) : Spaceship.Thruster_Particles.remove( _ )
    for _ in Spaceship.Bullets :
        _.Move()
        if (_.x < 0 or _.x > Window_Width) or (_.y < 0 or _.y > Window_Height) : Spaceship.Bullets.remove( _ )
    for Star in Stars :
        Star.Move()

    for Enemy in Enemies:
        if Collide(Enemy , Bullet):# look at me
            Enemies.remove(Enemy)
            #Enemy.Health -= Bullet_Damage

def Controls() :
    global Gameover , Temp_Twinkle

    Key_Pressed = pg.key.get_pressed()
    Mouse_Pressed = pg.mouse.get_pressed()
    Mouse_Position = pg.mouse.get_pos()
    for event in pg.event.get() :
        if event.type == pg.QUIT : Gameover = True

    if Key_Pressed[Controls_Quit]         : Gameover = True
    if Key_Pressed[Controls_Move_Left]    : Spaceship.Move(180)
    if Key_Pressed[Controls_Move_Right]   : Spaceship.Move(0)
    if Key_Pressed[Controls_Move_Down]    : Spaceship.Move(90)
    if Key_Pressed[Controls_Move_Up]      : Spaceship.Move(270)
    if Key_Pressed[Controls_Bullet_Fired] : Spaceship.Shoot()
    #else : Spaceship.Boost( Spaceship.Down_Thrusters  , 7 , 3 )
    if Key_Pressed[Controls_Twinkle] :
        #if Temp_Twinkle :
        Spaceship.Twinkle()
    #else : Temp_Twinkle = True


def Display_Effects() :
    for _ in Spaceship.Thruster_Particles : _.Display()
    for _ in Spaceship.Particles : _.Display()
    for Star in Stars : Star.Display()

def Display_Bullets() :
    for Bullet in Spaceship.Bullets :
        Bullet.Display()

def Display() :


    for Enemy in Enemies :
        Enemy.Display()
        if Enemy.Health <= 0:
            Enemies.remove(Enemy)
    Display_Effects()
    Display_Bullets()
    Spaceship.Display()


def main() :
    while not Gameover :
        pg.time.Clock().tick(FPS)
        #Window.fill(Color_Black)
        Controls()
        Logic()
        Display()
        pg.display.flip()
        if pg.key.get_pressed()[pg.K_ESCAPE]: break
main()

pg.quit()
quit()

