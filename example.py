global current_func
def f(x, y, t):
    return ((t)+1)*0.01 * (x* 0.01)*(y+ 40) + ((x-80)*y*sin(t)*0.1) 

current_func = f
