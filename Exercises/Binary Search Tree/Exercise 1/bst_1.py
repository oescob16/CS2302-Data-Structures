import bst
import queue 

def smallest(t):
    while t.left is not None:
        t = t.left
    return t.data

def largest(t):
    while t.right is not None:
        t = t.right
    return t.data

def isLeftChild(t):
    parent = t.parent
    child = t
    if parent is None: # t is root
        return False
    elif parent.left is child: # node is left child
        return True
    else: # node is not left child
        return False
        
     
if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    

    T = bst.BST()
    T2 = bst.BST()
    
    for a in A:
        T.insert(a)

    for b in B:
        T2.insert(b)

    T.inOrder()
    #plt.close('all')
    T.draw()
    T2.draw()
    
    print(smallest(T.root)) # 1
    print(largest(T.root))  # 20
    
    print(smallest(T2.root)) # 2
    print(largest(T2.root))  # 18
    
    t = T.find(14)
    print(isLeftChild(t))   # True
    
    t = T.find(4)
    print(isLeftChild(t))   # False
    
    t = T2.find(13)
    print(isLeftChild(t))   # True
    
    t = T2.find(8)
    print(isLeftChild(t))   # False