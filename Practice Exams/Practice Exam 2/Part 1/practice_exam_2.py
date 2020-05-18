#   CS 2302 - Data Structures
#   Instructor: Dr. Fuentes
#   Teaching Assistant: Harshavardhini Bagavathyraj
#   Author: Oswaldo Escobedo
#   Assignment: Practice Exam 2
#   Date of Last Modification: 04/05/2020
#   Purpose of the Program: To practice the topics of
#   BST, BTrees and hashtables, which are topics that are going to be on Exam 2

import matplotlib.pyplot as plt
import numpy as np
import bst
import btree
import hash_table_chain as htc

def path_to_largest(T): # Returns a list of the path from root to largest data
    if type(T) == bst.BST:
        T = T.root
    if T is None: 
        return []
    return [T.data] + path_to_largest(T.right) # Concatenates data

def path_to_k(T,k):
    if type(T) == bst.BST:
        T = T.root 
    path = []
    while T is not None: 
        if k == T.data: # k is in current node
            return path + [T.data] # returns the path + [key]
        path += [T.data]
        if k < T.data: # key is in the left subtree
            T = T.left
        else: # key is in the right subtree
            T = T.right
    return [] # key was not found

def prune_BST(T,d):
    if type(T) == bst.BST:
        T = T.root
    if T is None:
        return
    if d == 0: # We are in the desired depth
        T.left = None # Prunes left subtree
        T.right = None # Prunes right subtree
    prune_BST(T.left,d-1) # Traverses to left subtree
    prune_BST(T.right,d-1) # Traverses to right subtree

def keys_in_path_to_smallest(T):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return []
    if T.is_leaf:
        return T.data
    return (keys_in_path_to_smallest(T.child[0]) # Traverses left subtree
            + T.data) # Concatenates in ascending order

def smallest_in_nodes(T):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return []
    if T.is_leaf:
        return [T.data[0]] # Returns the smallest value in the node
    keys = []
    for i in T.child: 
        keys += smallest_in_nodes(i) # Concatenates all leaves
        if T.data[0] not in keys: # Condition to avoid repetition in list
            keys += [T.data[0]] # Concatenates nodes that are not leaves
    return keys
    
def prune_Btree(T,d):
    if type(T) == btree.BTree:
        T = T.root
    if len(T.data) == 0:
        return
    if T.is_leaf: # Depth d does not exists in the tree
        return
    if d == 0:
        T.is_leaf = True # Converts the current node to be a leave
        return
    for i in T.child:
        prune_Btree(i,d-1)

def item_status(h,k): 
    if h.retrieve(k) != None: # Key is in hashtable
        if len(h.bucket[h.h(k)]) == 1: # Key is the only record in its bucket
            return 0
        else: # Key is not the only record in its bucket 
            return 1
    else: # Key is not in the hashtable
        return -1
   
def repeats(S,c):
    h = htc.HashTableChain(len(S))
    repeat = []
    for i in range(len(S)):
        DNA = S[i:i+c] # Creates a string of length c
        if (h.retrieve(DNA) != None and # Sequence appears more than one time
            DNA not in repeat): # Condition to avoid repetition 
            repeat += [DNA] 
        else:
            h.insert(DNA,1) # Sequence appears at least one time
    return repeat

def build_index_table(L):
    h = htc.HashTableChain(len(L))
    for i in range(len(L)):
        if h.retrieve(L[i]) != None: # Key is already in the hashtable.
            indices = h.retrieve(L[i]) + [i] # So, we concatenate the index of the repeated key 
            h.update(L[i],indices)
        else: # Key is not in the hashtable
            h.insert(L[i],[i])
    return h

if __name__ == "__main__":
    plt.close('all')
    

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    T = bst.BST()

    for a in A:
        T.insert(a)
        
    T.draw()
    
    print('Question 1')     
    print(path_to_largest(T))    # [11, 16, 17, 18, 20]
    
    print('Question 2')
    print(path_to_k(T,7))   # [11, 6, 7]
    print(path_to_k(T,15))  # [11, 16, 14, 15] 
    print(path_to_k(T,19))  # []
    
    print('Question 3')
    prune_BST(T,3)
    T.draw()
    prune_BST(T,2)
    T.draw()
    prune_BST(T,1)
    T.draw()
    prune_BST(T,0)
    T.draw()
    
    print('Question 4')
    T = btree.BTree()    
    nums = [6, 3, 16, 11, 7, 17, 14, 8, 5, 19, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12, 21]
    for num in nums:
        T.insert(num)
    T.draw()

    print(keys_in_path_to_smallest(T))  # [1, 2, 3, 7, 10]

    print('Question 5')
    print(smallest_in_nodes(T)) # [1, 3, 4, 8, 10, 11, 14, 15, 18]

    print('Question 6')
    prune_Btree(T,2)
    T.draw()
    prune_Btree(T,1)
    T.draw()
    prune_Btree(T,0)
    T.draw()
    
    print('Question 7')
    h = htc.HashTableChain(5)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
    h.print_table()
    
    print(item_status(h,99))  # -1
    print(item_status(h,3))   # 0
    print(item_status(h,11))  # 1
    
   
    print('Question 8')
    S = 'GACCGAATCCG'
    print(repeats(S,1)) # ['C', 'G', 'A']
    print(repeats(S,2)) # ['GA', 'CC', 'CG']
    print(repeats(S,3)) # ['CCG']
    print(repeats(S,4)) # []
    
    print('Question 9')
    L = [2,4,6,1,2,3,1,12]    
    h = build_index_table(L)
    h.print_table()
    
#    Table contents:
#    bucket 0: [ ]
#    bucket 1: [ [1, [3, 6]] ]
#    bucket 2: [ [2, [0, 4]] ]
#    bucket 3: [ [3, [5]] ]
#    bucket 4: [ [4, [1]] [12, [7]] ]
#    bucket 5: [ ]
#    bucket 6: [ [6, [2]] ]
#    bucket 7: [ ]
 
    print(h.retrieve(2))    # [0, 4]
    print(h.retrieve(4))    # [1]
    print(h.retrieve(23))   # None
    