import math

import numpy as np
from scipy.misc import derivative

from sympy import *


def find_root_simple_iteration_double(f, g, start_x, start_y, stop_x, stop_y, epsilon):
    print("__________________simple iteration__________________")

    q_x = find_q_d_x(f, start_x, stop_x)
    l_x = -1 / q_x

    print(f"lambda={round(l_x, 5)}, q=={round(q_x, 5)}")

    q_y = find_q_d_y(g, start_y, stop_y)
    l_y = -1 / q_y

    print(f"lambda={round(l_y, 5)}, q=={round(q_y, 5)}")

    phi_y = lambda x, y: y + round(lambdify(symbols('x y'), g, 'numpy')(x, y), 10) * l_y
    print(f"phi(y) = y + g(x)*{round(l_y, 3)}")

    phi_x = lambda x, y: x + round(lambdify(symbols('x y'), f, 'numpy')(x, y), 10) * l_x
    print(f"phi(x) = x + f(x)*{round(l_x, 3)}")

    check = lambda epsilon_, yi_prev_, xi_prev_, xi_, yi_: (abs(xi_ - xi_prev_) > epsilon_ or xi_ == xi_prev_ or
                                                            abs(yi_ - yi_prev_) > epsilon_ or yi_ == yi_prev_)

    x0 = start_x
    x1 = phi_x(stop_x, stop_y)
    xi = x1
    xi_prev = x0

    y0 = start_y
    y1 = phi_y(stop_x, stop_y)
    yi = y1
    yi_prev = y0
    tmp = 0

    while check(epsilon, yi_prev, xi_prev, xi, yi):
        tmp_x = xi
        tmp_y = yi

        xi = phi_x(xi_prev, yi_prev)
        yi = phi_y(xi_prev, yi_prev)
        if tmp % 2 == 1:
            yi_prev = tmp_y
            xi_prev = tmp_x
        tmp += 1

    print("__________________simple iteration end__________________")

    return xi if not math.isnan(xi) else xi_prev, yi if not math.isnan(yi) else yi_prev, (tmp+1)//2


def find_root_simple_iteration(f, start, stop, epsilon):
    print("__________________simple iteration__________________")
    l = find_lambda(f, start, stop)
    q = find_q(f, start, stop)

    print(f"lambda={round(l, 5)}, q=={round(q, 5)}")

    phi = lambda x: x + f(x) * l
    print(f"phi(x) = x + f(x)*{round(l, 3)}")

    if (q > 0.5):
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) > epsilon
    else:
        check = lambda epsilon, xi, xi_prev, q: abs(xi - xi_prev) >= (1 - q / q) * epsilon

    x0 = start
    x1 = phi(x0)

    xi = x1
    xi_prev = x0

    while (check(epsilon, xi, xi_prev, q)):
        tmp = xi
        xi = phi(xi_prev)
        xi_prev = tmp
    print("__________________simple iteration end__________________")

    return xi


def find_q_d_x(f, start, stop):
    der_str = f.diff(Symbol('x'))
    der = lambdify(symbols('x y'), der_str, 'numpy')
    max_derivative = abs(der(start, 0))
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(der(i, 0)):
            max_derivative = abs(der(i, 0))
    return max_derivative


def find_q_d_y(f, start, stop):
    der_str = f.diff(Symbol('y'))
    der = lambdify(symbols('x y'), der_str, 'numpy')
    max_derivative = abs(der(0, start))
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(der(0, i)):
            max_derivative = abs(der(0, i))
    return max_derivative


def find_lambda(f, start, stop):
    max_derivative = abs(derivative(f, start, n=1))
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1)):
            max_derivative = abs(derivative(f, i, n=1))
    return -1 / max_derivative


def find_q(f, start, stop):
    max_derivative = derivative(f, start, n=1)
    for i in np.arange(start, stop, 0.01):
        if max_derivative < abs(derivative(f, i, n=1)):
            max_derivative = abs(derivative(f, i, n=1))
    return max_derivative
