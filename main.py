"""
    Program created for subject named
    "Metody Numeryczne" in April 2021

    created by Maciej Winczewski
    all rights reserved
"""

import matrix
import vector


def main():
    """ main function in program """
    a_matrix = matrix.Matrix(183211)

    for row in a_matrix.generate_matrix(5+2, -1, 2):
        print(row)

    b_vector = vector.Vector(183211)
    print(b_vector.generate_vector(3))

    for row in a_matrix.diag():
        print(row)

    print()

    for row in a_matrix.get_l():
        print(row)

    print()

    for row in a_matrix.get_u():
        print(row)

    print(b_vector.get_norm())


if __name__ == '__main__':
    main()
