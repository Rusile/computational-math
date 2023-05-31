from get_data import get_data
from lab6.src.euler import modified_euler_method
from plot import plot_result
from runge_kutta import runge_kutta_differentiation
from miln import miln_differentiation
from math import exp

def main():
    f, f_result, initial_conditions, h, bounds, accuracy, method = get_data()

    result_miln, x = miln_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_runge_kutta, x, hes = runge_kutta_differentiation(f, initial_conditions, h, bounds, accuracy)
    result_euler, x = modified_euler_method(f, initial_conditions, h, bounds)
    # print("=============results=============")
    # print(f"x\t\tmiln\t\trunge\t\trunge h\t\treal\t\t")
    # for i in range(len(x)):
    #     print(f"{round(x[i], 3)}\t\t{round(result_miln[i], 4)}\t\t{round(result_runge_kutta[i], 5)}\t\t{round(hes[i], 5)}\t\t {round(f_result(i), 5)}")
    match (method):
        case "runge-kutta":
            plot_result([round(f_result(i), 4) for i in x], x, result_runge_kutta, method)
        case "miln":
            plot_result([round(f_result(i), 4) for i in x], x, result_miln, method)
        case "euler":
            plot_result([round(f_result(i), 4) for i in x], x, result_euler, method)
        case _:
            print("Error in getting data from user!")
main()