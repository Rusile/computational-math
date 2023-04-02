from sympy import *
from scipy.misc import *
from findiff import *
import numpy as np
from simple_iteration_method import *



x, y = symbols('x y')
f = x ** 2 + x + 0.2 * y ** 2 - 0.3
g = x ** 2 + y - 5 * x * y - 0.7

f = 0.1 * x ** 2 + x + 0.2 * y ** 2 - 0.3
g = 0.2 * x ** 2 + y - 0.1 * x * y - 0.7

print(find_root_simple_iteration_double(f, g, 0, 0, 2, 2, 0.1))
