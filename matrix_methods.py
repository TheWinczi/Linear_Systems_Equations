""" file storing data in matrix. Can be used for
    generating matrix and some operations on them """


def generate_matrix(N, a1, a2, a3):
    """ generate new matrix in defined way .
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


def diag(matrix):
    """ return diagonal for matrix """
    diagonal = zeros(len(matrix))
    for i in range(len(matrix)):
        diagonal[i][i] = matrix[i][i]
    return diagonal


def get_l(matrix):
    l = zeros(len(matrix))
    for i in range(len(matrix)):
        l[i][i + 1:] = matrix[i][i + 1:]
    return l


def get_u(matrix):
    u = zeros(len(matrix))
    for i in range(len(matrix)):
        u[i][:i] = matrix[i][:i]
    return u


def zeros(n):
    row = [0 for i in range(n)]
    return [row.copy() for i in range(n)]
