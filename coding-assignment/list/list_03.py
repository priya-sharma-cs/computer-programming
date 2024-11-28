'''Swapping elements in a list is a common task in Python. We can easily shuffle and rearrange elements in a list. Python provides multiple ways to swap list elements.'''
a = [23, 65, 19, 90]

# Store element at index 1 (i.e., 65)
temp = a[1]

# Change element at index 1 to element at index 3 (i.e., 90)
a[1] = a[3]

# Change element at index 3 to temp (i.e., 65) 
a[3] = temp

print(a)
