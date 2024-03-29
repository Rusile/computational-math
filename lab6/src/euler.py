def modified_euler_method(f, initial_conditions, h, x_range):

    x0, xn = x_range[0], x_range[1]
    n = int((xn - x0) / h) + 1
    y = [initial_conditions]

    for i in range(1, n):
        xi = x0 + i * h
        yi = y[i-1] + (h/2) * (f(xi-h, y[i-1]) + f(xi, y[i-1]+h*f(xi-h, y[i-1])))
        y.append(yi)

    return y, [x_range[0] + h*i for i in range(n)]