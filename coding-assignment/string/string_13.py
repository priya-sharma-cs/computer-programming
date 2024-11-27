'''
 Find the Longest Word in a String
Problem: Write a function to find the longest word in a given sentence.

Scenario: You need to highlight the longest word from a text document.'''
s=input("").split()
max=0
word=""
for i in s:
    if len(i) > max:
      max=len(i) 
      word=i
        
print(word)
print("index is :",s.index(i))
