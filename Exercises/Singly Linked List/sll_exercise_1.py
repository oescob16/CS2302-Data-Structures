#   Course: CS 2302
#   Assignment: Exercise singly linked list
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 02/19/2020
#   Purpose of the Program: To practice and undesrtand how singly linked lists 
#   work and implement functions given from sll_exercise_1.py

import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def first(L):
    if L.head == None:
        return -math.inf
    return L.head.data 

def last(L):
    if L.head == None:
        return -math.inf
    return L.tail.data

def swap_first_and_last(L):
    if L.head == None:   # If the list is empty then do nothing
        return
    L.head.data,L.tail.data = L.tail.data,L.head.data   # swaps the first and last element

def length(L):
    temp = L.head   # Creates a temp variable to traverse the linked list
    counter = 0
    while temp is not None: # Stops until temp gets to the end of the list
        counter += 1
        temp = temp.next
    return counter

def sum_list(L):
    sum_L = 0
    temp = L.head
    while temp is not None:
        sum_L += temp.data
        temp = temp.next
    return sum_L

def max_list(L):
    if L.head == None:
        return -math.inf
    max_L = 0
    temp = L.head
    while temp is not None:
        if temp.data > max_L:
            max_L = temp.data
        temp = temp.next
    return max_L

def to_list(L):
    pylist = []   # Creates an empty list 
    temp = L.head
    while temp is not None:
        pylist.append(temp.data)   # Appends the data of the current node to pylist
        temp = temp.next
    return pylist

def identical(L1,L2):
    temp1 = L1.head
    temp2 = L2.head
    while temp1 is not None and temp2 is not None:
        if temp1.data != temp2.data:   # Condition to check if the data from L1 and 
            return False             # L2 is the same.
        temp1 = temp1.next
        temp2 = temp2.next
    if temp1 is None and temp2 is None: # If both linked lists have the same length and
        return True   #  arrived to the end at the same time, then it means they are identical.
    else:
        return False

def delete_first(L):
    if L.head is None:
        return
    L.head = L.head.next # Now head will point to the second node.

if __name__ == "__main__":
    plt.close('all')
    L1 = sll.List()
    L1.draw()
    L2 = sll.List()
    L2.extend([3,6,1,2,9,7,4,8,5])
    L2.draw()
    
    print(first(L1))   # -inf
    print(first(L2))   # 3
    
    print(last(L1))    # -inf
    print(last(L2))    # 5
    
    swap_first_and_last(L1)
    L1.print()              # []
    swap_first_and_last(L2) # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    L2.print()          
    
    print(length(L1))   # 0
    print(length(L2))   # 9
    
    print(sum_list(L1)) # 0
    print(sum_list(L2)) # 45
    
    print(max_list(L1)) # -inf
    print(max_list(L2)) # 9
    
    print(to_list(L1))  # []
    print(to_list(L2))  # [5, 6, 1, 2, 9, 7, 4, 8, 3]
    
    L3 = sll.List()
    L3.extend([3,6,1,2,9,7,4,8,5]) 
    
    L4 = sll.List()
    L4.extend([3,6,1,2,9,7,4,8,5])
    
    L5 = sll.List()
    L5.extend([3,6,1,2])
    
    print(identical(L1,L2))  # False
    print(identical(L2,L3))  # False
    print(identical(L3,L4))  # True
    print(identical(L4,L5))  # False

    delete_first(L2) 
    L2.print()       # [6, 1, 2, 9, 7, 4, 8, 3]