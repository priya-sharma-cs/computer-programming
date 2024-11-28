'''Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
Sample Dictionary'''
# Create an empty dictionary 'd' to store the squares of numbers.
d = dict()

# Iterate through numbers from 1 to 15 (inclusive).
for x in range(1, 16):
    # Calculate the square of each number and store it in the dictionary 'd' with the number as the key.
    d[x] = x ** 2

# Print the dictionary 'd' containing the squares of numbers from 1 to 15.
print(d)
