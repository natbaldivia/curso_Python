# %%
file_size = 2500
extra_space = 0.15

# define a lambda function
calculate_total = lambda x:x * (1 + extra_space)

# call the lambda function
print(calculate_total(file_size))

# %%
file_size = 2500
extra_space = 0.15

# call a lambda function in one line
print((lambda x:x  * (1 + extra_space))(file_size))