'''Split a tuple into equal parts.'''
def split_tuple(tup, n):
    avg = len(tup) // n
    split_result = [tup[i:i+avg] for i in range(0, len(tup), avg)]
    return tuple(split_result)

tup = (1, 2, 3, 4, 5, 6)
n = 2
result = split_tuple(tup, n)
print(result) 
