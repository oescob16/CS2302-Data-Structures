import numpy as np
import singly_linked_list as sll
import matplotlib.pyplot as plt
import math

def appears_in_all_rows(A,i):
    for j in range(A.shape[0]):
        if i not in A[j]:
            return False
    return True

def equal_first_and_second(L):
    if L.head != None and L.head.next != None:
        return L.head.data == L.head.next.data
    return False

def replace(L,i,j):
    temp = L.head
    while temp != None:
        if temp.data == i:
            temp.data = j
        temp = temp.next  


def remove_all_but_first_and_last(L):
    if L.head != None and L.head.next != None:
        L.head.next = L.tail
    
if __name__ == "__main__":
    plt.close('all') 
    A1 = np.array([[1,2,3],[4,5,3],[2,3,9]])
    A2 = np.array([[1,2,3],[4,3,6],[7,8,9]])
    print(A1)
    print(A2)
    print(appears_in_all_rows(A1,3)) # True 
    print(appears_in_all_rows(A2,3)) # False
    
    L1 = sll.List()
    L1.append(2302)
    L1.draw()
    L2 = sll.List()
    L2.extend([3,3,1,2,9,7,4,8,6,5])
    L2.draw()
    L3 = sll.List()
    L3.extend([9,7,4,8,6,5])
    L3.draw()
    
    print(equal_first_and_second(L1))  # False
    print(equal_first_and_second(L2))    # True
    print(equal_first_and_second(L3))    # False
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    replace(L,6,0)
    L.print()   # [3, 0, 1, 2, 9, 7, 4, 8, 0, 5]
    
    
    L= sll.List()
    L.extend([3,6,1,2,9,7,4,8,6,5])
    L.draw()
    
    remove_all_but_first_and_last(L)
    
    L.print() # [3, 5]
    