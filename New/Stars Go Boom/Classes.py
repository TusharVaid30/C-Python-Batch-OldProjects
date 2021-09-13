from Globals import *

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
        Circle( self.x , self.y , self.color , self.size )

class Bullet :

    def __init__(self , x , y , dx , dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.Speed = 2
        self.size = 3
        self.color = Color_Light_Red
        self.Type = 0
        self.Damage = 10
        self.Penetrate = False

        self.Wispy = False
        self.Wisps = []
        self.Wisp_Count = 5
        self.Wisps_Set = False

        self.Homing = False
        self.Homing_Target = None

    def Execute(self):
        if self.Wispy:
            if not(self.Wisps_Set):
                sep = 360/self.Wisp_Count
                for _ in range(self.Wisp_Count): self.Wisps.append(Particle(0, 0, 0, 0, Color_Light_Blue, 1, theta = ( _ + 1) * sep, radial = 10 ))
                for wisp in self.Wisps:
                    wisp.dx = cos(wisp.theta)
                    wisp.dy = sin(wisp.theta)
                    wisp.dtheta = 100
                self.Wisps_Set = True
            for wisp in self.Wisps:
                wisp.x = self.x + cos(wisp.theta) * wisp.radial
                wisp.y = self.y + sin(wisp.theta) * wisp.radial
                wisp.theta += wisp.dtheta
                wisp.Display()

        if self.Homing:
            if not(self.Homing_Target): raise NoTargetToHome
            temp_theta = math.acos((self.Homing_Target.x - self.x) / (math.sqrt((self.Homing_Target.x - self.x)**2 + (self.Homing_Target.y - self.y)**2)))
            if self.Homing_Target.y < self.y: temp_theta = -temp_theta
            self.x += math.cos(temp_theta)
            self.y += math.sin(temp_theta)
    def Display(self) :
        #pg.draw.circle( Window,  (255 , 0 , 0) , (int(self.x) , int(self.y)) , int(self.size) )
        Circle( self.x , self.y , self.color , self.size )
    def Move(self) :
        self.x += self.dx * self.Speed
        self.y += self.dy * self.Speed

class Laser:
    def __init__(self, x, y, width, height, theta):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.theta = theta
    def execute(self):
        pass

    def stuff(self):
        self.end_x = self.x
        self.end_y = self.y
        for _ in range(self.height):
            self.end_x += cos(self.theta)
            self.end_y += sin(self.theta)
    def display(self):
        pg.draw.line(Window, Color_White, (self.x, self.y), (self.end_x, self.end_y), self.width)


    def move(self):
        pass


class Ship :
    def __init__( self , x , y , Image , Image_Bit) :
        self.Particles = []
        self.Wisps = []
        self.Thrusters = []
        self.Thruster_Particles = []
        self.Barrels = []
        self.Bullets = []
        self.x = x
        self.y = y
        self.Image = Image
        self.Image_Bit = Image_Bit
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
            self.Barrels.append(Pipe(Barrel[0], Barrel[1], Barrel[2], Bps = Barrel[3] ))

    def Shoot(self):
        for Barrel in self.Barrels :
            Flag = False
            if int((time() - Barrel.Gamma)*Barrel.Bps) >= 1 :
                Flag = True
                Barrel.Gamma = time()
                self.Bullets.append( Bullet( self.x + Barrel.x, self.y + Barrel.y, cos(Barrel.angle) * self.Bullet_Speed, sin(Barrel.angle) * self.Bullet_Speed ))


    def Move( self , Theta ) :
        self.x += self.dx * cos(Theta)
        self.y += self.dy * sin(Theta)
        self.Boost( (Theta + 180 + self.RefTheta )%360 , 1 )

    def Add_Wisp( self , Color , Num ) :
        for _ in range(Num) :
            self.Wisps.append( Particle ( self.x , self.y , 0 , 0 , Color , 5 ,  0 , _*360/Num , 3 , 100 , randint( 5 , 30 )/20  ) )

    def Move_Wisp( self ) :
        for Wisp in self.Wisps :
            Wisp.x = self.x + self.Image_Bit/2 + Wisp.radial*cos( Wisp.theta )
            Wisp.y = self.y + self.Image_Bit/2 + Wisp.radial*sin( Wisp.theta ) #*Wisp.dradial )
            Wisp.theta += Wisp.dtheta
            Wisp.radial += randint(-5,5)/20



    def Twinkle( self ) :
        global Temp_Twinkle
        Temp_Twinkle = False
        Num = 5 # randint(4,10)
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
        #Num += randint(3,7)
        for _ in range(Num) :
            self.Particles.append( Particle ( self.x , self.y ,
                                              0 , 0 ,
                                              ( 0 ,200 , 200 ) ,
                                              7 ,
                                              0.005 ,
                                              _*(360/Num) + 180/Num ,
                                              -3 ,
                                              16,
                                              Num/3 ))

    def Curl( self ) :
        for _ in self.Particles :
            _.theta += _.dtheta
            _.dtheta += 0.015
            _.radial += _.dradial
            _.dradial -= _.ddradial
            _.x = self.x + self.Image_Bit/2 + cos(_.theta)*_.radial
            _.y = self.y + self.Image_Bit/2 + sin(_.theta)*_.radial
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
            _.x = self.x + self.Image_Bit/2 + cos(_.theta)*_.radial
            _.y = self.y + self.Image_Bit/2 + sin(_.theta)*_.radial
            if _.size <= 0 : self.Particles.remove(_)

    def Display_Particles ( self ) :
        for _ in self.Thruster_Particles : _.Display()
        for _ in self.Particles          : _.Display()
        for _ in self.Wisps              :
            Trail_Wisps.append( _ )
            _.Display()

    def Display( self ) :
        Window.blit( self.Image , ( self.x , self.y ) )

    def Flip( self ) :
        self.RefTheta += 180
        self.RefTheta %= 360
        for Thruster in self.Thrusters :
            Thruster.x = self.Image_Bit - Thruster.x
            Thruster.y = self.Image_Bit - Thruster.y
            Thruster.angle += 180
            Thruster.angle %= 360

    def Fire_Laser(self, theta):
        self.Lasers.append(Laser(self.x, self.y, 10, 100, theta))
