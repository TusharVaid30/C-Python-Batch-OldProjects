import math , random , pygame as pg
from random import choice
from time   import time

def sin( x ) : return math.sin( x*math.pi/180 )
def cos( x ) : return math.cos( x*math.pi/180 )
def randint( x , y ) : return random.randint( int(x)*100000 , int(y)*100000 )/100000
Text_Size = 20 

pg.init()
Window_Width  = pg.display.Info().current_w
Window_Height = pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) , pg.FULLSCREEN )
def Line( Start , End ) :
  pg.draw.line( Window , ( 255 , 255 , 255 ) , ( Start[0] , Start[1] ) , ( End[0] , End[1] ) , 1 ) 

def Write( x , y , Text  ) :
  Window.blit( pg.font.SysFont( None , Text_Size ).render( str(Text) , True , ( 255 , 255 , 255 ) ) , ( x , y ) ) 

def Circle( x , y , Radius , Color ) :
  pg.draw.circle( Window, Color , (int(x) , int(y)) , abs(int(Radius)) )
        
def Rectangle( x , y , Width , Height , Color ) :
  pg.draw.rect( Window , Color , ( x - Width/2 , y - Height/2 , Width , Height ) )
Sliders = []
class Slider :
    def __init__( self , Min_Value , Max_Value , Name = "Slider" , Length = 100 , x = 100 , y = 200 ):
        self.Min_Value = Min_Value
        self.Max_Value = Max_Value
        self.Variable = (Min_Value + Max_Value)/2
        self.Variable_x = self.x = x
        self.Variable_y = self.y = y
        self.Variable_Height = 15
        self.Variable_Width = 20
        
        
        self.Name = "  :- " + Name + " : " 
        self.Length = abs(Length)
        self.unit = (self.Max_Value - self.Min_Value)/self.Length

        self.Mover_x = self.x + self.Length/2
        self.Mover_y = self.y + self.Length/2
        self.Mover_Radius = 10
        self.Fresh()
        Sliders.append( self ) 
    def Fresh( self ) :
        self.Variable_Color = ( 100 , 100 , 100 )
        self.Mover_Color = ( 200 , 200 , 200 )
        # Set All buffers to 0 if maually moving sliders in code 
        
    def Display( self ) :
        Line(( self.x , self.y - self.Length/2 ) , (self.x , self.y + self.Length/2) )
        Write( self.x , self.y + self.Length/2 , self.Min_Value )
        Write( self.x , self.y - self.Length/2 - Text_Size/2 , self.Max_Value )
        Write( self.x , self.y , self.Name + str(self.Variable) )
        Circle( self.Mover_x , self.Mover_y , 10 , self.Mover_Color )
        Rectangle( self.Variable_x , self.Variable_y , self.Variable_Width , self.Variable_Height , self.Variable_Color ) 
        
    def Sync( self , Mouse_x , Mouse_y ) :
        Mouse_x += self.Buffer_Variable_x
        Mouse_y += self.Buffer_Variable_y
        #Current_Slider.Variable_x = Mouse_x
        if Mouse_y >= self.y - self.Length/2 and Mouse_y <= self.y + self.Length/2 :
            self.Variable_y = Mouse_y
        else :
            if Mouse_y <= self.y - self.Length/2 :
                self.Variable_y = self.y - self.Length/2
            if Mouse_y >= self.y + self.Length/2 :
                self.Variable_y = self.y + self.Length/2
        self.Variable = self.unit*(self.y + self.Length/2 - self.Variable_y) + self.Min_Value
    def Inverse_Sync( self ) :
        pass
    def Caught_Variable( self , Mouse_x , Mouse_y ) :
        if Mouse_x > self.Variable_x - self.Variable_Width/2 :
            if Mouse_x < self.Variable_x + self.Variable_Width/2 :
                if Mouse_y > self.Variable_y - self.Variable_Height/2 :
                    if Mouse_y < self.Variable_y + self.Variable_Height/2 :
                        return True
        return False
    def Caught_Mover( self , Mouse_x , Mouse_y ) :
        if Mouse_x > self.Mover_x - self.Mover_Radius :
            if Mouse_x < self.Mover_x + self.Mover_Radius :
                if Mouse_y > self.Mover_y - self.Mover_Radius :
                    if Mouse_y < self.Mover_y + self.Mover_Radius :
                        return True
        return False
    def Move( self , Mouse_x , Mouse_y ) :
        self.x = Mouse_x + self.Buffer_x
        self.y = Mouse_y + self.Buffer_y
        self.Variable_x = Mouse_x + self.Buffer_Variable_x
        self.Variable_y = Mouse_y + self.Buffer_Variable_y
        self.Mover_x = Mouse_x + self.Buffer_Mover_x
        self.Mover_y = Mouse_y + self.Buffer_Mover_y

def Slider_Driver() :
    global Current_Slider , Holding_Mover , Holding_Variable 
    Mouse_x , Mouse_y = pg.mouse.get_pos()
    Mouse_Clicked = pg.mouse.get_pressed()[0]
    if not Mouse_Clicked :
        Holding_Mover = Holding_Variable = False
        Current_Slider.Fresh()

    if Mouse_Clicked and not Holding_Variable and not Holding_Mover :
        for Slider in Sliders :
            if Slider.Caught_Variable( Mouse_x , Mouse_y ) :
                Holding_Variable = True
                Slider.Variable_Color = ( 255 , 255 , 255 ) 
                Slider.Buffer_Variable_x = Slider.Variable_x - Mouse_x  
                Slider.Buffer_Variable_y = Slider.Variable_y - Mouse_y
                Current_Slider = Slider
                break
            if Slider.Caught_Mover( Mouse_x , Mouse_y ) :
                Holding_Mover = True
                Slider.Mover_Color = ( 255 , 255 , 255 ) 
                Slider.Buffer_Variable_x = Slider.Variable_x - Mouse_x  
                Slider.Buffer_Variable_y = Slider.Variable_y - Mouse_y
                Slider.Buffer_Mover_x = Slider.Mover_x - Mouse_x  
                Slider.Buffer_Mover_y = Slider.Mover_y - Mouse_y
                Slider.Buffer_x = Slider.x - Mouse_x
                Slider.Buffer_y = Slider.y - Mouse_y
                Current_Slider = Slider
                break 
    if Holding_Variable :
        Current_Slider.Sync( Mouse_x , Mouse_y )
    if Holding_Mover :
        Current_Slider.Move( Mouse_x , Mouse_y ) 

class Pipe :
    def __init__ ( self , x , y , angle , size = 0, Bps = 0 ) :
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
        Circle( self.x , self.y , self.size , self.color  )
        
class Ship :
    def __init__( self , x , y ) :
        self.Particles = []
        self.Wisps = []
        self.Thrusters = []
        self.Thruster_Particles = []
        self.Barrels = []
        self.Bullets = []
        self.x = x
        self.y = y
        self.RefTheta = 0
        self.Lasers = []

    def Set( self , Health , dx , dy ) :
        self.Health = Health
        self.dx = dx
        self.dy = dy
        self.Thruster_dx = 15
        self.Thruster_dy = 15
        self.Thruster_Particles_Min_Size = 2
        self.Thruster_Particles_Max_Size = 10
        self.Bullet_Speed = 1#========================================================================bullet speed


    def Set_Thruster( self , Thrusters , Colors ) :
        for Thruster in Thrusters : self.Thrusters.append( Pipe(Thruster[0] , Thruster[1] , Thruster[2] , Thruster[3] ) )
        self.Thruster_Colors = Colors

    def Boost( self, Theta )  :
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


                for _ in range( int(Thruster_Thick*Intensity) ) :
                  self.Thruster_Particles.append( Particle( self.x + Thruster.x ,
                                                          self.y + Thruster.y ,
                                                          randint(1, Thruster_Delta*Intensity)*cos(Thruster.angle) ,
                                                          randint(1, Thruster_Delta*Intensity)*sin(Thruster.angle) ,
                                                          choice(self.Thruster_Colors) ,
                                                          randint( 1 , int(Thruster_Size)) ,
                                                          Particle_Small ) )

Colors = [ (255 , 0 , 0) , (225 , 225 , 0) ] 
Space = Ship(Window_Width/2 , Window_Height/2 )
Space.Set_Thruster([( 0 , 0 ,   0 , 10) ,
                    ( 0 , 0 ,  90 , 10) ,
                    ( 0 , 0 , 180 , 10) ,
                    ( 0 , 0 , 270 , 10) ] ,
                    Colors ) 

Slider_Theta = Slider( 0   , 180 , "Theta" , 100 ,  100 , 200 )
Slider_Thruster_Delta = Slider( 2 , 550 , "Thruster_Delta" , 509 ,  300 , 200 )
Slider_Particle_Small = Slider( 0.1 , 5 , "Particle_Small" , 200 , 400 , 200  ) 
Slider_Thruster_Size = Slider( 5 , 30 , "Thruster_Size" )
Slider_Thruster_Thick = Slider( 1 , 250 , "Thruster_Thick" , 500 )
Thruster_Thick = Thruster_Size = Thruster_Delta = Particle_Small = 0 

Current_Slider = Sliders[0]
while True :
    Window.fill ( (0,0,0) )
    if Thruster_Delta != Slider_Thruster_Delta.Variable : Thruster_Delta = Slider_Thruster_Delta.Variable
    if Thruster_Size != Slider_Thruster_Size.Variable : Thruster_Size = Slider_Thruster_Size.Variable
    if Particle_Small != Slider_Particle_Small.Variable : Particle_Small = Slider_Particle_Small.Variable
    if Thruster_Thick != Slider_Thruster_Thick.Variable : Thruster_Thick = Slider_Thruster_Thick.Variable
    Slider_Driver() 
    Space.Boost(Slider_Theta.Variable)
    for _ in Space.Thruster_Particles :
        _.Move()
        _.size -= _.dsize 
        if _.size < 0 : Space.Thruster_Particles.remove( _ ) 
        else : _.Display()
    for _ in Sliders : _.Display()
    for event in pg.event.get() :
        if event.type == pg.QUIT : break 
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
    
pg.quit() 
