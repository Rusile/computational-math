from math import sin, log2, sqrt, exp


def get_data():
    print("Choose function:")
    print("1 ----------------- y' = 2x")
    print("2 ----------------- y' = e^(-3*x)")
    print("3 ----------------- y' = 1/sqrt(x**2 - 1)")

    while True:
        try:
            choose_data_method = int(input())
            match (choose_data_method):
                case 1:
                    f = lambda x, y: 2 * x
                    break
                case 2:
                    f = lambda x, y: exp(-3 * x)
                    break
                case 3:
                    f = lambda x, y: 1 / sqrt(x ** 2 - 1)
                    break
                case _:
                    print("Enter your choice again!")
        except ValueError:
            print("Value has be integer! Try again from new line...")

    print("Enter segment's bounds (enter the values separated by a space):")
    while True:
        try:
            values = input().strip().split()
            values = [float(i) for i in values]
            if (len(values) == 2):
                bounds = (min(values[0], values[1]), max(values[0], values[1]))
                break
            else:
                print("Wrong format! Try again from new line...")
        except ValueError:
            print("Both values has be float! Try again from new line...")

    print("Enter the initial conditions as y(x_0)= ...")
    while True:
        try:
            initial_conditions = float(input())
            break
        except ValueError:
            print("Value has be float! Try again from new line...")

    x0 = bounds[0]
    y0 = initial_conditions
    match (choose_data_method):
        case 1:
            f_result = lambda x: x ** 2 + y0 - x0 ** 2
        case 2:
            f_result = lambda x: -1 / 3 * exp(-3 * x) + 1 / 3 * exp(-3 * x0) + y0
        case 3:
            f_result = lambda x: log2(abs(x + sqrt(x ** 2 - 1))) + y0

    print("Enter accuracy:")
    while True:
        try:
            accuracy = float(input())
            if 0 < accuracy and accuracy <= 1:
                break
            else:
                print("Value has to be in (0;1]. Try again from new line...")
        except ValueError:
            print("Value has be float! Try again from new line...")

    print("Enter length of intervals h:")
    while True:
        try:
            h = float(input())
            if h > bounds[1] - bounds[0]:
                print("Length of intervals must be less than entered interval! Try again from new line..")
            else:
                break
        except ValueError:
            print("Value has be integer! Try again from new line...")

    print("Choose method:")
    print("1 ----------------- Runge–Kutta method")
    print("2 ----------------- Milan method")
    print("3 ----------------- Euler method")
    while True:
        try:
            choose_data_method = int(input())
            match (choose_data_method):
                case 1:
                    method = "runge–kutta"
                    break
                case 2:
                    method = "miln"
                    break
                case 3:
                    method = "euler"
                    break
                case _:
                    print("Enter your choice again!")
        except ValueError:
            print("Value has be integer! Try again from new line...")

    return f, f_result, initial_conditions, h, bounds, accuracy, method
