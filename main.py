"""
    Program created for subject named
    "Metody Numeryczne" in April 2021

    created by Maciej Winczewski
    all rights reserved
"""

import constants as consts
import matrix_methods as mm
import vectors_methods as vm
import matplotlib.pyplot as plt
from time import time
from copy import deepcopy


# ------------
#    JACOBI
# ------------
def jacobi(a_matrix, b_vector, ended_norm):
    """ solve the system of equations Ax = b
        using iterative Jacobi method of the form:

        x{k+1}[i] = (b_vector[i] - (sum1 + sum2) / a_matrix[i][i]

        where:
            sum1 = sum_from_1_to_i-1(a_matrix[i][j]x{k}[j]
            sum2 = sum_from_i+1_to_N(a_matrix[i][j]x{k}[j]
    """

    n_size = len(b_vector)
    x_vector = [1.0 for i in range(n_size)]
    x_prev = [1.0 for i in range(n_size)]

    # variable for statistic
    iterations = 0
    start_time = time()

    # main calculating loop
    norm = 1
    while norm > ended_norm:
        for i in range(n_size):
            sums = 0
            for j in range(n_size):
                if i != j:
                    sums += (a_matrix[i][j] * x_prev[j])

            x_vector[i] = (b_vector[i] - sums) / a_matrix[i][i]

        for i in range(n_size):
            x_prev[i] = x_vector[i]
        iterations += 1
        res = vm.sub_vectors(mm.multiply_matrix_by_vector(a_matrix, x_vector), b_vector)
        norm = vm.norm(res)

        # if norm is more than variable can store break
        if norm == -1:
            print("! THE METHOD DOES NOT COINCIDE !")
            break

    return iterations, time() - start_time


# --------------
#  GAUSS-SEIDEL
# --------------
def gauss_seidel(a_matrix, b_vector, ended_norm):
    """ solve the system of equations Ax = b
        using iterative Gauss-Seidel method of the form:

        x{k+1}[i] = (b_vector[i] - (sum1 + sum2) / a_matrix[i][i]

        where:
            sum1 = sum_from_1_to_i-1(a_matrix[i][j]x{k+1}[j]
            sum2 = sum_from_i+1_to_N(a_matrix[i][j]x{k}[j]
    """

    n_size = len(b_vector)
    x_vector = [1.0 for i in range(n_size)]
    x_prev = [1.0 for i in range(n_size)]

    # variable for statistic
    iterations = 0
    start_time = time()

    # main calculating loop
    norm = 1
    while norm > ended_norm:
        for i in range(n_size):
            sums = 0
            for j in range(i):
                    sums += (a_matrix[i][j] * x_vector[j])
            for j in range(i+1, n_size):
                    sums += (a_matrix[i][j] * x_prev[j])

            x_vector[i] = (b_vector[i] - sums) / a_matrix[i][i]

        for i in range(n_size):
            x_prev[i] = x_vector[i]
        iterations += 1
        res = vm.sub_vectors(mm.multiply_matrix_by_vector(a_matrix, x_vector), b_vector)
        norm = vm.norm(res)

        # if norm is more than variable can store break
        if norm == -1:
            print("! THE METHOD DOES NOT COINCIDE !")
            break

    return iterations, time() - start_time


# ------------------
#  FACTORIZATION LU
# ------------------
def factorization_lu(a_matrix, b_vector):
    """ solve the system of equations Ax = b
        using factorization LU method """

    n_size = len(a_matrix)
    u_matrix = deepcopy(a_matrix)
    l_matrix = mm.ones(n_size)

    start_time = time()

    # calculate L and U matrices where L * U * x = b
    for i in range(n_size-1):
        for j in range(i+1, n_size):
            l_matrix[j][i] = u_matrix[j][i] / u_matrix[i][i]
            u_matrix[j][i:n_size] = vm.sub_vectors(u_matrix[j][i:n_size], vm.multiply_vector_by_scalar(u_matrix[i][i:n_size], l_matrix[j][i]))

    # calculate y vector using forward substitution where U * y = b
    y_vector = [1.0 for i in range(n_size)]
    for i in range(n_size):
        sum = 0.0
        for j in range(i):
            sum += l_matrix[i][j] * y_vector[j]
        y_vector[i] = (b_vector[i] - sum)

    # calculate x vector using back substitution where L * x = y
    x_vector = [1.0 for i in range(n_size)]
    for i in range(n_size-1, -1, -1):
        sum = 0.0
        for j in range(i+1, n_size):
            sum += u_matrix[i][j] * x_vector[j]
        x_vector[i] = (y_vector[i] - sum) / u_matrix[i][i]

    # calculate norm
    res = vm.sub_vectors(mm.multiply_matrix_by_vector(a_matrix, x_vector), b_vector)
    norm = float(vm.norm(res))

    return norm, time() - start_time


def create_diagram(x_data, y_data1, y_data2, y_data3, x_label, y_label, label1, label2, label3, title, output_file_name):
    """ create diagram using function argument """
    plt.figure()
    plt.plot(x_data, y_data1, 'b', label=label1)
    plt.plot(x_data, y_data2, 'y', label=label2)
    plt.plot(x_data, y_data3, 'g', label=label3)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.legend()
    plt.title(title)
    plt.savefig(output_file_name)
    plt.show()


def main():
    """ main function in program """

    # EXERCISE A
    a_matrix = mm.generate_matrix(consts.N_var, consts.a1_var, -1, -1)
    b_vector = vm.generate_vector(consts.N_var, consts.f_var)


    # EXERCISE B
    (jacobi_iter, jacobi_time) = jacobi(a_matrix, b_vector, pow(10, -9))
    print("Jacobi method summary:")
    print("jacobi iter =", jacobi_iter)
    print("jacobi time =", jacobi_time)
    print()

    (gauss_iter, gauss_time) = gauss_seidel(a_matrix, b_vector, pow(10, -9))
    print("Gauss method summary:")
    print("gauss iter =", gauss_iter)
    print("gauss time =", gauss_time)
    print()


    # EXERCISE C
    a_matrix = mm.generate_matrix(consts.N_var, 3, -1, -1)
    (jacobi_iter, jacobi_time) = jacobi(a_matrix, b_vector, pow(10, -9))
    print("Jacobi method summary:")
    print("jacobi iter =", jacobi_iter)
    print("jacobi time =", jacobi_time)
    print()

    (gauss_iter, gauss_time) = gauss_seidel(a_matrix, b_vector, pow(10, -9))
    print("Gauss method summary:")
    print("gauss iter =", gauss_iter)
    print("gauss time =", gauss_time)
    print()


    # EXERCISE D
    (lu_norm, lu_time) = factorization_lu(a_matrix, b_vector)
    print("Factorization LU method summary:")
    print("LU time: ", lu_time)
    print("LU norm: ", lu_norm)
    print()


    # EXERCISE E
    N = range(100, 2101, 500)
    gauss_time = [0 for i in range(len(N))]
    jacobi_time = [0 for i in range(len(N))]
    lu_time = [0 for i in range(len(N))]

    for i, n in enumerate(N):
        a_matrix = mm.generate_matrix(n, consts.a1_var, -1, -1)
        b_vector = vm.generate_vector(n, consts.f_var)

        (jacobi_iter, jacobi_time[i]) = jacobi(a_matrix, b_vector, pow(10, -9))
        (gauss_iter, gauss_time[i]) = gauss_seidel(a_matrix, b_vector, pow(10, -9))
        (lu_norm, lu_time[i]) = factorization_lu(a_matrix, b_vector)

    create_diagram(N,
                   jacobi_time,
                   gauss_time,
                   lu_time,
                   'rozmiar macierzy (n x n)',
                   'czas [s]',
                   'Jacobi',
                   'Gauss-Seidel',
                   'Faktoryzacja LU',
                   'wykres zaleznosci czasu od rozmiaru macierzy',
                   'porownanie_czasow.png')


# Let's do this!!
if __name__ == '__main__':
    main()
