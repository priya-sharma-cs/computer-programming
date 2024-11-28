''' Count the number of even and odd numbers in a tuple.'''
def count_even_odd(tup):
    even_count = sum(1 for x in tup if x % 2 == 0)
    odd_count = len(tup) - even_count
    return even_count, odd_count

tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even, odd = count_even_odd(tup)
print("Even:", even)  # Output: Even: 4
print("Odd:", odd)
