import matplotlib.pyplot as plt
import numpy as np
import hash_table_chain as htc

def same_hash_as_k(h,k): 
    sh = []
    b = h.bucket[h.h(k)]
    for i in b:
        sh.append(i.key)  
    return sh 
    
def difference(L1,L2):
    diff = []
    h = htc.HashTableChain(len(L2))  
    for i in L2:
        h.insert(i,i)
    for i in L1:
        val = h.retrieve(i) 
        if val == None:
            diff.append(i)  
    return diff  
    
def reversed_pairs(L):
    pairs = []
    h = htc.HashTableChain(len(L))
    for rev in L:
        h.insert(rev[::-1],rev[::-1])
    for s in L:
        val = h.retrieve(s) 
        if val != None:
            pairs.append(val)  
    return sorted(pairs)
    

if __name__ == "__main__":   
    plt.close('all') 
    
    countries = ['Russia','Canada', 'USA', 'Brazil', 'Australia', 'China','Spain','France']
    capitals = ['Moscow','Ottawa', 'Washington', 'Brasilia', 'Canberra', 'Beijing','Madrid','Paris']
    h = htc.HashTableChain(len(countries))

    for i in range(len(countries)):
        h.insert(countries[i],capitals[i])
    h.print_table()
    
    print(same_hash_as_k(h,'Russia')) # ['Russia', 'USA', 'France']
    print(same_hash_as_k(h,'Canada')) # ['Canada']
    
    L1 = [2,3,5,7,11,13]
    L2 = [3,4,5,11,17]
        
    print(difference(L1,L2)) # [2, 7, 13]
    
    L0=['the','rats','were','looking','at','a','star']
    L1 = ['a','lone','wolf','went','with','the','flow']
    L2 = ['anna','would','rather','write','a','while','loop','than','swim','in','the','pool']
    print(reversed_pairs(L0)) # ['a', 'rats', 'star']
    print(reversed_pairs(L1)) # ['a', 'flow', 'wolf']
    print(reversed_pairs(L2)) # ['a', 'anna', 'loop', 'pool']