#   Course: CS 2302
#   Assignment: Exercise 2 - Recursion
#   Author: Oswaldo Escobedo
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 01/31/2020
#   Purpose of the Program: to practice and 
#   use recursion solve the problems

import math

def sum_list(L):
    if len(L) == 0: #Base case, L is empty
        return 0
    else:
        return L[0] + sum_list(L[1:])
    
def is_in_list(A,a):
    if len(A) < 1:  # Edge case, A is empty
        return False
    if A[0] == a:   # Base case, a was in the list
        return True
    return is_in_list(A[1:],a)  # Creates a new list without the first element.
    
def smallest(L):
    if len(L) == 1:   # Base case, L had only one element
        return L[0]
    return min(L[0],smallest(L[1:])) 
        
def binary(n):
    if n == 0:   # Base case, n is zero.
        return ''
    rest = n // 2
    remainder = n % 2
    return binary(rest) + str(remainder) 
    
def identical(L1,L2):
    if (len(L1) == 1 and len(L2) == 1) and (L1[0] == L2[0]):    # Base case, the lists are identical
        return True
    if len(L1) != len(L2):  # Determines if the length of the lists are different.
        return False
    if L1[0] != L2[0]: # Determines if the current elements are different
        return False
    return identical(L1[1:],L2[1:]) # Slices both lists.
    
def reverse(L):
    if len(L) == 0: # Base case, L is empty
        return []
    return reverse(L[1:]) + [L[0]] # First element becomes last element.

def reverse_in_place(L,first,last):
    if first >= last:   # Base case, first and last have crossed.
        return
    temp = L[first]
    L[first] = L[last] # Swaps the first and last element.
    L[last] = temp
    return reverse_in_place(L,first+1,last-1) # First and last value changes to keep swaping the list.
                
def is_sorted(L):
    if len(L) == 0 or len(L) == 1:  # Base case, L is empty
        return True
    return L[0] < L[1] and is_sorted(L[1:]) # Condition to check if the list is in ascending order.

def print_binary(string_so_far,digits_left):
    if digits_left < 0:   # Edge case, digits_left has an negative index.
        return ''
    if digits_left == 0:    # Base case, digits_left is empty
        print(string_so_far)
    print_binary(string_so_far + '0',digits_left-1) # Recursive calls to create
    print_binary(string_so_far + '1',digits_left-1) # binary strings.

def permutations(word_so_far, chars_left):
  if len(chars_left) == 0:  # Base case, chars_left is empty.
    print(word_so_far)
  for char in chars_left:
    prev_word = chars_left.replace(char,'') # Removes the first char in the string.
    new_word = word_so_far + char # Creates a new string with the first char in the string.
    permutations(new_word,prev_word) 
        
def meals(choice_so_far,starter,main,desert):
    if len(choice_so_far) == 3:   # Base case
        print(choice_so_far)
    for i in starter:
        for j in main:
            for k in desert:    # Recursive call to create a new meal with the current elements in i,j,k.
                meals(choice_so_far + [i] + [j] + [k],starter[1:],main[1:],desert[1:]) # Slices the lists.

if __name__ == "__main__":  
    L = [4,1,7,9,3,0,6,5,2,8]
    print(L)

    print(sum_list(L))
    print(sum_list(L[2:6]))
    
    print(is_in_list(L,3))
    print(is_in_list(L,13))
    
    print(smallest(L))
    print(smallest(L[:5]))
    
    print(binary(8))
    print(binary(15))
    
    print(identical([2,4,5],[2,4,5,7]))
    print(identical([2,4,5],[2,4,6]))
    print(identical([2,3,5],[2,5,5]))
    print(identical([2,4,5],[2,4,5]))
    
    print(reverse(L))
    print(L)
    
    reverse_in_place(L,0,len(L)-1)
    print(L)
    
    print(is_sorted(L))
    print(is_sorted([10,20,45,77]))
    print(is_sorted([]))
    print(is_sorted([2302]))
    
    print_binary('',2)
    print_binary('',3)
    print_binary('',4)
    
    permutations('','UTEP')
    
    meals([],['salad', 'soup', 'pasta'],['steak', 'fish','lasagna'], ['cake', 'ice cream'])
'''
Program Output
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
45
19
True
False
0
1
1000
1111
False
False
False
True
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
[4, 1, 7, 9, 3, 0, 6, 5, 2, 8]
[8, 2, 5, 6, 0, 3, 9, 7, 1, 4]
False
True
True
True
00
01
10
11
000
001
010
011
100
101
110
111
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
UTEP
UTPE
UETP
UEPT
UPTE
UPET
TUEP
TUPE
TEUP
TEPU
TPUE
TPEU
EUTP
EUPT
ETUP
ETPU
EPUT
EPTU
PUTE
PUET
PTUE
PTEU
PEUT
PETU
['salad', 'steak', 'cake']
['salad', 'steak', 'ice cream']
['salad', 'fish', 'cake']
['salad', 'fish', 'ice cream']
['salad', 'lasagna', 'cake']
['salad', 'lasagna', 'ice cream']
['soup', 'steak', 'cake']
['soup', 'steak', 'ice cream']
['soup', 'fish', 'cake']
['soup', 'fish', 'ice cream']
['soup', 'lasagna', 'cake']
['soup', 'lasagna', 'ice cream']
['pasta', 'steak', 'cake']
['pasta', 'steak', 'ice cream']
['pasta', 'fish', 'cake']
['pasta', 'fish', 'ice cream']
['pasta', 'lasagna', 'cake']
['pasta', 'lasagna', 'ice cream']
'''   