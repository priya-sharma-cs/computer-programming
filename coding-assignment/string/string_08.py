#Write a Python program to count the number of occurrences of a specific substring in a string.
def count_substring_occurrences(input_string, substring):
count = 0
index = 0
while True:
    index = input_string.find(substring, index)
    if index == -1:
        break
    count += 1
    index += 1
return count
