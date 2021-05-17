index = 183211

first_ix_dig = (index // 10000) % 10
second_ix_dig = (index // 1000) % 10
third_ix_dig = (index // 100) % 10
fourth_ix_dig = (index // 10) % 10
fifth_ix_dig = index % 10

last_ix_dig = fifth_ix_dig
penultimate_ix_dig = fourth_ix_dig
e_var = fourth_ix_dig
f_var = third_ix_dig
a1_var = 5 + e_var

N_var = 911
