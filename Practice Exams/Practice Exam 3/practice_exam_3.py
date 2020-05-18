import matplotlib.pyplot as plt
import math
import numpy as np
import graph_AL 
import graph_AM
import dsf

def is_compressed(s):
    compressed = True
    for i in range(len(s.parent)):
        if s.parent[i]>=0 and s.parent[s.parent[i]]>=0:
            print('{} is not a root and its parent is not a root'.format(i))
            compressed = False
    return compressed

def three_layer_graph(a,b,c):
    g = graph_AL.Graph(a+b+c,directed=True)
    for i in range(a+b+c):
        if i < a:
            for j in range(a,a+b):
                g.insert_edge(i,j)
        elif i >= a and i < b+c:
            for j in range(a+b,a+b+c):
                g.insert_edge(i,j)
    return g 

def dist_from_prev(G,prev,v):
    d = 0
    while prev[v] != -1:
        d += G.am[prev[v],v]
        v = prev[v]
    return d

def in_degrees(G):
    L = [0 for i in range(G.am.shape[0])]
    for i in range(G.am.shape[0]):
        for j in range(G.am.shape[1]):
            if G.am[i,j] != -1:
                L[j] += 1
    return L
 
def compress(s):
    for i in range(len(s.parent)):
        if s.parent[i] != -1: 
            s.parent[i] = s.find(i)
    return s
        
def subsetsum_nr(S,goal): 
    stack = [[S,goal,[]]]
    while len(stack)>0:
        r= stack.pop()
        S,goal,selection = r[0],r[1],r[2]
        if goal==0:
            return selection
        if goal>0 and len(S)>0:
            stack.append([S[1:],goal-S[0],selection+[S[0]]])
            stack.append([S[1:],goal,selection])
    return None
            
def prime(n):
    for i in range(100):
        j = np.random.randint(2,n)
        if n%j == 0:
            return False
    return True
        
def edit_distance(s1,s2):
    # Finds edit distance from s1 to s2
    # If return_array is True it will return that array containing edit distances for all substrings of s1 and s2
    vowels = 'aeiouAEIOU'
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1)  # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1)  # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]:
                d[i,j] =d[i+1,j+1]
            else:
                if (s1[i] in vowels) == (s2[j] in vowels):
                    d[i,j] = 1 + min(d[i,j+1],d[i+1,j],d[i+1,j+1]) 
                else:
                    d[i,j] = 1 + min(d[i,j+1],d[i+1,j+1],d[i+1,j])
    return d

if __name__ == "__main__":   
    
    plt.close("all")   
    print('\n *********** Question 1 **************')
    g = three_layer_graph(3,2,3)
    g.display()
#    Graph representation
#    directed: True, weighted: False
#    Adjacency list:
#    al[0]=[(3,1)(4,1)]
#    al[1]=[(3,1)(4,1)]
#    al[2]=[(3,1)(4,1)]
#    al[3]=[(5,1)(6,1)(7,1)]
#    al[4]=[(5,1)(6,1)(7,1)]
#    al[5]=[]
#    al[6]=[]
#    al[7]=[]
       
    print('\n *********** Question 2 **************')
    g = graph_AM.Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,7)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(2,4,8)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    print(in_degrees(g))    # [0, 2, 2, 1, 2]
    g.draw()
   
    print('\n *********** Question 3 **************')
    prev = [-1, 0, 1, 2, 3]
    for v in range(5):
        print('dist to {} = {}'.format(v,dist_from_prev(g,prev,v)))
#    dist to 0 = 0
#    dist to 1 = 4
#    dist to 2 = 6
#    dist to 3 = 7
#    dist to 4 = 12
    
    print('\n *********** Question 4 **************')
    s = dsf.DSF(8)
    s.union(0,1)
    s.union(7,2)
    s.union(3,5)
    s.union(1,5)
    s.union(6,2)
    print(s.parent)
    print(is_compressed(s)) 
    s.draw()
    compress(s)
    print(s.parent)     # [-1  0  6  0 -1  0 -1  6]
    print(is_compressed(s)) # True
    s.draw()
    
    print('\n *********** Question 5 **************')
    mySet =[2,5,8,9,12,21,33]
	  
    goal_list = [7,15,16,20]
    #goal_list = [] # uncomment to prevent error
    for goal in goal_list:
        print('Goal:',goal,'  Solution:',subsetsum_nr(mySet,goal))
#    Goal: 7   Solution: [2, 5]
#    Goal: 15   Solution: [2, 5, 8]
#    Goal: 16   Solution: [2, 5, 9]
#    Goal: 20   Solution: [8, 12]
    
    print('\n *********** Question 6 **************')
    np.random.seed(seed=1)
    
    print(prime(11))  # True
    print(prime(20))  # False
    print(prime(29))  # True
    print(prime(32))  # False
    
    print('\n *********** Question 7 **************')
    s1,s2 = 'MINER','MONEY'
    d = edit_distance(s1,s2)
    
    print('edit_distance({},{})={}'.format(s1,s2,d[0,0]))   # edit_distance(MINER,MONEY)=2
    print('Distance matrix\n')
    print(d)
    
#    Distance matrix
#    
#    [[2 3 3 4 5 5]
#     [3 2 2 3 4 4]
#     [3 2 1 2 3 3]
#     [4 3 2 1 2 2]
#     [5 4 3 2 1 1]
#     [5 4 3 2 1 0]]