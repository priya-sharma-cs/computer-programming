'''Python program to count Even and Odd numbers in a List'''
list1 = list("Enter list")
 
even_count, odd_count = 0, 0
num = 0
 
# using while loop     
while(num < len(list1)):
     
    # checking condition
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
     
    # increment num 
    num += 1
     
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
