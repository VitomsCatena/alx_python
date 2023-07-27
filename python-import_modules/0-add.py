import importlib

# Define the add function to be used in this file
def add(a, b):
    return a + b

# Define the variables a and b
a = 1
b = 2

# Import the add function from add_0.py using importlib
add_module = importlib.import_module('add_0')
add_func = getattr(add_module, 'add')

# Print the result using string formatting
result = add_func(a, b)
print(f"{a} + {b} = {result}")
