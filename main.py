import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle
import time 


from Menu import Menu


def main(stdscr):
    menu = Menu(10, 10)


    menu.render(curses.newwin(10, 10, 0, 0))


    

    pass



wrapper(main)

print(f"Lines   {curses.LINES}")
print(f"Columns {curses.COLS}")
