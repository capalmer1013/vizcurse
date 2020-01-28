
def realMain(stdscr):
    while True:
        y, x = stdscr.getmaxyx()
        while True:
            curses.start_color()
            curses.use_default_colors()

            for i in range(0, curses.COLORS):
                curses.init_pair(i + 1, 0, i -1)

            random.seed(1)
            for i in range(y-1):
                for j in range(x-1):
                    stdscr.addstr(i, j, randchr(), curses.color_pair( getColor(i, j)))    

            stdscr.refresh()
            
    stdscr.getch()