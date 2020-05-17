#   Course: CS 2302
#   Assignment: Lab IV
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 03/23/2020
#   Purpose of the Program: Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import numpy as np

def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

def inOrder(T): 
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
        
def size(T): # Returns the number of nodes in the tree, O(n)
    if T is None: # T is empty
        return 0
    return 1 + size(T[1]) + size(T[2]) # Traverses left and right sub-trees
    
def minimum(T): # Returns the smallest item in the tree, O(n)
    if T[1] is None: # There is no left subtree
        return T[0]
    return minimum(T[1]) # Traverses left subtree
    
def maximum(T): # Returns the largest item in the tree, O(n)
    if T[2] is None: # There is no right subtree
        return T[0]
    return maximum(T[2]) # Traverses right subtree

def height(T): # Returns the height of the tree, O(n)
    if T is None: # T is None
        return -1
    else: # Chooses the largest height from left and right subtree
        return 1 + max(height(T[1]),height(T[2])) 
    
def inTree(T,i): # Searches if i is in the tree, O(n)
    if T is None: # T is None or i was not in the tree
        return False
    if T[0] == i: # Item was found
        return  True
    if T[0] > i: # Traverse left subtree
        return inTree(T[1],i)
    else: # Traverse right subtree
        return inTree(T[2],i)

def printByLevel(T): # Prints data items in level order traversal, O(n)
    Q = [T] # Enqueues root
    while len(Q) > 0: # While the queue is not empty
        t = Q.pop(0) # Dequeues front of queue
        if t!=None:
            print(t[0],end = ' ')
            Q.append(t[1]) # Enqueues left child
            Q.append(t[2]) # enqueues right child
            
def tree2List(T): # Returns a list of the tree's item in ascending order, O(n)
    if T is None: # T is None
        return []
    return tree2List(T[1]) + [T[0]] + tree2List(T[2]) # inOrder traversal 

def leaves(T): # Returns a list containing the leaves of the tree, O(n)
    if T is None: # T is None
        return []
    if T[1] is None and T[2] is None: # Node is leave
        return [T[0]]
    return leaves(T[1]) + leaves(T[2]) # Node is not a leave

def itemsAtDepthD(T,d): # Returns a list containing the items at depth d, O(n)
    if T is None: # T is None
        return []
    else:
        if d == 0: # We are at the desired depth
            return [T[0]] 
        return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1) # Traverses tree
        
def depthOfK(T,k): # Returns the depth of k in the tree, O(n)
    if T is None:
        return -1
    count = 0
    while T is not None:
        if k == T[0]: # k is in current node
            return count
        elif k < T[0]: # k is less than current node
            count += 1
            T = T[1]  # traverse left subtree
        else:
            count += 1
            T = T[2] # traverse right subtree
    return -1 # k was not in the tree

def draw(T,figure_name=' '): # Creates the ax, plt, and parameters of drawNode(), O(1)
    if T is not None:
        fig, ax = plt.subplots()
        drawNode(ax, T, 0, 0, 1000, 120)
        ax.set_title(figure_name)
        ax.axis('off') 
        
def drawNode(ax,T,x0,y0,dx,dy): # Draws the tree, O(n)
    if T[1] is not None: # Left child exists
        ax.plot([x0-dx,x0],[y0-dy,y0],linewidth=1.5,color='b') # Draws left branch
        drawNode(ax, T[1], x0-dx, y0-dy, dx/2, dy) # Traverses left subtree
    if T[2] is not None: # Right child exists
        ax.plot([x0+dx,x0],[y0-dy,y0],linewidth=1.5,color='r') # Draws right branch
        drawNode(ax, T[2], x0+dx, y0-dy, dx/2, dy) # Traverses right subtree
    ax.text(x0,y0, str(T[0]), size=18,ha="center", va="center", # Draws a circle (node)
        bbox=dict(facecolor='w',boxstyle="circle"))  # containing the node's data
            
    
if __name__ == "__main__": 
    
    plt.close('all')
        
    # Balanced Tree
    A = [16,24,20,28,18,22,26,30,17,19,21,23,25,27,29,31,8,12,10,14,11,13,9,15,4,2,6,1,3,5,7]
    T = None
    
    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)  
    
    print(size(T)) # size -> 31
    print(minimum(T)) # minimum -> 1
    print(maximum(T)) # maximum -> 31
    print(height(T)) # height -> 4
    i = 17
    print(inTree(T,i)) # inTree -> True
    i = 32 
    print(inTree(T,i)) # inTree -> False
    printByLevel(T) # print -> 16 8 24 4 12 20 28 2 6 10 14 18 22 26 30 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 
    print()
    print(tree2List(T)) # print -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    print(leaves(T)) # leaves -> [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    d = 2
    print(itemsAtDepthD(T,d)) # depth -> [4, 12, 20, 28]
    d = 3
    print(itemsAtDepthD(T,d)) # depth -> [2, 6, 10, 14, 18, 22, 26, 30]
    k = 7
    print(depthOfK(T,k))  # depth of k -> 4
    k = 10
    print(depthOfK(T,k))  # depth of k -> 3
    draw(T) 
    
    # One node
    # Balanced Tree
    # Unbalanced Tree
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''
    A = [11, 6, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]             
    T = None
    
    for a in A:
        print('Inserting',a)
        T = insert(T,a)   
        print(T)    
        
    inOrder(T)
    
    print()
    print('Tree size: ', size(T))
    print('Minimum: ', minimum(T))
    print('Maximum: ', maximum(T))
    print('Height: ', height(T))
    i = 17
    print('is',i,'? ',isTree(T,i))
    print('print by level: ',end='')
    printByLevel(T)
    print()
    print('tree to list: ',tree2List(T))
    print('leaves: ',leaves(T))
    d = 1
    print('items at depth',d,'is:',itemsAtDepthD(T,d))
    k = 3
    print('Depth of',k,'is:',depthOfK(T,k))
    draw(T)
    '''
    

