'''Find the product of all elements in a tuple.'''
def product_tuple(tup):
    product = 1
    for x in tup:
        product *= x
    return product

tup = (1, 2, 3, 4, 5)
result = product_tuple(tup)
print(result)
