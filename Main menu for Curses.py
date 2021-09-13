import curses
import time

menu = ["Play","Options","Scoreboard","Exit"] #Exit should be last element 
                                                                       #as we are terminating by len(menu) - 1
    

def pmenu(s, selected_row_index):
    h , w  = s.getmaxyx()
    
    s.clear()     
    for index , row in enumerate(menu) :
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + index
        if index == selected_row_index :
            s.attron(curses.color_pair(1))
            s.addstr(y,x,row)
            s.attroff(curses.color_pair(1))
        else :
            s.addstr(y,x,row)
    s.refresh()

    
def main(s) :
    curses.curs_set(0)
    curses.init_pair(1,curses.COLOR_BLACK,curses.COLOR_WHITE)
    current_row_index = 0
    pmenu(s,current_row_index) 
    while True :
        key = s.getch()
        s.clear()
        if key== curses.KEY_UP :
            if current_row_index > 0 :
                current_row_index -= 1
        if key== curses.KEY_DOWN :
            if current_row_index < len(menu) - 1 :
                current_row_index += 1
        if key== curses.KEY_ENTER or key in [10,13] :
            s.clear()
            s.addstr(0,0,"<Selected {}>".format(menu[current_row_index]))
            s.getch()
            if current_row_index == len(menu) - 1 :
                break
        pmenu(s,current_row_index)

            
curses.wrapper(main)
#def main(s) :
#   curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_RED) # indifier 1 has color pair x and y ..   
#   h , w = s.getmaxyx()
#   text = "Hello?"
#   x = w//2 - len(text)//2
#   y = h//2
#   s.attron(curses.color_pair(1)) #s.attroff(curses.color_pair(1))
#   s.addstr(y,x,text)
#   s.refresh()
#   time.sleep(3)
