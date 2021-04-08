

class Database(object):
    """ Database class storing all needed data """

    def __init__(self, index):
        """ initialize the object """

        self.__index = index

        self.first_index_digit = (index // 10000) % 10
        self.second_index_digit = (index // 1000) % 10
        self.third_index_digit = (index // 100) % 10
        self.fourth_index_digit = (index // 10) % 10
        self.fifth_index_digit = index % 10

        self.N_var = 9 * self.fifth_index_digit * self.fourth_index_digit


    def get_last_index_digit(self):
        return self.fifth_index_digit

    def get_e_var(self):
        return self.fourth_index_digit

    def get_f_var(self):
        return self.third_index_digit
