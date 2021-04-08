index = 183211

first_index_digit = (index // 10000) % 10
second_index_digit = (index // 1000) % 10
third_index_digit = (index // 100) % 10
fourth_index_digit = (index // 10) % 10
fifth_index_digit = index % 10

last_index_digit = fifth_index_digit
e_var = fourth_index_digit
f_var = third_index_digit

N_var = 9 * fifth_index_digit * fourth_index_digit
