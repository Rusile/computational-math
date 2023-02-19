import re
import sys

from numpy import multiply

# TODO:clean up prints

def validate_matrix(matrix):

    if(matrix == []):
        print("Error: Input data is empty")
        sys.exit(1)
    n = len(matrix)

    for line in matrix:
        if len(line) - 1 != n:
            print("Error: Invalide amount of numbers in lines")
            sys.exit(1)
    return n

def print_matrix(label, matrix):
    print(f"________{label}________")
    for line in matrix:
            print(line)
    print("________________________\n")


def swap_lines(matrix, i):
    for j in range(i + 1, len(matrix)):
        if(matrix[j][i] != 0):
            # print_matrix(f"matrix before swap line i={i} and line j={j}", matrix)
            matrix[j], matrix[i] = matrix[i], matrix[j]
            # print_matrix(f"matrix after swap line i={i} and line j={j}", matrix)
            return matrix
    print_matrix("Warning: System has no unique solution!", matrix)
    sys.exit(0)

def triangulize_matrix(matrix):
    n = len(matrix)
    for i in range(0, n):

        if(matrix[i][i] == 0):
            matrix = swap_lines(matrix, i)

        i_i = matrix[i][i]
        for j_in_i_line in range(i, n + 1):
            matrix[i][j_in_i_line] = matrix[i][j_in_i_line]/i_i

        for j_after_i in range(i + 1, n):
            j_line_head = matrix[j_after_i][i]
            for k in range(i, n + 1):
                matrix[j_after_i][k] = matrix[j_after_i][k] - j_line_head*matrix[i][k]
    return matrix


def count_result(matrix):
    n = len(matrix)
    matrix = triangulize_matrix(matrix)

    for i in range(1, n):
        for j_before_i in range(0, i):
            i_head = matrix[j_before_i][i]
            for k in range(i, n + 1):
                matrix[j_before_i][k] = matrix[j_before_i][k] - matrix[i][k]*i_head

    return [round(matrix[i][n], 3) for i in range(0, len(matrix))]


def count_matrix_det(matrix):
    det = 0
    for i in range(len(matrix[0])):
        if(len(matrix) > 1):
            minor = [line[:i] + line[(i + 1):] for line in matrix[1:]]
            det += (-1)**(i)*matrix[0][i]*count_matrix_det(minor)
        elif (len(matrix) == 1):
            return matrix[0][0]
        else:
            print("Error: can't count det of matrix with dim less then 1.")
    return det

def count_residual_vector(matrix, solution):
    return [sum([solution[i]*line[i]  for i in range(len(line) - 1)]) - line[-1] for line in matrix]

