import numpy as np
import matplotlib.pyplot as plt

from input_data import read_equation_console
from input_data import read_interval_console
from input_data import read_epsilon_console
from input_data import read_method
from input_data import get_system
from input_data import read_system_console

from newton_method import find_root_newton
from simple_iteration_method import find_root_simple_iteration
from simple_iteration_method import find_root_simple_iteration_double
from half_div_method import half_div

import sympy as sp

is_system = get_system()

f, g = read_system_console() if is_system else None

eq = read_equation_console() if not is_system else None

start_x, stop_x = read_interval_console('x')
if is_system:
    start_y, stop_y = read_interval_console('y')
epsilon = read_epsilon_console()

match read_method():
    case 1:
        root = find_root_newton(eq, start_x, stop_x, epsilon)
        if root == None: print("Invalide interval and equation for Newton calculation method")
    case 2:
        root = half_div(eq, start_x, stop_x, epsilon)
        if root == None: print("Invalide interval and equation for scant calculation method")
    case 3:
        root = find_root_simple_iteration(eq, start_x, stop_x, epsilon)
        if root == None: print("Invalide interval and equation for simple iteration calculation method")
    case 4:
        root_x, root_y, count = find_root_simple_iteration_double(f, g, start_x, start_y, stop_x, stop_y, epsilon)

        if root_x == None or root_y == None: print("Invalide interval and equation for simple iteration calculation method")
        root = None
    case _:
        print("Error with choosing method!")

if root != None:
    print(f"root={root} in [{start_x}, {stop_x}]")
    plt.plot([i for i in np.arange(start_x, stop_x, 0.01)], [eq(i) for i in np.arange(start_x, stop_x, 0.01)])
    plt.plot(root, eq(root), 'o')
    plt.title(f"Root in [{start_x},{stop_x}]")
    plt.show()
elif root_x != None and root_y != None:
    f = sp.lambdify(sp.symbols('x y'), f, 'numpy')
    g = sp.lambdify(sp.symbols('x y'), g, 'numpy')

    root_z = f(root_x, root_y)

    # Print the root and its range
    print(f"Iterations count = {count} \nRoot=({root_x}, {root_y}) in [{start_x}, {stop_x}] x [{start_y}, {stop_y}]")

    # Generate the x and y values
    x = np.linspace(start_x, stop_x, 100)
    y = np.linspace(start_y, stop_y, 100)
    X, Y = np.meshgrid(x, y)

    # Calculate the Z values for the functions
    Z1 = f(X, Y)
    Z2 = g(X, Y)

    # Plot the functions and the root
    fig = plt.figure(figsize=(12, 5))

    # Plot for the first function
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    ax1.plot_surface(X, Y, Z1, cmap='jet', alpha=0.8)
    ax1.scatter(root_x, root_y, root_z, s=50, c='red', label='root')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('z')
    ax1.set_title('x^2 + y^2')

    # Plot for the second function
    ax1.plot_surface(X, Y, Z2, cmap='jet', alpha=0.8)

    # Add a common title and legend
    fig.legend()

    # Show the plot
    plt.show()

exit(0)
