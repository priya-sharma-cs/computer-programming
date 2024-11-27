'''Compress a String Using the Counts of Repeated Characters
Problem: Write a function to compress a string by replacing consecutive repeated characters with the character followed by the count.

Scenario: You are implementing a data compression algorithm.'''
s=input('')
r=""
for i in s :
    b=s.count(i)
    if i not in r:
        r+=i+str(b)
print(r)
