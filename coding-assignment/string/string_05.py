#Write a Python program to find the second most frequent character in a string.
def second_most_frequent_char(input_string):
 char_count = {}
 for char in input_string:
    char_count[char] = char_count.get(char, 0) + 1
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_char_count[1][0] if len(sorted_char_count)
