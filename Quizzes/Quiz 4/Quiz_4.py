import matplotlib.pyplot as plt
import bst

def childrenOfRoot(t):
    if t.root is None:
        return 0
    count = 0
    if t.root.left is not None:
        count += 1
    if t.root.right is not None:
        count += 1
    return count

def rootPredecessor(t):
    t = t.left
    while t.right is not None:
        t = t.right
    return t.data

def treeToList(t):
    if t is None:
        return []
    return treeToList(t.left) + [t.data] + treeToList(t.right)

if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[25, 13, 11, 6, 7, 18, 14]
    
    T_empty = bst.BST()
    T_oneNode = bst.BST()
    T_oneNode.insert(23)
    TA = bst.BST()
    for a in A:
        TA.insert(a)
    TB = bst.BST()
    for b in B:
        TB.insert(b)

    plt.close('all')
    TA.draw()
    TB.draw()
    
    print(childrenOfRoot(T_empty))  # 0
    print(childrenOfRoot(T_oneNode))# 0
    print(childrenOfRoot(TA))       # 2
    print(childrenOfRoot(TB))       # 1
    
    
    print(rootPredecessor(TA.root))  # 8
    print(rootPredecessor(TB.root)) # 18
    
    print(treeToList(TA.root))  # [1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(treeToList(TB.root))  # [6, 7, 11, 13, 14, 18, 25]
    
    
