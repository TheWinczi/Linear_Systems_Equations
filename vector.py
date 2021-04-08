from math import sin
from math import sqrt
from math import pow


class Vector(object):
    """ class storing data in vector. Can be used for
        generating vector and some operations on them """

    def __init__(self, index):
        """ initialize the matrix """
        self.__student_index = index
        self.__f = 0

        last_index_digit = self.__student_index % 10
        penultimate_index_digit = (self.__student_index // 10) % 10
        self.__N = 9 * last_index_digit * penultimate_index_digit

        self.__vector = [0.0 for i in range(self.__N)]


    def generate_vector(self, f):
        """ generate new matrix in defined way .
            @:return{vector} generated vector """

        for i in range(self.__N):
            self.__vector[i] = sin((i+1) * (f + 1))

        return self.__vector


    def get_norm(self):

        norm = 0
        for i in range(self.__N):
            norm += pow(self.__vector[i], 2)

        return sqrt(norm)