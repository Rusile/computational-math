from input import read_from_stdin
from input import read_from_file
from gauss_calculation import count_matrix_det_by_gauss, count_result, print_matrix
from gauss_calculation import count_matrix_det
from gauss_calculation import count_residual_vector
from gauss_calculation import validate_matrix
from gauss_calculation import print_matrix
from gauss_calculation import triangulize_matrix
from gauss_calculation import count_matrix_det_by_gauss
import numpy as np

response = input("Read data from file? (y/n)")
matrix = []

if (response == "n"):
    matrix = read_from_stdin()
elif (response == "y"):
    filename = input("Enter filepath: ")
    matrix = read_from_file(filename)

validate_matrix(matrix)

det = count_matrix_det([line[:-1] for line in matrix])
print(f"Matrix det:{round(det, 3)}")

triangle_matrix = triangulize_matrix(matrix.copy())
print(f"Triangle matrix:")
print_matrix("triangle matrix", [[round(value, 3) for value in line] for line in triangle_matrix])

solution = count_result(matrix.copy())
print(f"Matrix solution:{solution}")
# print(f"Numpy mattix solution:{np.linalg.solve([line[:-1] for line in matrix], [line[len(line) - 1] for line in matrix])}")

residual_vector = count_residual_vector(matrix, solution)
print(f"Residual vector:{[round(value, 6) for value in residual_vector]}")
