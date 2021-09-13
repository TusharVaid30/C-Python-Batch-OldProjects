import pygame as pg
from random import randint as R , choice as C
import math
def cos( x ) : return math.cos( x*math.pi/180 ) 
def sin( x ) : return math.sin( x*math.pi/180 )
def tan( x ) : return math.tan( x*math.pi/180 )

Text_Size = 20

pg.init()
Window_Width  = 500 # pg.display.Info().current_w
Window_Height = 500 # pg.display.Info().current_h
Window = pg.display.set_mode((Window_Width, Window_Height) ) #, pg.FULLSCREEN )

def Line( Start , End ) :
  pg.draw.line( Window , ( 255 , 255 , 255 ) , ( Start[0] , Start[1] ) , ( End[0] , End[1] ) , 1 ) 

def Write( x , y , Text ) :
  Window.blit( pg.font.SysFont( None , Text_Size ).render( str(Text) , True , ( 255 , 255 , 255 ) ) , ( x , y ) ) 

def Circle( x , y , Radius , Color ) :
  pg.draw.circle( Window, Color , (int(x) , int(y)) , abs(int(Radius)) )
        
def Rectangle( x , y , Width , Height , Color ) :
  pg.draw.rect( Window , Color , ( x - Width/2 , y - Height/2 , Width , Height ) )

def Tilt( x , y , Angle ) :
  Temp_x = x
  Temp_y = y
  x = Temp_x*cos(Angle) - Temp_y*sin(Angle)
  y = Temp_x*sin(Angle) + Temp_y*cos(Angle)
  return x , y

Sliders = [] 
class Slider :
    def __init__( self , Min_Value , Max_Value , x , y , Name = "Slider" , Length = 100 ):
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
        self.Fresh()

        Sliders.append( self ) 
        
        
    def Fresh( self ) :
        self.Variable_Color = ( 100 , 100 , 100 )
        self.Mover_Color = ( 200 , 200 , 200 )
        self.Mover_Radius = 10
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


Slider_One = Slider( 0 , 100 , Window_Width/2 , Window_Height/2 )
Slider_Two = Slider( 250 , 420 , Window_Width/3 , Window_Height/3 )
Current_Slider = Sliders[0]

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
        
        
while True :
    Window.fill( ( 0 , 0 , 0 ) )
    
    Slider_Driver()
    
    for Slider in Sliders : Slider.Display()

    for event in pg.event.get() :
        if event.type == pg.QUIT : break
    if pg.key.get_pressed()[pg.K_ESCAPE]: break
    pg.display.flip()
    
pg.quit()
