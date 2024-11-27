'''Find the First Non-Repeating Character
Problem: Write a function to find the first non-repeating character in a string.

Scenario: You need to identify the first character in a string that does not repeat.'''
s=input("")
for i in s:
    if s.count(i) == 1:
        print(i)
        break
