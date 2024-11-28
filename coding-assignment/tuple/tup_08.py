'''Convert a tuple of integers to a tuple of strings.'''
def int_to_str_tuple(tup):
    return tuple(str(x) for x in tup)

tup = (1, 2, 3, 4, 5)
str_tup = int_to_str_tuple(tup)
print(str_tup)
