import bst
import matplotlib.pyplot as plt

def printSmaller(t,k):
    if t is None:
        return ''
    printSmaller(t.left,k)
    if t.data < k:
        print(t.data,end=' ')
    printSmaller(t.right,k)

def printLeaves(t):
    if t is None:
        return
    if t.left is None and t.right is None:
        print(t.data,end=' ')
    printLeaves(t.left)
    printLeaves(t.right)

def atDepth(t,d):
    if t is None:
        return []
    else:
        if d == 0:
            return [t.data]
        else:
            return atDepth(t.left,d-1) + atDepth(t.right,d-1)

def depthOfK(t,k):
    if t is None:
        return -1
    count = 0
    while t is not None:
        if t.data == k:
            return count
        if k < t.data:
            t = t.left
            count += 1
        else:
            t = t.right
            count+=1
    return -1
        

def tree2List(t):
    if t is None:
        return []
    return tree2List(t.left) + [t.data] + tree2List(t.right)

def list2Tree(L):
    if len(L) == 0:
        return None
    mid = len(L)//2
    tree = bst.BST()
    tree.insert(L[mid])
    root = tree.root
    root.left = list2Tree(L[:mid])
    root.right = list2Tree(L[mid+1:])
    return root
   
            

if __name__ == "__main__":

    A =[11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1,  20, 13]
    B =[8, 15, 5, 13, 11, 6, 7, 2, 4, 18, 14]
    
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
    
    printSmaller(T_empty.root, 16) # 
    print()
    printSmaller(T_oneNode.root, 30) # 23
    print()
    printSmaller(TA.root, 16) # 1 2 4 6 7 8 11 13 14 15
    print()
    printSmaller(TA.root, 5)  # 1 2 4
    print()
    printSmaller(TB.root, 2302) # 2 4 5 6 7 8 11 13 14 15 18 
    print()
    
    print(atDepth(T_empty.root,2))      # []
    print(atDepth(T_oneNode.root,0))    # [23]
    print(atDepth(TA.root,0))           # [11]
    print(atDepth(TA.root,2))           # [2, 7, 14, 17]              
    print(atDepth(TA.root,3))           # [1, 4, 8, 13, 15, 18]
    print(atDepth(TA.root,4))           # [20]
    print(atDepth(TA.root,5))           # []
    print(atDepth(TB.root,2))           # [2, 6, 13, 18]
    
    printLeaves(T_empty.root) # 
    print()
    printLeaves(T_oneNode.root) # 23
    print()
    printLeaves(TA.root) # 1 4 8 13 15 20
    print()
    printLeaves(TB.root) # 4 7 11 14 18 
    print()
    
    print(depthOfK(T_empty.root,2301))   # -1
    print(depthOfK(T_oneNode.root,0))    # -1
    print(depthOfK(TA.root,11))          # 0 
    print(depthOfK(TA.root,6))           # 1
    print(depthOfK(TA.root,18))          # 3
    print(depthOfK(TA.root,21))          # -1
    print(depthOfK(TB.root,11))          # 3             
    
    print(tree2List(TA.root))  # [1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(tree2List(TB.root))  # [2, 4, 5, 6, 7, 8, 11, 13, 14, 15, 18]
    
    A.sort()
    
    root_a = list2Tree(A)
    Ta = bst.BST()
    Ta.root = root_a
    Ta.size = len(A)
    Ta.draw()
    
    L = [i for i in range(31)]
    
    root_a = list2Tree(L)
    Ta = bst.BST()
    Ta.root = root_a
    Ta.size = len(L)
    Ta.draw()
    
        
    