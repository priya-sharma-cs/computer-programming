'''Check if Two Strings are Rotations of Each Other
Problem: Write a function to check if one string is a rotation of another string.

Scenario: You are developing a circular queue system and need to check if one sequence is a rotated version of another'''
s=input("")
r=input("")
n=int(input(""))
b=len(s)
p=s[b-n::]+s[0:b-n:1]  
if p==r:
    print("True")
else:
    print("False")
