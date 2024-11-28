'''Remove empty tuples from a list – Python'''
a = list("Enter list with Empty Tuple")
res = []

# Iterate over the list 'a'
for t in a:
  
    # If tuple is not empty then add it to res.
    if t:
        res.append(t)

print(res)
