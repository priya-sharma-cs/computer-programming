'''We are given a string and we need to reverse words of a given string'''


string = "geeks quiz practice code"
s = string.split()[::-1]
l = []
for i in s:
	l.append(i)
print(" ".join(l))
