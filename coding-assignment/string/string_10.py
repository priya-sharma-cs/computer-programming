'''Count Vowels in a String
Problem: Write a function to count the number of vowels in a string.

Scenario: You are tasked with calculating how many vowels appear in a given sentence.'''
problem 3
s= input("")
c=0
for i in s:
    if i in ["a","e","i","o","u"]:
       c+=1
print(c)
