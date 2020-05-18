import matplotlib.pyplot as plt
import numpy as np
import bst
import btree
import hash_table_chain as htc 

def path_to_largest(T): # Error: we are only appending and returning the 
    p = []           # initial root's data when it should be concatenating
    if T==None:     # /storing all the nodes we visit into p 
        return []
    if type(T)==bst.BST: 
        T=T.root
    p += [T.data] #p.append(T.data)  
    return p + path_to_largest(T.right)

def path_to_k(T,k): # Error: We need to have a condition that returns [] if the key was not found
    if T==None:
        return []
    if type(T)==bst.BST:
        T=T.root
    if T.data == k:
        return [T.data]
    if T.data < k:
        p = path_to_k(T.right,k)
    else:
        p = path_to_k(T.left,k)
    p = [T.data]+p 
    if k not in p: # If the key was not found it should return []
        return []
    return p

def prune_BST(T,d): # Error: We should also have a condition that returns inmediately if we are at none
    if type(T)==bst.BST:
        T=T.root
    if T is None: 
        return
    if d <= 0:
        T.left = T.right=None
    else:
        prune_BST(T.left,d-1)
        prune_BST(T.right,d-1)

def keys_in_path_to_smallest(T): # Error: We are not adding to the list the data we visit
    p = []
    if type(T)==btree.BTree:
        T=T.root
    p = p+T.data
    if not T.is_leaf: 
        p = keys_in_path_to_smallest(T.child[0]) + p 
    return p

def smallest_in_nodes(T): # No errors found, however, instead of using a library we can 
    if type(T)==btree.BTree: # concatenate the min nodes while traversing the tree.
        T=T.root          # This will improve the time complexity from O(n^2) to O(n)
    s = [T.data[0]]    
    if T.is_leaf:
        return s
    else:
        s = smallest_in_nodes(T.child[0]) + s
        for c in range(1,len(T.child)):
            s = s + smallest_in_nodes(T.child[c])
    return s

def prune_Btree(T,d): # Error: We need to subtract d by one each recursive call to get to the base case
    if type(T)==btree.BTree:
        T=T.root
    if d <= 0:
        T.is_leaf = True 
    else:
        for c in T.child:
            prune_Btree(c,d-1)  

def item_status(h,k): # No errors found, however we can improve the time complexity 
    b = h.h(k)      # from O(n^2) to be best case: O(1) and worst case: O(n)
    if h.retrieve(k) != None:
        if len(h.bucket[b]) == 1:
            return 0
        else:
            return 1
    else:
        return -1 
   
def repeats(S,c): # Error: We should avoid repetition when appending the sequences to the list
    h = htc.HashTableChain(len(S)) 
    repeat = []
    for i in range(len(S)-c+1):
        s = S[i:i+c]
        count = h.retrieve(s)
        if count == None:
            h.insert(s,1)
        else:
            count +=1
            h.update(s,count)
            if s not in repeat: 
                repeat.append(s)      
    return repeat

def build_index_table(L): # Error: The indices are only being added to the first record
    h = htc.HashTableChain(len(L))
    for i in range (len(L)):
        if h.retrieve(L[i]) == None:
            h.insert(L[i],[i])
        else:
            #buck = h.h(L[i])
            index = h.retrieve(L[i]) # Therefore, we need to specify which key we want to update
            index.append(i)
            h.update(L[i],index)
            #h.bucket[buck][0].data.append(i)
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

    print(keys_in_path_to_smallest(T)) # [1, 2, 3, 7, 10]

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
    L = [2,11,4,6,1,2,3,1,11]   
    h = build_index_table(L)
    h.print_table()
    
    #Table contents:
    #bucket 0: [ ]
    #bucket 1: [ [1, [4, 7]] ]
    #bucket 2: [ [2, [0, 5]] [11, [1, 8]] ] 
    #bucket 3: [ [3, [6]] ]
    #bucket 4: [ [4, [2]] ]
    #bucket 5: [ ]
    #bucket 6: [ [6, [3]] ]
    #bucket 7: [ ]
    #bucket 8: [ ]
    
    print(h.retrieve(2))    # [0, 5]
    print(h.retrieve(4))    # [2]
    print(h.retrieve(23))   # None
    
    
    
    