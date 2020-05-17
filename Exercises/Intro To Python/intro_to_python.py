#   Course: CS 2302
#   Assignment: Intro to Python
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 01/27/2020
#   Purpose of the Program: to practice and get familiar with python

import numpy as np

'''   Integers exercises   '''

def divisible(a,b):
    if a % b == 0:
        return True
    else:
        return False

def prime(n):
    for i in range(2,n):
        if n % i == 0:      # If there is another number that can divide 
            return False    # n, then it not a prime number.
    return True

def sum_digits(n):
    if n < 10:
        return n
    rest = n // 10   # It eliminates the last digit of a number.
    remainder = n % 10   # It gets the last digit of a number.
    return remainder + sum_digits(rest)  # It sums the last digit and returns the rest.

'''   Strings exercises   '''

def reverse(s):
    str = ''
    for char in s:
        str = char + str   # Create a string that puts the current character 
    return str             # at the beginning, thus reversing it 

def remove_vowels(s):
    vowels = ('A','E','I','O','U','a','e','i','o','u')
    for char in s:
        if char in vowels:  # If the actual character is a vowel, 
            s = s.replace(char,"")  # then replace it with an empty character.
    return s

def pal(s):
    s = s.lower()
    str = ''.join(reversed(s))   # Method to reverse a string.
    if str == s:   # If the original and the reverse string are the same,
        return True   # then it means that it is a palindrome.
    return False

'''   1D Array exercises   '''

def max_array(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max
    
def find(A,x):
    for i in range(len(A)):
        if A[i] == x:   # If the current element is equal to the key,
            return i   # then return its index.
    return -1   # Else, return -1. Meaning that the key was not found.

def sum_array(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i]
    return sum

def replace_array(A,x,y):
    B = A.copy()    # This method copies and assigns each element of the array to B
    for i in range(len(B)):
        if B[i] == x:   # If the current element is equal to X, 
            B[i] = y   # then replace the element with the value of Y.
    return B

'''   2D Array   '''

def is_square(A):
    dimensions = np.shape(A)    # This method returns the dimensions of the array.
    if dimensions[0] == dimensions[1]:  # If the row and column are the same length,
        return True             # then it means that it is a square.
    return False

def diagonal_sum(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i][i]
    return sum

def sec_diagonal_sum(A):
    sum = 0
    for i in range(len(A)):
        sum += A[i][len(A)-1-i]
    return sum

def diagonal(A):
    return A.diagonal() # This method returns a 1D array containg the main diagonal.

def sec_diagonal(A):    # This method flips the rows in the left to right direction.
    return np.diag(np.fliplr(A))    # After that, it returns a 1D array containing the sec diag.

def swap_rows(A,i,j):
    B = A.copy()
    temp = B[i].copy()  # We copy and store the values of the ith row in a temporary variable.
    B[i] = B[j]   # We assign the values of row j to row i.
    B[j] = temp   # We assign the values of temp to row j
    return B
    
def swap_columns(A,i,j):
    B = A.copy()
    temp = B[:,[i]].copy()  # We copy and store the values of the ith column in a temporary variable.
    B[:,[i]] = B[:,[j]] # We assign the values of column jth to column i.
    B[:,[j]] = temp     # We assign the values of temp to column j
    return B

def replace_max_array(A,x):
    B = A.copy()
    max = B[0][0]
    row = 0
    col = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            if B[i][j] > max:
                max = B[i][j]
                row = i   # We store the row location of the current max.
                col = j   # We store the column location of the current max.
    B[row][col] = x   # We replace the max value with the value of x.
    return B

'''   Lists   '''

def greater_than_list(L,x):
    greater_list = []
    for i in range(len(L)):
        if L[i] > x:    # If the current element is bigger than x, 
            greater_list.append(L[i])   # then append that value to greater_list.
    return greater_list
 
def split(L):
    even_index_list = []
    odd_index_list = []
    for i in range(len(L)):
        if i % 2 == 0:  # If i is an even number 
            even_index_list.append(L[i])   # then append that value to the even list.
        else:
            odd_index_list.append(L[i])   # Else, append the odd value into the odd list.
    return even_index_list, odd_index_list

def merge(L1, L2):
    L1.extend(L2)   # We add and append the values of L2 into L1
    merge_list = L1    
    for i in range(0, len(merge_list)-1):
        for j in range(i+1, len(merge_list)):
            if merge_list[i] > merge_list[j]:   # If the i element is bigger
                temp = merge_list[i]            # than j element, then swap.
                merge_list[i] = merge_list[j]
                merge_list[j] = temp
    return merge_list

def split_pivot(L):
    pivot = L[0]
    min_values = []
    big_values = []
    for i in range(len(L)):
        if L[i] < pivot:    # If the current element is less than the pivot 
            min_values.append(L[i]) # then append it to min_values.
        else:
            big_values.append(L[i]) # Else, append it to max_values.
    return min_values, big_values