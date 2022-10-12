import curses

class Menu():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = None
        self.options = {
            "Display": "Some Display Object",
            "Network": "Some Network Object",
            "Date": "Some Date Object",
        }
        self.selected_label = None
        self.selected_index = None

    def register(self, label, controller):
        self.option[label] = controller


    def read_selection(self, render_target):
        while True:
            key = render_target.getkey()




            if key == curses.KEY_UP:
                render_target.addstr(5, 0, "Arrow up")
            elif key == curses.KEY_DOWN:
                render_target.addstr(5, 0, "Arrow down")
            elif key == curses.KEY_LEFT:
                render_target.addstr(5, 0, "Arrow left")
            elif key == curses.KEY_RIGHT:
                render_target.addstr(5, 0, "Arrow right")



            #render_target.addstr(5, 0, curses.KEY_UP)
            render_target.refresh()


    def render(self, render_target):
        # render_target is window object of curses

        entry_names = list(self.options.keys())
        
        for row in range(len(entry_names)):
            render_target.addstr(row, 0, entry_names[row])
    
        render_target.refresh()
        self.read_selection(render_target) 
    
