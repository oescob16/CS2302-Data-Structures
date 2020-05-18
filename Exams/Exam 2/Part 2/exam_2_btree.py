import matplotlib.pyplot as plt
import numpy as np
import btree
import math 

def find_depth(T,k):
    if type(T)==btree.BTree:
        T=T.root
    if T.is_leaf and k not in T.data:
        return -1    
    if k in T.data:
        return 0
    ch = 0
    for i in range(len(T.data)):  
        if k < T.data[i]:
            ch = i
            break 
    if k > T.data[-1]:
        ch = len(T.data)
    d = find_depth(T.child[ch],k)
    if d>=0:
        d+=1
    return d

def nodes_with_n_keys(T,n):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return 0
    count = int(len(T.data) == n)
    if not T.is_leaf:
        for i in T.child:
            count += nodes_with_n_keys(i,n)
    return count

def add_n(T,n):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return 0
    for j in range(len(T.data)):
        T.data[j] += n
    if not T.is_leaf:
        for i in T.child: 
            add_n(i,n)
    return
        
def prune_leaves(T):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return 0
    if T.is_leaf:
        T.data = T.data[0:2]
    for i in T.child:
        prune_leaves(i)

if __name__ == "__main__":  
    plt.close('all') 
    T = btree.BTree()  
    T_empty = btree.BTree()  
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
    T.draw()  
    
    print('Question 1')
    print(find_depth(T,10))    # 0
    print(find_depth(T,14))    # 1
    print(find_depth(T,7))     # 1
    print(find_depth(T,5))     # 1 <- There is a typo, 5 is in depth 2
    print(find_depth(T,9))     # 2
    print(find_depth(T,25))   # -1
    
    print('Question 2')
    print(nodes_with_n_keys(T,1))  # 1
    print(nodes_with_n_keys(T,2))  # 5
    print(nodes_with_n_keys(T,3))  # 2
    
    print('Question 3')    
    add_n(T,5)
    T.draw()   
    
    print('Question 4')   
    prune_leaves(T)
    T.draw() 
    
    