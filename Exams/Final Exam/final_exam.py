import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll
import bst
import btree
import graph_AL
import graph_AM
import hash_table_chain as htc

def set_drawing_parameters_and_save(ax,title):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    fig.suptitle(title, fontsize=16)
    plt.show()
    fig.savefig(title+'.png')

def draw_squares(ax,n,x0,y0,side):
    if n>0:
        s = side/2
        x = x0 + np.array([-s,-s,s,s,-s])
        y = y0 + np.array([-s,s,s,-s,-s])
        ax.plot(x,y,linewidth=1.0,color='b')
        draw_squares(ax,n-1,x0-(side/2),y0,side/4)
        draw_squares(ax,n-1,x0,y0-(side/2),side/4)
        draw_squares(ax,n-1,x0+(side/2),y0,side/4)
        draw_squares(ax,n-1,x0,y0+(side/2),side/4)
        
def smaller(L,i):
    if len(L) == 0:
        return []
    if L[0] < i:
        return smaller(L[1:],i) + [L[0]] 
    return smaller(L[1:],i)

def cumulative_sum(L):
    C = sll.List()
    Sum = 0
    t = L.head
    while t != None:
        Sum += t.data
        C.append(Sum)
        t = t.next
    return C

def sorted_rows(a):
    sorted_row = []
    for i in range(a.shape[0]):
        if all([a[i][j-1] <= a[i][j] for j in range(1,a.shape[1])]):
            sorted_row.append(i)
    return sorted_row
            
def in_leaves(T):
    if T is None:
        return []
    if T.left is None and T.right is None:
        return [T.data]
    return in_leaves(T.left) + in_leaves(T.right)

def internal(T):
    if T.is_leaf:
        return []
    L = internal(T.child[0])
    L += T.data
    if not T.is_leaf:
        for c in T.child[1:]:
            L += internal(c)
    return L

def find_sum_pair(S,k):
    h = htc.HashTableChain(len(S))
    for s in S:
        if h.retrieve(k-s)!=None:
            return [h.retrieve(k-s),s]
        else:
            h.insert(s,s)
    return None
                
def make_undirected(G):
    G.directed = False
    for i in range(G.am.shape[0]):
        for j in range(G.am.shape[1]):
            if G.am[i,j] == 1:
                G.am[j,i] = 1
    
def make_weighted(G):
    G.weighted = True
    for v in range(len(G.al)):
        for e in range(len(G.al[v])):
            G.al[v][e].weight = v + G.al[v][e].dest    
    return 

def subsetsum_v2(S,g,remaining):
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Simple solution; does not return the subset that adds up to g if it exists
    if g==0 or g==remaining: # Take no items or take all items 
        return True
    if g<0 or remaining<g:
    		return False
    return subsetsum_v2(S[1:],g-S[0],remaining-S[0]) or subsetsum_v2(S[1:],g,remaining-S[0])

if __name__ == "__main__":

    plt.close("all") # Close all figures
    
    print('================ Question 1 ===============')
    fig, ax = plt.subplots()
    draw_squares(ax, 2, 0, 0, 800)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 2, 0, 0, 800)')
    
    fig, ax = plt.subplots()
    draw_squares(ax, 3, 0, 0, 800)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 3, 0, 0, 800)')
    
    fig, ax = plt.subplots()
    draw_squares(ax, 4, 0, 0, 800)
    set_drawing_parameters_and_save(ax,'draw_squares(ax, 4, 0, 0, 800)')

    print('================ Question 2 ===============')
    L2 =  [1, 7, 4, 3, 0, 9, 2, 5, 8, 6]
    print(smaller(L2,3))    # [2, 0, 1]
    print(smaller(L2,6))    # [5, 2, 0, 3, 4, 1]
    print(smaller(L2,9))    # [6, 8, 5, 2, 0, 3, 4, 7, 1]
    
    print('================ Question 3 ===============')
    L3a = sll.List()
    L3b = sll.List()
    L3c = sll.List()
    L3d = sll.List()
    L3b.extend([5])
    L3c.extend([7,8])
    L3d.extend([3, 0, 9, 2, 5])
    for L in [L3a,L3b,L3c,L3d]:  # Show original lists
        L.print()
        L.draw('Original list')
       
    for L in [L3a,L3b,L3c,L3d]:  # Show cumulative sums
        C = cumulative_sum(L)
        C.print()
        L.draw('cumulative sum list')
    # []
    # [5]
    # [7, 15]
    # [3, 3, 12, 14, 19]
    
    print('================ Question 4 ===============')
    A1 = np.array([[1],[2],[3]])
    A2 = np.array([[1,3],[12,2],[3,5],[7,7]])
    A3 = np.array([[1,3,5],[2,2,12],[3,3,3],[7,8,7],[5,8,7]])
    A4 = np.array([[1,31,5,6],[2,2,2,1],[3,13,5,6],[7,18,7,6],[5,8,7,2]])
    for a in [A1,A2,A3,A4]:  # Show arrays
        print(a)
    for a in [A1,A2,A3,A4]:  # Show results
        print(sorted_rows(a))    
    #[0, 1, 2]
    #[0, 2, 3]
    #[0, 1, 2]
    #[]
    
    
    print('================ Question 5 ===============')
    L5 =[11, 6, 7, 16, 2, 4, 14, 8, 15, 1,  13,0]
    T = bst.BST()
    for a in L5:
        T.insert(a)
    T.draw()
    print(in_leaves(T.root))   # [0, 4, 8, 13, 15]
    
    
    
    print('================ Question 6 ===============')
    T = btree.BTree()
    L7 = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for n in L7:
        T.insert(n) 
    T.draw()
    print(internal(T.root)) # [6, 11, 17, 23, 27]
    
    
    print('================ Question 7 ===============')
    S = [1,2,3,4,6,7]
    for i in range(15):
        print(i,find_sum_pair(S,i))
        
    #0 None
    #1 None
    #2 None
    #3 [1, 2]
    #4 [1, 3]
    #5 [2, 3]
    #6 [2, 4]
    #7 [3, 4]
    #8 [2, 6]
    #9 [3, 6]
    #10 [4, 6]
    #11 [4, 7]
    #12 None
    #13 [6, 7]
    #14 None    
    
    
    print('================ Question 8 ===============')
    g8 = graph_AM.Graph(5,directed=True)
    g8.insert_edge(0,1)
    g8.insert_edge(1,2)
    g8.insert_edge(1,3)    
    g8.insert_edge(0,3)
    g8.insert_edge(2,3)
    g8.insert_edge(3,4)
    g8.insert_edge(2,4)
    g8.display()
    g8.draw('Hey 1')
    make_undirected(g8)
    g8.display()
    g8.draw('Hey 2')
    
    #Graph representation
    #directed: False, weighted: False
    #Adjacency matrix:
    #[[-1  1 -1  1 -1]
    # [ 1 -1  1  1 -1]
    # [-1  1 -1  1  1]
    # [ 1  1  1 -1  1]
    # [-1 -1  1  1 -1]]
              
    
    print('================ Question 9 ===============')
    g9 = graph_AL.Graph(6,directed=True)
    g9.insert_edge(1,0)
    g9.insert_edge(1,2)
    g9.insert_edge(1,3)    
    g9.insert_edge(0,3)
    g9.insert_edge(2,3)
    g9.insert_edge(3,4)
    g9.insert_edge(2,4)
    g9.insert_edge(5,4)
    g9.display()
    g9.draw()
    make_weighted(g9)
    g9.display()
    g9.draw()
    
    #Graph representation
    #directed: True, weighted: True
    #Adjacency list:
    #al[0]=[(3,3)]
    #al[1]=[(0,1)(2,3)(3,4)]
    #al[2]=[(3,5)(4,6)]
    #al[3]=[(4,7)]
    #al[4]=[]
    #al[5]=[(4,9)] 
    
    
    print('================ Question 10 ===============')
    S = [11,7,3,2]
    for i in range(sum(S)+2):
        print('S=',S,'goal=',i,'is there a solution: ',subsetsum_v2(S,i,sum(S)))
        
    #S= [11, 7, 3, 2] goal= 0 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 1 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 2 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 3 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 4 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 5 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 6 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 7 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 8 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 9 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 10 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 11 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 12 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 13 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 14 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 15 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 16 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 17 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 18 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 19 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 20 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 21 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 22 is there a solution:  False
    #S= [11, 7, 3, 2] goal= 23 is there a solution:  True
    #S= [11, 7, 3, 2] goal= 24 is there a solution:  False