'''. Remove Spaces from a String
Problem: Write a function to remove all spaces from a given string.

Scenario: You are processing user input and need to remove any spaces for validation purposes.'''
s= input("")
x=s.split()
a=""
for i in x:
    a+=i
print(a)
