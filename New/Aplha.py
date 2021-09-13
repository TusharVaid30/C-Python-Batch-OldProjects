import pygame as pg
from random import randint , choice
import math

def sin( x ) : return math.sin( x*math.pi/180 )
def cos( x ) : return math.cos( x*math.pi/180 )
def mod( x ) :
    if x < 0 : x *= -1
    return x
pg.init()

Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )

#COLORS

Color_Black        = (  0  ,  0  ,  0  )
Color_White        = ( 255 , 255 , 255 )
Color_Red          = ( 128 ,  0  ,  0  )
Color_Green        = (  0  , 100 ,  0  )
Color_Blue         = (  0  ,  0  , 100 )
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
Stars_Max_dy = 10


Enemies_Number = 5
Enemies_Image = pg.image.load("Enemy.png")


class Pipe :
    def __init__ ( self , x , y , angle , size ) :
        self.x = x
        self.y = y
        self.angle = angle
        self.size = size

class Particle :
    def __init__( self , x , y , dx , dy , size , color , dsize = 0 ) :
        self.x  = x
        self.y  = y
        self.dx = dx
        self.dy = dy
        self.size = size
        self.color = color
        self.dsize = 1 # dsize
    def Move( self ) :
        self.x += self.dx
        self.y += self.dy
    def Display( self ) :
        pg.draw.circle( Window,  self.color , (int(self.x) , int(self.y)) , int(self.size) )

class Bullet :

    def __init__(self):
        self.dx = 0
    def Display(self) :
        pg.draw.circle( Window,  (255 , 0 , 0) , (int(self.x) , int(self.y)) , int(self.size) )
    def Move(self) :
        self.x += self.dx
        self.y += self.dy



class Ship :
    def __init__( self , x , y , Image ) :
        self.Particles = []
        self.Thrusters = []
        self.Thruster_Particles = []
        self.x = x
        self.y = y
        self.Image = Image

    def Set( self , Health , dx , dy ) :
        self.Health = Health
        self.dx = dx
        self.dy = dy
        self.Thruster_dx = 15
        self.Thruster_dy = 15
        self.Thruster_Particles_Min_Size = 2
        self.Thruster_Particles_Max_Size = 10

    def Set_Thruster( self , Thrusters , Colors ) :
        for Thruster in Thrusters :
            self.Thrusters.append( Pipe(Thruster[0] , Thruster[1] , Thruster[2] , Thruster[3] ) )
        self.Thruster_Colors = Colors

    def Boost( self, Theta , Particle_Small )  :
        Theta %= 360
        
        Theta_1 = (Theta - 90)%360
        Theta_2 = (Theta + 90)%360
        for Thruster in self.Thrusters :
            Flag = False 
            #if Theta_1 < Theta_2 :
            #    if Thruster.angle > Theta_1 and Thruster.angle < Theta_2 :
            #        Flag = True
            #else :
            #    if Thruster.angle > Theta_2 or Thruster.angle < Theta_2 : 
            #        Flag = True
            #if (Theta_1 < Theta_2 and Thruster.angle > Theta_1 and Thruster.angle < Theta_2)
            #or (Theta_1 > Theta_1 and (Thruster.angle > Theta_1 or Thruster.angle < Theta_2)) :
            if Theta_1 < Theta_2 :
                if Thruster.angle > Theta_1 and Thruster.angle < Theta_2 : Flag = True
            else :
                if Thruster.angle > Theta_1 or Thruster.angle < Theta_2 : Flag = True  
            if  Flag  : 
                for _ in range(5) :
                    self.Thruster_Particles.append( Particle( self.x + Thruster.x ,
                                                          self.y + Thruster.y ,
                                                          self.Thruster_dx*cos(Thruster.angle)*cos( Theta - Thruster.angle ) , 
                                                          self.Thruster_dy*sin(Thruster.angle)*cos( Theta - Thruster.angle ) ,
                                                          randint( 1 , Thruster.size)  ,
                                                          choice(self.Thruster_Colors) ,
                                                          Particle_Small ) )
                
    def Move( self , Theta ) :
        self.x += self.dx * cos(Theta)
        self.y += self.dy * sin(Theta)
        #self.Boost( (Theta + 180)%360 , 1 )
        self.Boost( Theta + 180 , 1 ) 

    def Shoot_Primary( self ) :
        pass

    def Shoot( self ) :
        self.Shoot_Primary()

    def Display( self ) :
        pg.display.get_surface().blit( self.Image , ( self.x , self.y ) )

    def Display_Health(self, x, y, width, height):
        t_height = self.Health/4
        pg.draw.rect( Window ,  Color_Green, (self.x + x, self.y + y, width, t_height))


Spaceship_1 = Ship( Spaceship_Start_x , Spaceship_Start_y , Spaceship_Image )
Spaceship_1.Set( Spaceship_Start_Health , Spaceship_Start_dx , Spaceship_Start_dy )

Spaceship_1.Set_Thruster( [
                            (24 , 14 , 270 , 5) , (39 , 14 , 270 , 5) ,  #Up
                            (22 , 64 , 100 , 6) , (32 , 64 ,  90 , 13) , (41 , 64 , 80 , 6) , #Down
                            ( 0 , 46 , 180 , 15) , #Left
                            (64 , 46 ,  0  , 15) #Right
                           ],
                        Spaceship_Thruster_Colors )

Spaceship = Spaceship_1

Stars = []
for _ in range(Stars_Count) :
    Temp_x  = randint( 0 , Window_Width  )
    Temp_y  = randint( 0 , Window_Height )
    Temp_dx = 0#randint( 0 , Stars_Max_dx  )*choice( ( 1 , -1 ) )
    Temp_dy = randint( 1 , Stars_Max_dy  ) #choice( ( 1 , -1 ) )
    Temp_size  = randint( 1 , 5 )
    Temp_color = Color_White
    Stars.append( Particle( Temp_x , Temp_y , Temp_dx , Temp_dy , Temp_size , Temp_color ) )


Enemies = []
for _ in range(Enemies_Number):
    Temp_x = randint( 0 , Window_Width - Image_Bit )
    Temp_y = randint( 0 , Window_Height/2 - Image_Bit )
    Enemies.append( Ship(Temp_x , Temp_y , Enemies_Image)  )


'''
def Booster( Object ) :
    Booster_Colors = [Color_Orange, Color_Red, Color_Yellow]
    Booster_Spread = Object.Booster_Spread

    Booster_Color  = random.choice(Booster_Colors)
    Booster_x      = int(Object.x + Image_Bit/2 + random.randint(-int(), int()))
    Booster_y      = int(Object.y + Image_Bit   + random.randint(0 , int() ))
    Booster_Radius = 10
    for i in range(int(100)):
        pg.draw.circle(Window, Booster_Color, (Booster_x, Booster_y), Booster_Radius)
'''
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

def Logic() :
    global zz
    #Spaceship.Boost( Spaceship.Down_Thrusters  , 7 , 4 )
    Spaceship.Boost( zz , 4 )
    #Stuff()
    #Spaceship.Move( zz )
    zz += 10
    zz %= 360
    Teleport_Corner( Spaceship )
    for Star in Stars : Teleport_Corner( Star )

    for _ in Spaceship.Thruster_Particles :
        _.Move()

    for Star in Stars :
        Star.Move()

    for _ in Spaceship.Thruster_Particles :
        _.size -= _.dsize
        if (_.x < 0 or _.x > Window_Width) or (_.y < 0 or _.y > Window_Height) or  (_.size <= 0) : Spaceship.Thruster_Particles.remove( _ )


def Controls() :
    global Gameover

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
    #else : Spaceship.Boost( Spaceship.Down_Thrusters  , 7 , 3 )
    if Key_Pressed[Controls_Bullet_Fired] : Spaceship.Shoot()


#def Display_Bullets() :
    #for Bullet in Spaceship.Bullets : Bullet.Display()

def Display_Effects() :
    for _ in Spaceship.Thruster_Particles : _.Display()
    for Star in Stars :
        Star.Display()

def Display() :

    Spaceship.Display()
    for Enemy in Enemies : Enemy.Display()
    Display_Effects()
    Spaceship.Display_Health(31, 18, 2, 25)


def main() :
    while not Gameover :
        Window.fill(Color_Black)
        Controls()
        Logic()
        Display()
        pg.display.flip()
        if pg.key.get_pressed()[pg.K_ESCAPE]: break
main()

pg.quit()
quit()
