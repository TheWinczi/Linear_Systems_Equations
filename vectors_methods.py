""" file storing data in vector. Can be used for
    generating vector and some operations on them """


from math import pow, sin, sqrt


def generate_vector(N, f):
    """ generate new matrix in defined way .
        @:return{vector} generated vector """
    vector = [0.0 for i in range(N)]
    for i in range(N):
        vector[i] = sin((i + 1) * (f + 1))
    return vector


def zeros(length):
    """ return vector with only zeros which length is N """
    return [0 for i in range(length)]


def norm(vector):
    """ return norm from vector """
    normy = 0
    try:
        if type(vector) == list:
            for i in range(len(vector)):
                normy += pow(vector[i], 2)
    except OverflowError:
        return -1

    return sqrt(normy)


def add_vectors(v1, v2):
    """ return vector which is sum of 2 vectors """
    result = [0 for i in range(len(v1))]
    for i in range(len(v1)):
        result[i] = v1[i] + v2[i]
    return result


def sub_vectors(v1, v2):
    """ return vector which is subtract of 2 vectors """
    result = [0 for i in range(len(v1))]
    for i in range(len(v1)):
        result[i] = v1[i] - v2[i]
    return result


def multiply_vector_by_matrix(vector, matrix):
    """ return vector which is sum of multiplying matrix by vector """
    result = []
    for i in range(len(matrix[0])):
        sum = 0
        for j in range(len(matrix)):
            sum += vector[i] * matrix[j][i]
        result.append(sum)
    return result


def multiply_vector_by_scalar(vector, scalar):
    """ return vector multiplyed by scalar """
    return [n*scalar for i, n in enumerate(vector)]
