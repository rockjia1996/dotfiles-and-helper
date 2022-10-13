import curses

class Menu():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = None
        self.options = [
            "Display", "Network", "Date" 
        ]
        self.selected = 0

    def register(self, controller):
        self.options.append(controller)


    def read_selection(self, render_target):
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

        while True:
            key = render_target.getkey()
           
            if key == "q": break

            if key == "KEY_UP":
                if self.selected > 0:
                    self.selected -= 1
                

            if key == "KEY_DOWN":
                if self.selected < len(self.options) - 1:
                    self.selected += 1


            for i in range(len(self.options)):
                content = self.options[i] + " " * (19 - len(self.options))
                if i == self.selected:
                    render_target.move(self.selected, 0) 
                    render_target.clrtoeol() 
                    render_target.addstr(
                        self.selected, 
                        0,
                        content,
                        curses.color_pair(1)
                    )
                else:
                    render_target.move(i, 0) 
                    render_target.clrtoeol() 
                    render_target.addstr(
                        i,
                        0,
                        content)

                    render_target.refresh()




    def render(self, render_target):
        # render_target is window object of curses
        padding = 20

        for i in range(len(self.options)):
            content = self.options[i] + " " * (19 - len(self.options))
            render_target.addstr(i, 0, content)
    
        render_target.refresh()
        self.read_selection(render_target) 
    
