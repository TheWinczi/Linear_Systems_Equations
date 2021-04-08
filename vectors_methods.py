""" file storing data in vector. Can be used for
    generating vector and some operations on them """


from math import pow
from math import sin
from math import sqrt


def generate_vector(N, f):
    """ generate new matrix in defined way .
        @:return{vector} generated vector """
    vector = [0.0 for i in range(N)]

    for i in range(N):
        vector[i] = sin((i + 1) * (f + 1))

    return vector


def norm(vector):
    """ return norm from vector """
    normy = 0
    if type(vector) == list:
        for i in range(len(vector)):
            normy += pow(vector[i], 2)

    return sqrt(normy)
