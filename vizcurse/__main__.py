import os
import argparse
import curses
from curses import wrapper
import random
import string
import time
from math import sin

# parse args
parser = argparse.ArgumentParser(description='Live coded visuals in the terminal')
parser.add_argument('-i', type=str, nargs=1, help='Input file to read.', required=True)
args = parser.parse_args()

# set vars
startTime = time.time()
FILE_PATH = args.i[0]  # not sure if there's a right way to do this
lastupdateTime = os.path.getmtime(FILE_PATH)
current_func = lambda x, y, t: 0
exec(open(FILE_PATH).read())

def now():
    return (time.time() - startTime)

def randchr():
    return random.choice(string.ascii_letters+string.punctuation)

def updateFunc():
    global current_func
    global lastupdateTime
    newUpdateTime = os.path.getmtime(FILE_PATH)
    if newUpdateTime > lastupdateTime:
        lastupdateTime = os.path.getmtime(FILE_PATH)
        exec(open(FILE_PATH).read())

def getColor(y, x):
    t = now()
    result = int(current_func(x, y, t))
    return result % curses.COLORS


def realMain(stdscr):
    updateFunc()
    while True:
        y, x = stdscr.getmaxyx()
        while True:
            updateFunc()
            curses.start_color()
            curses.use_default_colors()

            for i in range(0, curses.COLORS):
                curses.init_pair(i + 1, 0, i -1)

            # random.seed(1)
            for i in range(y-1):
                for j in range(x-1):
                    stdscr.addstr(i, j, ' ', curses.color_pair( getColor(i, j)))    

            stdscr.refresh()

    stdscr.getch()

wrapper(realMain)
