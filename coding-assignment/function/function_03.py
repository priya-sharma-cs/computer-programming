'''Write a Python function to multiply all the numbers in a list.'''
# Define a function named 'multiply' that takes a list of numbers as input
def multiply(numbers):
    # Initialize a variable 'total' to store the multiplication result, starting at 1
    total = 1
    
    # Iterate through each element 'x' in the 'numbers' list
    for x in numbers:
        # Multiply the current element 'x' with the 'total'
        total *= x
    
    # Return the final multiplication result stored in the 'total' variable
    return total

# Print the result of calling the 'multiply' function with a tuple of numbers (8, 2, 3, -1, 7)
print(multiply((8, 2, 3, -1, 7))) 
