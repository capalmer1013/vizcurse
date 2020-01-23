global current_func
def f(x, y, t):
    # return (x*sin(y)*sin(t)*0.5*(sin(x/(y or 1))))
    return (x%7) + (y%5)   + t *16 + x**2 / (y or 1)
    # return ((t)+1)*0.01 * y + (x*y*sin(t)*0.1)
    # return random.randint(0, 256)
current_func = f
