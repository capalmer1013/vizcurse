import curses
from multiprocessing import Process, Queue, cpu_count
import math

def printColors(stdscr):
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, 0, i -1)
    
    for i in range(curses.COLORS):
        stdscr.addstr(str(i), curses.color_pair(i))
    stdscr.refresh()
    stdscr.getch()


class Series():
    def __init__(self):
        self.coreCount = cpu_count()

    @staticmethod
    def weierstrauss(x, n, a=0.5, b=7):
        return (a**n) * math.cos((b**n * math.pi * x))


    def sumThread(self, q, i, n, functionToSum, x):
        result=0.0
        if i != 0: i+=1
        for t in range(int(i), int(n+1)):
            result += functionToSum(x, t)

        q.put(result)


    def summation(self, i , n , functionToSum, x=1):
        threads = []
        q = Queue()

        threadWork = n/self.coreCount
        upperBound = threadWork
        lowerBound = 0

        for t in range(0, self.coreCount):
            newThread = Process(target=self.sumThread, args=(q, lowerBound, upperBound, functionToSum, x))
            newThread.start()
            threads.append(newThread)

            lowerBound += threadWork
            upperBound += threadWork

        for thread in threads:
            thread.join()

        result = 0
        while(not q.empty()):
            result += q.get()

        return result


#print("result: "+str(A.summation(0, 100, Series.weierstrauss, .5)))
