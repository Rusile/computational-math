from sympy import *

def get_system():
    print("Do you need to solve system?(y/n)")
    match (input()):
        case 'y':
            return True
        case 'n':
            return False
        case _:
            return True

def read_system_console():
    print("Choose one system:")
    print("1 -------- x^2 + x + 0.2 * y^2 - 0.3")
    print("  -------- x^2 + y - 5 * x * y - 0.7")
    print("2 -------- 0.1 * x^2 + x + 0.2 * y^2 - 0.3")
    print("  -------- 0.2 * x^2 + y - 0.1 * x * y - 0.7")
    x, y = symbols('x y')

    match int(input()):
        case 1:
            f = x + 0.2 * y ** 2 - 0.3
            g = x ** 2 + y - 5 * x * y - 0.7

        case 2:
            f = 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3
            g = 0.2 * x ** 2 + y - 0.1 * x * y - 0.7

        case _:
            f = x ** 2 + x + 0.2 * y ** 2 - 0.3
            g = x ** 2 + y - 5 * x * y - 0.7
    return f, g

def read_equation_console():
    print("Choose one of five equations:")
    print("1 -------- x^3 + 2*x^2 + 3*x (defalut)")
    print("2 -------- -x^3 +  7*x^2 - 3*x - 2")
    print("3 -------- x^3 - 2")
    print("4 -------- x^2 - 1")
    print("5 -------- -x^2 - 3*x + 3")
    x, y = symbols('x y')

    match int(input()):
        case 1:
            return lambda x: x ** 3 + 2 * x ** 2 + 3 * x
        case 2:
            return lambda x: -x ** 3 + 7 * x ** 2 - 3 * x - 2
        case 3:
            return lambda x: x ** 3 - 2
        case 4:
            return lambda x: x ** 2 - 1
        case 5:
            return lambda x: -x ** 2 - 3 * x + 3
        case 6:
            f = x ** 2 + x + 0.2 * y ** 2 - 0.3
            g = x ** 2 + y - 5 * x * y - 0.7
            return f, g
        case 7:
            f = 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3
            g = 0.2 * x ** 2 + y - 0.1 * x * y - 0.7
            return f, g
        case _:
            equation = lambda x: x ** 3 + 2 * x ** 2 + 3 * x
    return equation


def read_interval_console(label):
    print(f"Enter the interval start float value for {label}")
    start = float(input())
    print(f"Enter the interval stop float value for {label} (notice, it has to be greater then start)")
    stop = float(input())

    if (stop <= start):
        print("Error! Stop has to be greater than start!")
        return read_interval_console()
    else:
        return start, stop


def read_epsilon_console():
    print("Enter accuracy:")
    return float(input())


def read_method():
    print("Choose method to calculate root:")
    print("1 -------- Newton method")
    print("2 -------- Half division method")
    print("3 -------- Simple iteration method")
    print("4 -------- Simple iteration method(for systems)")

    return int(input())
