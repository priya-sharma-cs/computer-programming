'''Find the second largest element in a tuple.'''
def second_largest(tup):
    sorted_tup = sorted(tup)
    return sorted_tup[-2]

tup = (10, 5, 8, 20, 15)
second_largest_element = second_largest(tup)
print(second_largest_element)
