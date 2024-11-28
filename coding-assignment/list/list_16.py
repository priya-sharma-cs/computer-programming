'''Reverse Row sort in Lists of List we need to perform the sorting of rows of the matrix in descending order. This kind of problem has its application in the web development and Data Science domain'''
#test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
test_list=list("input nested list")
 
# printing original list
print("The original list is : " + str(test_list))
 
# Reverse Row sort in Lists of List
# using loop
for ele in test_list:
    ele.sort(reverse=True)
 
# printing result
print("The reverse sorted Matrix is : " + str(test_list))
