#Write a Python program to find the common characters between two strings.
def common_characters(str1, str2):
  return "".join(char for char in set(str1) if char in str2)
