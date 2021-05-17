""" file storing data in matrix. Can be used for
    generating matrix and some operations on them """

import copy


def generate_matrix(N, a1, a2, a3):
    """ generate new matrix in defined way.
        @:return{matrix} generated matrix """

    row = [0 for i in range(N)]
    matrix = [row.copy() for i in range(N)]

    # set a1 places
    for i in range(N):
        matrix[i][i] = a1

    # set a2 places
    for i in range(N - 1):
        matrix[i][i + 1] = a2
        matrix[i + 1][i] = a2

    # set a3 places
    for i in range(N - 2):
        matrix[i][i + 2] = a3
        matrix[i + 2][i] = a3

    return matrix


def diagonal(M):
    """ return diagonal for matrix """
    matrix = M.copy()

    diagonal = zeros(len(matrix))
    for i in range(len(matrix)):
        diagonal[i][i] = matrix[i][i]
    return diagonal


def lower_triangle(M):
    """ return bottom triangle in matrix """
    matrix = M.copy()

    lower = zeros(len(matrix))
    for i in range(len(matrix)):
        lower[i][:i] = matrix[i][:i].copy()
    return lower


def upper_triangle(M):
    """ return upper triangle in matrix """
    matrix = M.copy()

    upper = zeros(len(matrix))
    for i in range(len(matrix)):
        upper[i][i + 1:] = matrix[i][i + 1:]
    return upper


def zeros(n):
    """ return matrix NxN with only zeros """
    row = [0 for i in range(n)]
    return [row.copy() for i in range(n)]


def ones(n):
    """ return matrix NxN with ones in diagonal """
    matrix = []
    row = [0 for i in range(n)]
    for i in range(n):
        row[i] = 1
        matrix.append(row.copy())
        row[i] = 0
    return matrix


def multiply_matrices(M1, M2):
    """ multiply matrix_1 by matrix_2 and return as new matrix """
    if len(M1[0]) != len(M2):
        print("Bad matrix sizes to multiply!")
        return M1

    matrix = [[] for i in range(len(M2[0]))]

    for i in range(len(M1)):
        for j in range(len(M2[0])):
            number = 0
            for k in range(len(M1[0])):
                number += M1[i][k] * M2[k][j]
                matrix[i].append(number)

    return matrix


def multiply_matrix_by_scalar(matrix, scalar):
    """ return matrix multiplied by scalar """

    if scalar == 0:
        print("Multiplying by 0")
        return matrix

    tmp_matrix = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            tmp_matrix[i][j] *= scalar

    return tmp_matrix


def add_matrices(M1, M2):
    """ return matrix which is sum of M1 and M2 """

    if (len(M1) != len(M2)) or (len(M1[0]) != len(M2[0])):
        print("Cannot add matrix. Bad sizes")
        return M1

    tmp_matrix = copy.deepcopy(M1)
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            tmp_matrix[i][j] += M2[i][j]

    return tmp_matrix


def sub_matrices(M1, M2):
    """ return matrix which is sum of M1 and M2 """

    if (len(M1) != len(M2)) or (len(M1[0]) != len(M2[0])):
        print("Cannot add matrix. Bad sizes")
        return M1

    tmp_matrix = M1.copy()
    for i in range(len(M1)):
        for j in range(len(M1[0])):
            tmp_matrix[i][j] -= M2[i][j]

    return tmp_matrix


def transpose(matrix):
    """ return matrix transposition """
    tr_matrix = [[] for i in range(len(matrix[0]))]

    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            tr_matrix[j].append(row[j])

    return tr_matrix


def multiply_matrix_by_vector(matrix, vector):
    """ return vector which is result of multiplying matrix by vector """
    result = []

    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += vector[j] * matrix[i][j]
        result.append(sum)

    return result
