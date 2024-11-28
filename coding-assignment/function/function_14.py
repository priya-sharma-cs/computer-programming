'''Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.'''
# Take user input and split it into a list based on the hyphen ("-") separator, creating a list named 'items'
items = [n for n in input().split('-')]

# Sort the elements in the 'items' list in lexicographical order (alphabetical and numerical sorting)
items.sort()

# Join the sorted elements in the 'items' list using the hyphen ("-") separator and print the resulting string
print('-'.join(items)) 
