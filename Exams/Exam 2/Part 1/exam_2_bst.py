import matplotlib.pyplot as plt
import numpy as np
import bst

def count_odd(T): # Error: We are only adding the value of the first call
    s = 0
    if type(T)==bst.BST: 
        T=T.root
    if T==None:
        return s
    if T.data%2 ==1:
        s+=1
    return s + count_odd(T.left) + count_odd(T.right)

def is_full(T):
    if type(T) == bst.BST:
        T = T.root
    if T is None:
        return True
    if T.left is None and T.right is None: # No child exists
        return True
    if T.left is None and T.right != None: # Only right child exists
        return False
    if T.left != None and T.right is None: # Only left child exists
        return False
    return is_full(T.left) and is_full(T.right)  
    

def subtract_n(T,n):
    if type(T) == bst.BST:
        T = T.root
    if T is None:
        return
    T.data -= n
    subtract_n(T.left,n)
    subtract_n(T.right,n)
    
def follow_path(T,s):   
    if type(T) == bst.BST:
        T = T.root
    if len(s) == 0:
        return T.data
    while T is not None:
        if len(s) == 0:
            return T.data 
        if s[0] == 'L':
            T = T.left
        else:
            T = T.right
        s = s[1:]
    return None

if __name__ == "__main__":
    plt.close('all')

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]
    T = bst.BST()
    for a in A:
        T.insert(a)
    T.draw()
    
    A =[8, 15, 6, 11, 7, 17, 2, 4, 16, 20, 1]
    T2 = bst.BST()
    for a in A:
        T2.insert(a)
    T2.draw()  
    
    print('Question 1')     
    print(count_odd(T))     # 6
    print(count_odd(T2))    # 5
    
    print('Question 2')
    print(is_full(T))    # False
    print(is_full(T2))   # True
    
    print('Question 3')
    subtract_n(T2,2)
    T2.draw()
    
    T.draw()
    print('Question 4')
    print(follow_path(T,''))     # 11
    print(follow_path(T,'LR'))   #  7
    print(follow_path(T,'RLR'))  # 15
    print(follow_path(T,'LRLR')) # None