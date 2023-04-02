from simple_iteration_method import *
def half_devidion():
    print("----------- Метод половинного деления ------------")
    a = -3
    b = -2.5
    e = 0.001
    f = lambda x: -2.7 * x ** 3 - 1.48 * x ** 2 + 19.23 * x + 6.35
    i = 0

    while (abs(a - b) > e):
        xi = a - (a-b)/(f(a)-f(b))*f(a)


        # print(f"i={i} a={round(a, 3)} b={round(b, 3)} x={round(xi, 3)} f(a)={round(f(a),3)} f(b)={round(f(b), 3)} |a-b|={round(abs(a-b),3)}")
        # print(f"|{i}\t|{round(a, 3)}\t|{round(b, 3)}\t|{round(xi, 3)}\t|{round(f(a),3)}\t|{round(f(b), 3)}\t|{round(abs(a-b),3)}|")
        print(
            f"{i}     {round(a, 3)}     {round(b, 3)}     {round(xi, 3)}     {round(f(xi), 3)}\t& {round(abs(a - b), 3)}\\\\\n\\hline")

        a = b
        b = xi
        i += 1
    print(f"calculation result: root={round((a + b) / 2, 3)}")


def hord_method():
    print("----------- Метод секущих ------------")
    a = 2
    b = 3
    e = 0.01
    f = lambda x: -2.7 * x ** 3 - 1.48 * x ** 2 + 19.23 * x + 6.35
    i = 0
    xi = b

    while (abs(f(xi)) > e):
        xi = a - ((b - a) * f(a)) / (f(b) - f(a))
        print(
            f"{i}     {round(a, 3)}     {round(b, 3)}     {round(xi, 3)}    {round(f(a), 3)}     {round(f(b), 3)}     {round(f(xi), 3)}     {round(abs(a - b), 3)}\\\\\n\\hline")
        if (f(xi) * f(a) > 0):
            a = xi
        else:
            b = xi
        i += 1
    print(f"calculation result: root={round(xi, 3)}")


def simple_iteration():
    print("----------- Метод простой итерации ------------")
    a = -1
    b = 0
    e = 0.001



    f = lambda x: -2.7 * x ** 3 - 1.48 * x ** 2 + 19.23 * x + 6.35

    l = find_lambda(f, a, b)
    q = find_q(f,a,b)
    phi = lambda x: x + f(x) * l
    i = 0
    xi = b
    x_prev = xi + 2 * e

    while (abs(xi - x_prev) > e):
        x_prev = xi
        xi = phi(xi)
        print(
            f"{i}, {round(x_prev, 3)}, {round(xi, 3)}, {round(f(xi), 3)}, {round(abs(xi - x_prev), 3)} ")
        i += 1
    print(f"calculation result: root={round(xi, 3)}")


hord_method()
half_devidion()
simple_iteration()
