import cProfile, pstats, io
import curses
import vizcurse as vc


w = curses.initscr()

pr = cProfile.Profile()
pr.enable()

try:
    x, y = vc.api.main(w, limit=500)
finally:
    curses.endwin()


print(x, ",", y)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())