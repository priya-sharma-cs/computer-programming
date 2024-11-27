'''Count Frequency of Each Character
Problem: Write a function to count the frequency of each character in a string.

Scenario: You are analyzing text data and need to find the frequency of individual characters.'''
s=input("")
d={}
for i in s:
    if i not in d:
      d[i]=s.count(i)
print(d)
