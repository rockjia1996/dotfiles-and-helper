import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 


from Menu import Menu


def main(stdscr):
   
    content_win = curses.newwin(20, 20, 0, 0)
    content_win.keypad(True)
    menu = Menu(10, 10)
    menu.render(content_win)


    

    pass



wrapper(main)

print(f"Lines   {curses.LINES}")
print(f"Columns {curses.COLS}")
