

class Matrix(object):
    """ class storing data in matrix. Can be used for
        generating matrix and some operations on they """

    def __init__(self, index):
        """ initialize the matrix """
        self.__student_index = index
        self.__matrix = []

        last_index_digit = self.__student_index % 10
        penultimate_index_digit = (self.__student_index // 10) % 10
        self.__N = 9 * last_index_digit * penultimate_index_digit

        row = [0 for i in range(self.__N)]
        self.__matrix = [row.copy() for i in range(self.__N)]


    def generate_matrix(self, a1, a2, a3):
        """ generate new matrix in defined way .
            @:param{index} student index
            @:return{matrix} generated matrix """

        # set a1 places
        for i in range(self.__N):
            self.__matrix[i][i] = a1

        # set a2 places
        for i in range(self.__N-1):
            self.__matrix[i][i+1] = a2
            self.__matrix[i+1][i] = a2

        # set a3 places
        for i in range(self.__N-2):
            self.__matrix[i][i+2] = a3
            self.__matrix[i+2][i] = a3

        return self.__matrix


    def get_n(self):
        return self.__N

    def get_matrix(self):
        return self.__matrix

    def get_student_index(self):
        return self.__student_index

    def diag(self):
        diagonal = self.zeros(self.__N)
        for i in range(self.__N):
            diagonal[i][i] = self.__matrix[i][i]

        return diagonal

    def get_l(self):
        l = self.zeros(self.__N)
        for i in range(self.__N):
            l[i][i+1:] = self.__matrix[i][i+1:]

        return l


    def get_u(self):
        u = self.zeros(self.__N)
        for i in range(self.__N):
            u[i][:i] = self.__matrix[i][:i]

        return u

    def zeros(self, n):
        row = [0 for i in range(n)]
        return [row.copy() for i in range(n)]
