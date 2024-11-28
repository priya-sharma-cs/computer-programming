'''Merge two tuples and remove duplicates.'''
def merge_and_remove_duplicates(tup1, tup2):
    return tuple(set(tup1).union(tup2))

tup1 = (1, 2, 3)
tup2 = (3, 4, 5)
result = merge_and_remove_duplicates(tup1, tup2)
print(result) 
