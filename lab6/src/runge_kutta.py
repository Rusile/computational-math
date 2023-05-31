from decimal import Decimal
import numpy as np
from math import ceil

def runge_kutta(x0, y0, xf, h, f):
    while x0 < xf:
        if x0+h > xf: h=xf-x0
        k1 = h*f(x0,y0)
        k2 = h*f(x0+0.5*h,y0+0.5*k1)
        k3 = h*f(x0+0.5*h,y0+0.5*k2)
        k4 = h*f(x0+h,y0+k3)
        y0+=(k1+2*k2+2*k3+k4)/6
        x0+=h
    return y0

def runge_kutta_differentiation(f, initial_conditions, h, bounds, e):
    # print("_____________________ RUNGE-KUTA _____________________________")
    n = ceil((bounds[1] - bounds[0])/ h) + 1 # здесь добавляется 1, чтобы количество точек было правильным (у k интервалов k+1 конец)
    # print(f"bounds=[{bounds[0]}, {bounds[1]}], diff={bounds[1]-bounds[0]}, h={h}, n={n}")
    # для этих иксов нужно предсказать значение y
    x = [bounds[0] + h*i for i in range(n)]
    y = [0]*(n)
    hes = [0]*(n) # ширина интервала для необходимой точности
    y[0] = initial_conditions
    
    # print(f"h\t\ty1\t\ty2\t\tR\t\te")
    for i in range(n - 1):
        # print(f"--x{i}--")
        h0 = h
        a = x[i]
        b = x[i + 1]
        y0 = y[i]
        y2, R, h0 = do_iteration(h0, a, b, y0, f, e)
        while R >= e:
            y2, R, h0 = do_iteration(h0, a, b, y0, f, e)
        y[i + 1] = y2
        hes[i + 1] = h0
    # print("_____________________ RUNGE-KUTA END _____________________________")
    return y, x, hes

def do_iteration(h0, a, b, y0, f, e):
    y1 = runge_kutta(a, y0, b, h0, f)
    h0 /= 2
    y2 = runge_kutta(a, y0, b, h0/2, f)
    R = abs(y1 - y2) / (2**(-fexp(e)) - 1)
    # print(f"{h0}\t\t{round(y1, 3)}\t\t{round(y2, 3)}\t\t{round(R)}\t\t{e}")
    return y2, R, h0

def fexp(number):
    (sign, digits, exponent) = Decimal(number).as_tuple()
    return len(digits) + exponent - 1