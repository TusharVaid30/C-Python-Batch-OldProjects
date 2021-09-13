from turtle import *
from random import *
import math , subprocess , time
scale   = 50
sped = 1
lineedge = scale*3.6
mod = 2/3
pi2 = 2*3.14159265358979323846264338327950
rt2 = 2**0.5
frameskip  = 10*sped
frameskip2 = 1*sped
undoskip   = 1
LINEframeskip1 = 20*sped
listen()
w   = Screen() ; w.bgcolor("black") ; w.tracer(0) ; w.setup(7*scale,7*scale)
t,tt,t1,t2,t3,t4  = Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle()
t .ht(); t .speed(0); t .pu(); t.moves = 0
tt.ht(); tt.speed(0); tt.pu(); tt.moves= 0
t.setundobuffer(6516)            ; tt.setundobuffer(10*305)
a   = [ [(-2*scale ,  2*scale) , (0 ,  2*scale) , (2*scale ,  2*scale)] ,
        [(-2*scale ,     0   ) , (0 ,     0   ) , (2*scale ,     0   )] ,
        [(-2*scale , -2*scale) , (0 , -2*scale) , (2*scale , -2*scale)] ]
b   = [ [" "," "," "] ,
        [" "," "," "] ,
        [" "," "," "] ]
T   = [t1, t2 , t3 ,t4]
player   = choice(("X","O"))
current  = True
winnerdecided = False
Wantedquit = False
localmoves , moves = 0 , 0
Xwins , Owins = 0 , 0
round_   = 0
xwin,ywin= 10,10
dagwin   = ""
loser    = "<eror>"
LINEtxt  = "<rror>"
spa      = 15*"-"
tabelcolors = ("magenta","green","blue","yellow")
peicecolors = ("white","white")
cutcolors   = ("red","red") #magenta","cyan","purple","pink")
#==============================================================================
def O(A,TUR = t) :
    global current
    current = False
    lin = randint(1,64)*pi2/randint(1,64)
    lan = choice((1,-1))
    TUR.pu()
    TUR.goto(A[0] - scale*mod*math.cos(lin) , A[1] + scale*mod*math.sin(lin))
    TUR.setheading(lan*270-math.degrees(lin))
    TUR.pd()
    TUR.moves += 4
    for _ in range(360) :
        TUR.fd(pi2*mod*scale/360)
        TUR.lt(lan)
        TUR.moves += 2
        if _%frameskip == 0 : w.update()
    w.update()
    current = True
def Xm(x,y,z = 1,TUR = t) :
    TUR.pu()
    d = choice((-1,1))
    TUR.goto( x + z*d*mod*scale , y + d*mod*scale)
    if d == - 1 : TUR.setheading((z*45)) 
    if d ==   1 : TUR.setheading((z*45)+180)
    if z !=   1 : TUR.lt(180)
    TUR.pd()
    TUR.moves += 4
    for _ in range(int(TUR.distance( x - z*d*mod*scale , y - d*mod*scale))) :
        TUR.fd(1)
        TUR.moves += 1
        if _%frameskip == 0 : w.update()
def X(A) :
    global current
    current = False
    lin = choice((1,-1))
    Xm(A[0],A[1],lin) ; Xm(A[0],A[1],-lin)
    current = True
def LINE(alin , x , y ,TUR = tt) :
    d = choice((-1,1))
    if alin == "h" :
        TUR.goto(d*lineedge,a[x][y][1])
        if d == 1  : TUR.setheading(180) 
        else : TUR.setheading(0)
    if alin == "v" : TUR.goto(a[x][y][0],d*lineedge) ; TUR.setheading(d*-90)
    TUR.pd()
    for _ in range(int(2*lineedge)) :
        TUR.fd(1)
        TUR.moves += 1
        if _%LINEframeskip1 == 0 : w.update()
def dLINE(alin , TUR = tt) :#DAG
    d = choice((-1,1))
    if alin == "dl" :
        TUR.goto(-d*lineedge,d*lineedge)
        if d == 1  : TUR.setheading(-45) 
        else : TUR.setheading(90+45)
    if alin == "dr" :
        TUR.goto(-d*lineedge,-d*lineedge)
        if d == 1  : TUR.setheading(45) 
        else : TUR.setheading(-(90+45))
    TUR.pd()
    for _ in range(int(2*rt2*lineedge)) :
        TUR.fd(1)
        TUR.moves += 1
        if _%LINEframeskip1 == 0 : w.update()
#==============================================================================
def checkin() :
    global loser,current,winnerdecided,LINEtxt,xwin,ywin ; current = False
    y = 0
    for x in range(3) :
        if b[x][0] == b[x][1] == b[x][2] != " " :
            LINEtxt = [[x],[y]]; xwin = x
            LINE("h" , x , y ) ; loser = player; winnerdecided = True ; return True
    x = 0
    for y in range(3) :
        if b[0][y] == b[1][y] == b[2][y] != " " :
            LINEtxt = [[x],[y]]; ywin = y
            LINE("v" , x , y ) ; loser = player; winnerdecided = True ; return True
    if b[0][0] == b[1][1] == b[2][2] != " " :
        LINEtxt = "l"          ; dagwin = "l"
        dLINE("dl") ; loser = player ; winnerdecided = True ; return True
    if b[2][0] == b[1][1] == b[0][2] != " " :
        LINEtxt == "r"         ; dagwin = "r"
        dLINE("dr") ; loser = player ; winnerdecided = True ; return True
    current = True #OBFISTICATE THIS
def tileclick(x,y) :
    if current == True :
        xtile , ytile = 10,10
        if x in range (-3*scale ,  -scale) : ytile = 0
        if x in range (-scale   ,   scale) : ytile = 1
        if x in range (scale    , 3*scale) : ytile = 2
        if y in range (-3*scale ,  -scale) : xtile = 2
        if y in range (-scale   ,   scale) : xtile = 1
        if y in range (scale    , 3*scale) : xtile = 0
        if xtile == 10 or ytile == 10 : return
        if b[xtile][ytile] == " " : play(xtile,ytile)
#======================
def randomplay():
    imdone = False
    x = randint(0,2)
    y = randint(0,2)
    if b[x][y] == " " : play(x,y) #print(player,"RANDOMED!") 
def computer(Gameover,compplayer) :
    cheating = False
    cheated  = False
    if compplayer == "X" : elseplayer = "O"
    else : elseplayer = "X"
    #UNETHICAL MOVESET
    #REMOVE THE BELOW CODE
    if player == compplayer and cheating and not cheated :
        if b[1][1] == elseplayer : print("Enemy has center!")
        if b[1][1] == compplayer : print("We have taken over the center!")
        if b[1][1] == " "        : print("Center Ready to take!")
        cheated = True
    #TOTALLY CHEATS ^^^
    if player == compplayer and not Gameover:
        for me in [compplayer,elseplayer]:
            for _ in range(3) :#H
                if b[_][0] == b[_][1] == me and b[_][2] == " " : play(_,2) ; return
                if b[_][2] == b[_][0] == me and b[_][1] == " " : play(_,1) ; return
                if b[_][1] == b[_][2] == me and b[_][0] == " " : play(_,0) ; return
            for _ in range(3) :#V
                if b[0][_] == b[1][_] == me and b[2][_] == " " : play(2,_) ; return
                if b[2][_] == b[0][_] == me and b[1][_] == " " : play(1,_) ; return
                if b[1][_] == b[2][_] == me and b[0][_] == " " : play(0,_) ; return
            #Dagonal check
            if b[0][0] == b[1][1] == me and b[2][2] == " " : play(2,2) ; return
            if b[2][2] == b[0][0] == me and b[1][1] == " " : play(1,1) ; return
            if b[1][1] == b[2][2] == me and b[0][0] == " " : play(0,0) ; return
            if b[0][2] == b[1][1] == me and b[2][0] == " " : play(2,0) ; return
            if b[2][0] == b[0][2] == me and b[1][1] == " " : play(1,1) ; return
            if b[1][1] == b[2][0] == me and b[0][2] == " " : play(0,2) ; return
        randomplay()
    #if b[x][y] == " " : play(x,y)
    

#======================
def play(x,y):
    global player
    global b
    global moves , localmoves
    moves += 1
    localmoves += 1
    if player == "X" :
        b[x][y]= "X" ; X(a[x][y]) ; player = "O" ; return
    if player == "O" :
        b[x][y]= "O" ; O(a[x][y]) ; player = "X" ; return
#-----------------------------------------------------
def tabel(cl = "") :
    if cl != "white"  : cl = choice(tabelcolors)
    for _ in T :
        _.pu() ;   _.color(cl) ; _.ht() ; _.width(1)   
    t1.goto(-scale ,  3*scale) ; t1.setheading(270)
    t2.goto( scale , -3*scale) ; t2.setheading(90)
    t3.goto( 3*scale ,  scale) ; t3.setheading(180)
    t4.goto(-3*scale , -scale) ; t4.setheading(0)
    for _ in T :
        _.pd()
    for _ in range(6*scale) :
        for __ in T :
            __.fd(1)
        if _%frameskip2 == 0 :
            w.update()
def antitabel() :
    undos = 0
    for _ in range(6*scale) :
        for __ in T :
            __.undo()
            for ___ in range(undoskip) :
                if undos > t.moves : break
                else :
                    for ____ in range(5) : t.undo() ; undos += 1
            tt.undo()
        if _%frameskip2 == 0 :
            w.update()
    #t.clear()
def maketabel() :
    for _ in range(3) :
        for __ in range(3) :
            if b[_][__] == "X" : X(a[_][__])
            if b[_][__] == "O" : O(a[_][__])
def TXTtabeldraw() :
    #TOTAL 6x10
    for _ in range(3):
        print(end=" ")
        for __ in range(3) :
            if __ != 2 : print(b[_][__],end = " | ")
            else : print(b[_][__])
        if _ != 2 : print(2*"___|"+"___")
        else : print(2*"   |")

        
def TXTtabel() :
    x = ywin
    y = xwin
    count = 0
    if x == 10 :
        for _ in range(3):
            if y == _ : print(end="-")
            else : print(end=" ")
            for __ in range(3) :
                if y == _ and __ != 2 : print(b[_][__],end = "-|-")
                elif __ != 2 : print(b[_][__],end=" | ")
                elif _ == y  : print(b[_][__],end="-\n")
                else :         print(b[_][__])
            if _ != 2 : print(2*"___|" + "___")
            else : print(2*"   |")
##    if y == 10 :
##        for _ in range(3):
##            print(end=" ")
##            for __ in range(3) :
##                if __ != 2 : print(b[_][__],end = " | ")
##                else : print(b[_][__])
##            if x == _ : print("line")
##            elif _ != 2 : print(2*"___|" + "___")
##            else : print(2*"   |")
##    if dagwin == "l" :
##        for _ in range(3):
##        print(end=" ")
##        for __ in range(3) :
##            if __ != 2 : print(b[_][__],end = " | ")
##            else : print(b[_][__])
##        if _ != 2 : print(2*"___|"+"___")
##        else : print(2*"   |")
def refilltabel(piece = " ") :
    global b
    for _ in range(3) :
        for __ in range(3) : b[_][__] = piece
def cleartabel(TUR = t) :
    global current
    current = False
    print(spa,"NEW MATCH",spa,"\n\n")
    refilltabel()
    antitabel()
    w.update()
    time.sleep(0.1)
    tabel()
    current = True
def endmatch():
    global Wantedquit ; Wantedquit = True
#-----------------------------------------------------
def Game() :
    global round_ , localmoves , winnerdecided , xwin , ywinw , Wantedquit 
    t.setundobuffer(440*scale)
    tt.moves , t.moves = 0 , 0
    localmoves  = 0
    xwin , ywin = 10 , 10
    Wantedquit , Gameover = False , False
    winnerdecided = False
    round_+= 1
    tt.color(choice(cutcolors))
    t.color(choice(peicecolors))
    #tmp = subprocess.call("cls",shell = True)
    print("Round ",round_,"\n:>",player,"goes first")
    while not Gameover:
        if localmoves == 9 : Gameover = True ; return "00000000f"
        w.update()
        if current == True :
            computer(Gameover,"X") ; Gameover = checkin()
            #computer(Gameover,"O") ; Gameover = checkin()
            onscreenclick(tileclick) ; Gameover = checkin()
            onkey(endmatch,"e")
        #Gameover = checkin()
        if winnerdecided == True : return loser
        if localmoves == 9 : Gameover = True ; return "00000000f"
        if Wantedquit :      Gameover = True ; return "00000000a"
        
        
def Results() :
    global Xwins,Owins
    if loser == "O" : winner = "X" ; Xwins += 1
    if loser == "X" : winner = "O" ; Owins += 1
    if loser == "00000000f" : print("Draw Game")
    if loser == "00000000a" : print("Quit Match")
    if loser in("O","X")    : print(winner,"won!")
    print("Match results:")
    #if loser != "00000000f" : TXTtabel()
    #else : TXTtabeldraw()
    TXTtabeldraw()
    #print(tt.moves,"by tt")
    print(localmoves,"moves played in this match.\nTotal moves :",moves)
    print("X wins :>",Xwins)
    print("O wins :>",Owins)


####################################
tabel("white")
##refilltabel("O")
##maketabel()
##w.update()
##print(t.moves)
while True :
    loser = Game()
    Results()
    cleartabel()
####################################    























