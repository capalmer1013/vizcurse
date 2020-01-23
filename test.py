from curses import wrapper
import curses
from curses.textpad import Textbox, rectangle
import random
import string
import time
from math import sin

def main(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    while True:
        
        y, x = stdscr.getmaxyx()
        if not random.randint(0, 10):
            # stdscr.clear()
            pass
        for _ in range(int(1)):
            try:
                yset = random.randint(0, y)
                xset = random.randint(0, x)
                character = random.choice(string.ascii_letters+string.punctuation+' '*100)
                character = random.choice([i for i in range(127)])
                color = curses.color_pair(random.randint(0, 254))
                stdscr.addstr(yset, xset, character, color)
            except Exception:
                pass

        time.sleep(0.0)

        stdscr.refresh()
        # stdscr.getch()

def realMain(stdscr):
    while True:
        y, x = stdscr.getmaxyx()

        # c = random.choice(string.ascii_letters+string.punctuation)
        # try:
        #     c = block(y, x)
        #     color = curses.color_pair(random.randint(0, 254))
        #     for _ in range(200):
                
        #         yset = random.randint(0, y)
        #         xset = random.randint(0, x)
        #         stdscr.addstr(yset, xset, c, color)
        #         time.sleep(0.01)
        #         stdscr.refresh()
        # except Exception as e:
        #     pass

        while True:
            curses.start_color()
            curses.use_default_colors()
            for i in range(0, curses.COLORS):
                curses.init_pair(i + 1, i, -1)
            for i in range(y-1):
                for j in range(x-1):
                    try:
                        stdscr.addstr(i, j, block(y, x), curses.color_pair( getColor(i, j)))    
                    except Exception as e:
                        print(e)
            #time.sleep(0.05)
            stdscr.refresh()
            
    stdscr.getch()
def now():
    return (time.time() - startTime)

def getColor(y, x):
    
    return int((x * y * sin(now()*0.25))) + int(sin(now())*4) + int(sin(x)*10)  + int(sin(y)*5)% 256 

def block(y, x):
    return chr(0x2588)

def rand(y, x):
    # chr(random.randint(10, 127))
    return random.choice([chr(random.randint(0x1f600, 0x1f700)),  chr(0x2588)]+[" "]*2)

def flood(y, x, character=0):
    return character

def main2(stdscr):
    for i in range(9000, 10000):
        try:
            stdscr.addstr(str(chr(i)))
        except Exception as e:
            print(e)
            # End of screen reached
    stdscr.getch()

#curses.wrapper()

startTime = time.time()
wrapper(realMain)
