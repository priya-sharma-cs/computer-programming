'''Remove Multiple Elements from List in Python'''
numbers = list("Enter list")

# Elements to remove
to_remove = [3, 5, 7]

# Removing elements
for item in to_remove:
    if item in numbers:
        numbers.remove(item)

# Output the modified list
print(numbers)
