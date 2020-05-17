import matplotlib.pyplot as plt
import numpy as np
import btree

def smallest(T):
    t = T.root
    while not t.is_leaf:
        t = t.child[0]
    return t.data[0]

def largest(T):
    t = T.root
    while not t.is_leaf:
        t = t.child[-1] 
    return t.data[-1]

def numItems(T):
    count = 0
    Q = [T.root]
    while len(Q)>0: 
        curr_node_size = len(Q)
        while curr_node_size > 0: 
            length_root = Q.pop(0)
            count += len(length_root.data)
            for i in range(len(length_root.child)): 
                Q.append(length_root.child[i])
            curr_node_size -= 1
    return count

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    for num in nums:
        T.insert(num)
    T.draw()

    print(smallest(T))  # 1
    print(largest(T))   # 30
    print(numItems(T))  # 30


