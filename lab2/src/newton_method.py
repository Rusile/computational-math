import numpy as np
from scipy.misc import derivative


def find_root_newton(equation, start, stop, epsilon):
    if not check_interval(equation, start, stop): return None
    x0 = choose_x0(equation, start)
    x1 = x0 - equation(x0) / derivative(equation, x0, n=1)

    xi = x1
    xi_prev = x0
    print(f"i\tx_i\tf(xi)\tf'(xi)\tx_i+1\t|x_i+1-xi|")
    print(
        f"i={0}\t{round(xi_prev, 3)}\t{round(equation(xi_prev), 3)}\t{round(derivative(equation, xi_prev, n=1), 3)}\t{round(xi, 3)}\t{round(abs(xi - xi_prev), 3)}")
    i = 1
    while abs(xi - xi_prev) > epsilon:
        xi_prev = xi
        xi = xi - equation(xi) / derivative(equation, xi, n=1)
        print(
            f"i={i}\t{round(xi_prev, 3)}\t{round(equation(xi_prev), 3)}\t{round(derivative(equation, xi_prev, n=1), 3)}\t{round(xi, 3)}\t{round(abs(xi - xi_prev), 3)}")
        i += 1

    return xi


def check_interval(equation, start, stop):
    if not equation(start) * equation(stop) < 0: return False
    start_derivative_fst = derivative(equation, start, n=1)
    start_derivative_snd = derivative(equation, start, n=2)

    # points = [round(x * 0.01, 1) for x in range(start, stop)]
    for i in np.arange(start, stop, 0.01):
        if not ((start_derivative_fst * derivative(equation, i, n=1) > 0)
                and (start_derivative_snd * derivative(equation, i, n=2) >= 0)):
            print(
                f"start_fst={start_derivative_fst}, start_snd={start_derivative_snd}, derivative(n=1)={derivative(equation, i, n=1)} derivative(n=2)={derivative(equation, i, n=2)}")
            return False
    return True


def choose_x0(equation, start):
    start_derivative_snd = derivative(equation, start, n=2)
    if (start_derivative_snd * start > 0):
        return start
    else:
        return True
