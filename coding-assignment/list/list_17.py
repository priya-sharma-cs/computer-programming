'''Convert List of Lists to Dictionary – Python'''
# a = [['a', 1], ['b', 2], ['c', 3]]
a=eval("Enter nested list")
# Initialize an empty dictionary
d = {}

# Loop through list and add key-value pairs into 'd'
for sublist in a:
    d[sublist[0]] = sublist[1]

print(d)
