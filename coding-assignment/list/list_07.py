'''Python program to select Random value from list of lists'''
from itertools import chain
import random
 
# Initializing list
test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]
 
# Printing original list
print("The original list is : " + str(test_list))
 
# choice() for random number, from_iterables for flattening
res = random.choice(list(chain.from_iterable(test_list)))
 
# Printing result
print("Random number from Matrix : " + str(res))
