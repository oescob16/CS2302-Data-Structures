import graph_AL 
import graph_AM
import dsf
import matplotlib.pyplot as plt
import numpy as np
import math

def count_sinks(G):
    count = 0
    for i in G.al:
        if len(i) == 0:
            count += 1 
    return count
    
def first_kruskal(G):
    first_edge = [None,None,math.inf]
    for i in range(len(G.al)):
        for j in G.al[i]:
            if j.weight < first_edge[2]:
                first_edge = [i,j.dest,j.weight]  
    return first_edge       
        
def graph_from_prev(prev):
    g = graph_AM.Graph(len(prev),directed=True)
    for i in range(g.am.shape[0]):
        if prev[i] != -1:
            g.insert_edge(prev[i],i)
    return g

def num_sets(s):
    return len(s.set_list()) 

def subsetsum_with_negatives(S,goal): 
    # Determines if there is a subset of S that adds up to g, where elements of S are positive integers
    # Return the subset that adds up to g if it exists or None if no such subset exists
    if goal ==0:
        return []
    if len(S)==0:
        return None # There is no solution
    subset = subsetsum_with_negatives(S[1:],goal-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else:   # There is no solution when taking S[0], try leaving S[0]
        return subsetsum_with_negatives(S[1:],goal) # Don't take S[0]

def min_coins_greedy(C,D):
    # Assumes D is sorted on descending order
    # Max contains the Maximum number of coins of each denomination available (i.e. Max[i] is the number of coins with denominationD[i] that are available)
    count = np.zeros(len(D),dtype=int) 
    # count[i] is the number of coins of value D[i] we must give
    for i in range(len(D)):
        count[i] = C//D[i] # Number of coins of value D[i] that fit in C
        C = C - count[i]*D[i]  # Remaining debt
    if C == 0:
        return count
    return -1 # No solution found

def min_coins_greedy_with_max(C,D,Max):
    # Assumes D is sorted on descending order
    # Max contains the Maximum number of coins of each denomination available (i.e. Max[i] is the number of coins with denominationD[i] that are available)
    count = np.zeros(len(D),dtype=int) 
    # count[i] is the number of coins of value D[i] we must give
    for i in range(len(D)):
        count[i] = C//D[i] # Number of coins of value D[i] that fit in C
        if count[i]>Max[i]: # Check to see if coins are available
            count[i]=Max[i]
        C = C - count[i]*D[i] # Remaining debt  
    if C == 0:
        return count
    return -1 # No solution found

if __name__ == "__main__":   
    
    plt.close("all")   
    
    print('\n *********** Question 1 **************')
    g = graph_AL.Graph(6,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,5)
    g.insert_edge(2,5)
    g.display()
    g.draw('Question 1')
    print(count_sinks(g))  # 2
    

    print('\n *********** Question 2 **************')
    g = graph_AL.Graph(5,weighted=True)
    g.insert_edge(0,1,2)
    g.insert_edge(1,2,1)
    g.insert_edge(2,3,6)
    g.insert_edge(3,4,3)
    g.insert_edge(4,0,4)
    g.insert_edge(3,0,5)
    g.display()
    g.draw('Question 2')
    print(first_kruskal(g))    # [1, 2, 1]
    

    print('\n *********** Question 3 **************')
    prev = [-1, 4, 0, 2, 0]
    g = graph_from_prev(prev)
    g.display()
#    Graph representation
#    directed: True, weighted: False
#    Adjacency matrix:
#    [[-1 -1  1 -1  1]
#     [-1 -1 -1 -1 -1]
#     [-1 -1 -1  1 -1]
#     [-1 -1 -1 -1 -1]
#     [-1  1 -1 -1 -1]]
    g.draw('Question 3') 
    
    print('\n *********** Question 4 **************')
    s = dsf.DSF(8)
    s.union(0,1)
    s.union(7,2)
    s.union(3,5)
    s.union(1,5)
    s.union(6,2)
    print(s.parent)
    s.draw('Question 4')
    print(s.set_list())
    print(num_sets(s)) # 3
    
    print('\n *********** Question 5 **************')
    mySet =[-2,5,-7,-9,4]
    for i in range(-10,11):
        print('goal:',i,'solution:',subsetsum_with_negatives(mySet,i))
        
#    goal: -10 solution: None
#    goal: -9 solution: [-2, 5, -7, -9, 4]
#    goal: -8 solution: None
#    goal: -7 solution: [-2, -9, 4]
#    goal: -6 solution: [-2, 5, -9]
#    goal: -5 solution: [-2, -7, 4]
#    goal: -4 solution: [-2, 5, -7]
#    goal: -3 solution: [-7, 4]
#    goal: -2 solution: [-2]
#    goal: -1 solution: None
#    goal: 0 solution: []
#    goal: 1 solution: None
#    goal: 2 solution: [-2, 4]
#    goal: 3 solution: [-2, 5]
#    goal: 4 solution: [4]
#    goal: 5 solution: [5]
#    goal: 6 solution: None
#    goal: 7 solution: [-2, 5, 4]
#    goal: 8 solution: None
#    goal: 9 solution: [5, 4]
#    goal: 10 solution: None    
        
    print('\n *********** Question 6 **************')
    D = [25,10,5,1]
    Max = [1,2,3,100]
    print(min_coins_greedy_with_max(85,D,[1,2,3,100]))   # [ 1  2  3 25]
    print(min_coins_greedy_with_max(85,D,[10,10,10,10])) # [3 1 0 0]
    print(min_coins_greedy_with_max(48,D,[1,1,3,100]))   # [1 1 2 3]
    print(min_coins_greedy_with_max(48,D,[0,10,3,100]))  # [0 4 1 3]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    