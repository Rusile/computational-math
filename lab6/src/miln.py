from runge_kutta import runge_kutta_differentiation
from math import ceil
import numpy as np
import pandas as pd

def miln_differentiation(f, initial_conditions, h, bounds, accuracy):
    # print("_____________________ MILAN _____________________________")
    n = ceil((bounds[1] - bounds[0]) / h) + 1 # здесь добавляется 1, чтобы количество точек было правильным (у k интервалов k+1 конец)
    if (n < 4):
        # print("For Milan differentiation num of intervals has to be at least 4!")
        # print(f"h = {h}, on  ({bounds[0]}, {bounds[1]}), n = ceil((bounds[1] - bounds[0])/ h) + 1 = {n}")
        exit(0)

    # для этих иксов нужно предсказать значение y
    x = [bounds[0] + h*i for i in range(n)]
    # y = [0]*(n)
    y = []


    # Вычисляем первые 4 значения y
    runge_result, runge_x, hes = runge_kutta_differentiation(f, initial_conditions, h, [x[0], x[3]], accuracy)
    y = runge_result[:4]

    # print(f"predict\t\t\tcorrect\t\t\tdiff\t\taccuracy")
    for i in range(4, n):
        y_prediction = prediction(h, f, x, y, i)
        y_correction = correction(h, f, x, y, i, y_prediction)
        # print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")

        while abs(y_correction - y_prediction) > accuracy:
            y_prediction = y_correction
            y_correction = correction(h, f, x, y, i, y_prediction)
            print(y_correction)

            # print(f"{round(y_prediction, 6)}\t\t{round(y_correction, 6)}\t\t{round(abs(y_correction - y_prediction), 3)}\t\t{accuracy}")
        y.append(y_correction)
    # print("_____________________ MILAN END _____________________________")
    return y, x

def prediction(h, f, x, y, i):
    tmp = 2*f(x[i-3], y[i-3]) - f(x[i-2], y[i-2]) + 2*f(x[i-1], y[i-1])
    return y[i-4] + 4*h*tmp/3

def correction(h, f, x, y, i, y_pred):
    tmp = f(x[i-2], y[i-2]) + 4*f(x[i-1], y[i-1]) + f(x[i], y_pred)
    return y[i-2] + h*tmp/3