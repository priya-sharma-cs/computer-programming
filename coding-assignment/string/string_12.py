'''Check if Two Strings are Anagrams
Problem: Write a function to check if two strings are anagrams (i.e., they contain the same characters in different order).

Scenario: You are working on a text processing tool and need to check if two words are anagrams.'''
s1=input("")
s2=input("")
c=0
if len(s1)==len(s2):
    for i in s1:
       if i in s2:
         c+=1
       else:
          continue
if c==l(s2):
    print("anangram")
else:
    print("not")




