import os
import argparse
import itertools
import curses
from curses import wrapper
import random
import string
import time
from math import sin
import sys

def now():
    return (time.time() - startTime)

def randchr():
    return random.choice(string.ascii_letters+string.punctuation)

def updateFunc():
    global current_func
    global lastupdateTime
    global file_contents
    try:
        newUpdateTime = os.path.getmtime(FILE_PATH)
        if newUpdateTime > lastupdateTime:
            lastupdateTime = os.path.getmtime(FILE_PATH)
            file_contents = open(FILE_PATH).read()
            exec(file_contents)
    except:
        pass

def getColor(y, x):
    t = now()
    result = int(current_func(x, y, t))
    return result % curses.COLORS

def main(stdscr, limit=0):
    def loop():
        global file_contents
        global HIDE_OVERLAY
        updateFunc()

        for i in range(0, curses.COLORS):
            curses.init_pair(i + 1, 0, i - 1)

        # random.seed(1)
        for product in itertools.product(range(y-1), range(x-1)):
            stdscr.addstr(
                product[0],
                product[1],
                ' ',
                curses.color_pair(getColor(product[0], product[1]))
            )
        # Draw code block
        if not HIDE_OVERLAY:
            file_content_lines = file_contents.splitlines()
            for line_y, line_content in enumerate(file_content_lines, start=3):
                stdscr.addstr(line_y, 0, '{} '.format(line_content))

        stdscr.refresh()

    y, x = stdscr.getmaxyx()
    curses.start_color()
    curses.use_default_colors()
    # Try to hide cursor at the end of the code block (could error in some terminals)
    try:
        curses.curs_set(0)
    except curses.error:
        pass
    if limit:
        for _ in range(limit):
            loop()
        return x, y
    else:
        while True:
            loop()

# parse args - none are required and defaults are set so __name__ does not need to be checked
#   If in the future any args become required, we can do:
#       REQUIRED = __name__ == 'api'
#       parser.add_argument('-E', required=REQUIRED)
parser = argparse.ArgumentParser(description='Live coded visuals in the terminal')
parser.add_argument('-i', type=str, help='Input file to read.', default='example.py')
parser.add_argument('--hide-overlay', help='Hide code overlay.', action='store_true')
args = parser.parse_args()

# set vars
FILE_PATH = args.i
HIDE_OVERLAY = args.hide_overlay

startTime = time.time()
lastupdateTime = os.path.getmtime(FILE_PATH)
current_func = lambda x, y, t: 0
file_contents = open(FILE_PATH).read()
exec(file_contents)
