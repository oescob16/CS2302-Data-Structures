import dsf
import numpy as np
import matplotlib.pyplot as plt

def is_singleton(s,v):
    for i in s.set_list():
        if v in i and len(i) == 1:
            return True
    return False

def is_compressed(s):
    for i in s.parent:
        if i != -1 and s.parent[i] != -1:
            return False
    return True

if __name__ == "__main__":   
    plt.close("all")      
    s = dsf.DSF(8)
    s.union(0,1)
    print(s.parent)
    print(is_compressed(s))  # True
    s.draw()
    
    s.union(7,2)
    print(s.parent)
    print(is_compressed(s))  # True
    s.draw()
    
    s.union(3,5)
    print(s.parent)
    print(is_compressed(s))  # True
    s.draw()
    
    s.union(1,5)
    print(s.parent)
    print(is_compressed(s))  # False
    
    s.draw()
    print('Set of sets:',s.set_list())
    # Set of sets: [[0, 1, 3, 5], [4], [6], [2, 7]]
    
    for v in range(8):
        print('is_singleton(s,{}): {}'.format(v,is_singleton(s,v)))
    '''
    is_singleton(s,0): False
    is_singleton(s,1): False
    is_singleton(s,2): False
    is_singleton(s,3): False
    is_singleton(s,4): True
    is_singleton(s,5): False
    is_singleton(s,6): True
    is_singleton(s,7): False
    '''
    
    
     