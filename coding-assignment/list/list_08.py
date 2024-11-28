'''Given a list, the task is to sort the list according to the column using the lambda approach'''
def sortarray(array):
     
    for i in range(len(array[0])):
         
        # sorting array in ascending 
        # order specific to column i,
        # here i is the column index
        sortedcolumn = sorted(array, key = lambda x:x[i])
         
        # After sorting array Column 1
        print("Sorted array specific to column {}, \
        {}".format(i, sortedcolumn))
     
# Driver code 
if __name__ == '__main__': 
     
    # array of size 3 X 2 
    array = [['java', 1995], ['c++', 1983],
             ['python', 1989]]
     
    # passing array in sortarray function
    sortarray(array)
