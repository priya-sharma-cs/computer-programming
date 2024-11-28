'''Find the difference between two tuples.'''
def tuple_difference(tup1, tup2):
    return tuple(x for x in tup1 if x not in tup2)

tup1 = (1, 2, 3, 4, 5)
tup2 = (3, 4, 5, 6)
difference = tuple_difference(tup1, tup2)
print(difference)  # Output: (1, 2)
