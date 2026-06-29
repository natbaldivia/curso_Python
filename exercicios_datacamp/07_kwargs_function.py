# %%
# define a function called concat
def concat(**kwargs):
    """Concatenates multiple string arguments with spaces between them."""

    result = ""

    # iterate over the python args tuple
    for kwarg in kwargs.values():
        result += " " + kwarg
    return result
    

# call the function
print(concat(start="Python",middle="is",end="great!"))