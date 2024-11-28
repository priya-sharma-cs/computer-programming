'''Check if a tuple is a subset of another tuple.'''
def is_subset(sub, main):
    return all(x in main for x in sub)

main_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sub_tuple = (2, 4, 6)
result = is_subset(sub_tuple, main_tuple)
print(result)  # Output: True
