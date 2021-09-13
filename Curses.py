import curses
import time

##w = curses.initscr()
##
##curses.curs_set(0)   #
##curses.noecho()       # disable you writing
##curses.cbreak()        # instant input
##w.keypad(True)        # somewhat like listen()
##
##w.addstr(5,5,"hello") #y,x
##w.refresh()
##time.sleep(3)
##
##curses.echo()
##curses.nobreak()
##w.keypad(False)
##
##curses.endwin() # close
char = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def main(stdscr):
    curses.curs_set(0)
    while True :
        for i in range(26) :
            c= i%26
            for j in range(100) :
                stdscr.addstr(i,j,char[c])
            stdscr.refresh()
            time.sleep(0.1)
    stdscr.cls
curses.wrapper(main)
