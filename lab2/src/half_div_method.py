def half_div(f, start, stop, epsilon):
    a = start
    b = stop
    x = (start + stop) / 2

    while(abs(b - a) > epsilon):
        x = (a + b) / 2
        if (f(a) * f(x) > 0):
            a = x
        else:
            b = x
    return x
