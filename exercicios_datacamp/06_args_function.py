# %%
# define a function called concat
def concat(*args):
    """Concatenates multiple string arguments with spaces between them."""

    result = ""

    # iterate over the python args tuple
    for arg in args:
        result += " " + arg
    return result
    

# call the function
print(concat("Python","is","great!"))