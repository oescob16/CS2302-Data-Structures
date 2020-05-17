import hash_table_chain as htc

def location(h,k):
    b, index = -1, None
    b = h.h(k)
    for i in range(len(h.bucket[b])):
        if h.bucket[b][i].key == k:
            return b,i
    return b, index
        
def change_key(h,k,new_k):
    if h.retrieve(k) == None:
        return
    data = h.retrieve(k)
    if h.insert(new_k,data) == -1:
        return
    h.delete(k)
    return
        
def unique_items(L):
    h = htc.HashTableChain(len(L))
    unique = []
    for i in range(len(h.bucket)):
        if h.insert(L[i],L[i]) == 1:
            unique.append(L[i])
    unique.sort()
    return unique
            
def sum2(L,k):
    for i in range(len(L)):
        for j in range(1,len(L)):
            if L[i] + L[j] == k:
                return i,j
    return None, None

def sum2HT(L,k):
    h = htc.HashTableChain(len(L))
    for i in range(len(L)): # iterates the list
        h.insert(i,k-L[i])  # index as data and data as k - L[i], to find the missing number
        if h.retrieve(i) in L: # checks if the curr index data is in the list L
            return i,L.index(h.bucket[i][0].data) # returns curr index (i) and the pos (j) in which the other number is
    return None, None # No such values that sum is equal to k
    

if __name__ == "__main__":
    h = htc.HashTableChain(5)
    
    players = ['Bellinger','Betts', 'Hernandez', 'Pederson', 'Pollock', 'Taylor']
    numbers= [35, 50, 14, 31, 11, 3]
    
    for i in range(len(players)):
        h.insert(numbers[i],players[i])
        
    h.print_table()
    
#    Table contents:
#    bucket 0: [ [35, Bellinger] [50, Betts] ]
#    bucket 1: [ [31, Pederson] [11, Pollock] ]
#    bucket 2: [ ]
#    bucket 3: [ [3, Taylor] ]
#    bucket 4: [ [14, Hernandez] ]
    
    print('\nQuestion 1')
    print(location(h,31))  # (1, 0)
    print(location(h,14))  # (4, 0)
    print(location(h,4))   # (4, None)
    
    print('\nQuestion 2')
    change_key(h,35,22)
    h.print_table()
    
#    Table contents:
#    bucket 0: [ [50, Betts] ]
#    bucket 1: [ [31, Pederson] [11, Pollock] ]
#    bucket 2: [ [22, Bellinger] ]
#    bucket 3: [ [3, Taylor] ]
#    bucket 4: [ [14, Hernandez] ]

    change_key(h,14,26)
    h.print_table()
#    Table contents:
#    bucket 0: [ [50, Betts] ]
#    bucket 1: [ [31, Pederson] [11, Pollock] [26, Hernandez] ]
#    bucket 2: [ [22, Bellinger] ]
#    bucket 3: [ [3, Taylor] ]
#    bucket 4: [ ]    
    
    change_key(h,17,18)
    h.print_table()
#    Table contents:
#    bucket 0: [ [50, Betts] ]
#    bucket 1: [ [31, Pederson] [11, Pollock] [26, Hernandez] ]
#    bucket 2: [ [22, Bellinger] ]
#    bucket 3: [ [3, Taylor] ] 
#    bucket 4: [ ]    
        
    change_key(h,11,50)
    h.print_table()
#    Table contents:
#    bucket 0: [ [50, Betts] ]
#    bucket 1: [ [31, Pederson] [11, Pollock] [26, Hernandez] ]
#    bucket 2: [ [22, Bellinger] ]
#    bucket 3: [ [3, Taylor] ]
#    bucket 4: [ ]

    L1 = [1, 9, 5, 5, 8, 0, 8, 5, 5, 2]
    L2 = [1, 7, 0, 5, 8, 9, 7, 7, 9, 8]
    L3 = [7, 10, 14, 8, 16, 5, 2, 18, 13, 6]
    
    print('\nQuestion 3')
    print(unique_items(L1)) # [0, 1, 2, 5, 8, 9]
    print(unique_items(L2)) # [0, 1, 5, 7, 8, 9]
    print(unique_items(L3)) # [2, 5, 6, 7, 8, 10, 13, 14, 16, 18] 
    
    print('\nQuestion 4')
    k = 13
    i,j = sum2(L3, k) 
    print('k =',k,'indices:', i,j)   # k = 13 indices: 0 9
    if i!= None:
        print(L3[i],'+',L3[j],'=',k) # 7 + 6 = 13
    
    k = 4
    i,j = sum2(L3, k)
    print('k =',k,'indices:', i,j)   # k = 4 indices: 6 6
    if i!= None:
        print(L3[i],'+',L3[j],'=',k) # 2 + 2 = 4
       
    k = 33
    i,j = sum2(L3, k)
    print('k =',k,'indices:', i,j)   # k = 33 indices: None None
    if i!= None:
        print(L3[i],'+',L3[j],'=',k)
        
    print('\nQuestion 5')    
    k = 13
    i,j = sum2HT(L3, k)
    print('k =',k,'indices:', i,j)   # k = 13 indices: 0 9
    if i!= None:
        print(L3[i],'+',L3[j],'=',k) # 7 + 6 = 13
    
    k = 4
    i,j = sum2HT(L3, k)
    print('k =',k,'indices:', i,j)   # k = 4 indices: 6 6
    if i!= None:
        print(L3[i],'+',L3[j],'=',k) # 2 + 2 = 4
       
    k = 33
    i,j = sum2HT(L3, k)
    print('k =',k,'indices:', i,j)   # k = 33 indices: None None
    if i!= None:
        print(L3[i],'+',L3[j],'=',k)
           