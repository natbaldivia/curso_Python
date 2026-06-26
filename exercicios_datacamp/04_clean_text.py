# %%
# Working with functions, chapter 2 of 
#Intermediate Python for Developers

text = """Practical Examples:
Through exercices, you applied these concepts by creating functions for various tasks, such as cleaning text data by replacing spaces with underscores and converting characters to lowercase."""

def clean_string(text):
    no_spaces = text.replace(" ","_")
    clean_text = no_spaces.lower()
    return clean_text

print(clean_string(text))

# %%
product = "Wireless Mouse"

# Define clean_text function
def clean_text(text,lower=True):
    clean_text = text.replace(' ','_')
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()

# Test with default behavior
print(clean_text(product))