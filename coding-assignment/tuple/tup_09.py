'''Find the first and last elements of a tuple.'''
def first_last_elements(tup):
    return tup[0], tup[-1]

tup = (10, 20, 30, 40, 50)
first, last = first_last_elements(tup)
print("First:", first)  # Output: First: 10
print("Last:", last)  
