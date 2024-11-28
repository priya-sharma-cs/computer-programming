'''The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.'''
N=int(input())
d={}
L=[]
for _ in range(N):
    name = input()
    score = float(input())
    d[name]=score
    L.append(score)
a=min(L)
c=L.count(a)
for i in range(c):
    L.remove(a)
b=min(L)
A=[]
for i in d:    
    if d[i]==b:
       A.append(i)
A.sort()
for k in A:
    print(k)
