import curses

def printColors(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, 0, i -1)
    
    for i in range(curses.COLORS):
        stdscr.addstr(str(i), curses.color_pair(i))
    stdscr.refresh()
    stdscr.getch()
