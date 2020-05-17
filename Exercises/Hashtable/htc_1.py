# Starter code for hash table exercise 1
# Rename this program as lastname_firstname_htc_ex1.py and submit it 
import numpy as np
import hash_table_chain as htc

def load_factor(h):
    c = 0 # Variable that adds the length of all the buckets
    n = len(h.bucket)
    for i in range(n):
        c += len(h.bucket[i])
    return c/n

def longest_bucket(h):
    max_bucket = 0 # Stores the length of the longest bucket so far
    length = len(h.bucket)
    for i in range(length):
        if len(h.bucket[i]) > max_bucket:
            max_bucket = len(h.bucket[i]) 
    return max_bucket

def check(h):
    n = len(h.bucket)
    for i in range(n):
        for j in h.bucket[i]:
            if j.key % n != i: # Checks if key in the correct index
                return False
    return True

def has_duplicates(L):
    h = htc.HashTableChain(len(L))
    for i in range(len(L)):
        if h.insert(L[i],L[i]) == -1: # Using number as key and index as data
            return True
    return False

if __name__ == "__main__":
    h = htc.HashTableChain(9)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]

    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()

    print(load_factor(h))  # 0.66666666666666
    
    print(longest_bucket(h)) # 2 
    
    print(check(h)) # True
    h.bucket[2][0].key = 2302
    h.print_table()
    print(check(h)) # False
    
    L1 = [1,4,2,5,6,7,8,39,20,45]
    L2 = [1,4,2,5,6,7,8,39,20,45,9,13,5,34]
    
    print(has_duplicates(L1)) # False
    print(has_duplicates(L2)) # True
    
    
    for i in range(len(h.bucket)):
        if len(h.bucket[i]) == 0:
            continue
        print(h.bucket[i][0].key) # Prints first item
    
    
    L = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    h3 = htc.HashTableChain(len(L))
    for i in range(len(L)):
        if L[i] % 2 == 0:
            h3.insert(L[i],L[i]) # inserts even keys
    h3.print_table()   
    

