

global current_func
def f(x, y, t):
	#return sin(t)*10
	return Series.weierstrauss(x, t, y, t)

current_func = f
