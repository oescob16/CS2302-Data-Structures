#   Course: CS 2302
#   Assignment: Lab VI
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 04/27/2020
#   Purpose of the Program: To implement two algorithms to identify 
#   the most influential node.

import numpy as np
import matplotlib.pyplot as plt
import math
import random
import graph_AL as AL
import graph_AM as AM

#%% Creation of Graphs in AL and AM
    
def build_graphAM():
    g_am = AM.Graph(4039) 
    f = open('facebook_combined.txt','r')
    for line in f: # Iterates until there is no line left to read
        v = line.split(' ') # Array of size 2 containing source and dest
        g_am.insert_edge(int(v[0]),int(v[1]))
    f.close()
    return g_am
    
def build_graphAL():
    g_al = AL.Graph(4039)
    f = open('facebook_combined.txt','r')  
    for line in f: # Iterates until there is no line left to read in the document
        v = line.split(' ') # Array of size 2 containing source and dest
        g_al.insert_edge(int(v[0]),int(v[1]))
    f.close()
    return g_al


#%% Random Walk Algorithm Section
    
def neighbors(E):
    L = []
    for i in E:
        L.append(i.dest) # Appends neighbors
    return L 

def random_walk(G,steps=1000): 
    v = random.randint(0,len(G.al)) # Picks a random vertex
    visited = [0] * len(G.al) # Contains how many times have we visit vertex v
    for i in range(steps): 
        visited[v] += 1 # Vertex v has been visited
        N = neighbors(G.al[v])
        if len(N) == 0: # Vertex v has no neighbors
            N = np.arange(0,len(G.al)) # List that contains all V in G
        u = random.choice(N) # Randomly choose a neighbor
        v = u # We change vertex v to be neighbor u, this to traverse the graph
    p = np.divide(visited,steps) 
    return p # Returns a list of probabilities that we will visit i.

def get_info_rw(p):
    return np.argmax(p),np.amax(p) # Returns the largest value and its index.

def remove_influence_rw(G,v):
    while len(G.al[v]) != 0:
        G.delete_edge(v,G.al[v][0].dest) # Deletes neighbors from Vimp to remove influence


#%% Iterative Algorithm Section
    
def out_degrees(G):
    return list(np.sum(G.am>-1,axis=1))
        
def transition_matrix(G):
    size = len(G.am)
    T = np.zeros((size,size),dtype=np.float64) # Matrix that contains zeros of size 4039x4039
    out = out_degrees(G) 
    for i in range(G.am.shape[0]):
        for j in range(G.am.shape[1]):
            if out[i] == 0: # Vertex i has no neighbors and influence
                T[i,j] = 1/size
            elif G.am[i,j] != -1: # There is an edge going from i to j
                T[i,j] = 1/out[i]
            else: # There is no edge going from i to j
                T[i,j] = 0
    return T # Returns a matrix of probabilities that vertex i will go to vertex j
    
def iterative_p(G,convergence=1000):
    size = len(G.am)
    p = np.array(size*[1/size]) # List that contains the initial probability of all v's in V
    T = transition_matrix(G) # Matrix containing probabilities of going from vertex i to vertex j
    for i in range(convergence): # Iterates until the probablities ov visiting vertex i are exact
        p = np.dot(p,T)
    return p
    
def get_info_ip(p):
    return np.argmax(p),round(np.amax(p),5) # Returns the largest value and its index

def remove_influence_ip(G,v):
    for i in range(G.am.shape[1]):
        if G.am[v][i] != -1:
            G.delete_edge(v,i) # Deletes neighbors/influence from Vimp
    
    
#%% Main Method
if __name__ == "__main__":
    
    plt.close("all")
    
    g_al = build_graphAL()
    g_am = build_graphAM()
    
    print('\nUsing random walk method and adjacency list representation')
    for i in range(10):
        p = random_walk(g_al) 
        V_imp,val = get_info_rw(p) 
        print('Iteration {} most important vertex: {}, with p = {}'.format(i+1,V_imp,val))
        remove_influence_rw(g_al,V_imp)
    
    print('\nUsing iterative method and adjacency matrix representation')
    for i in range(10):
        p = iterative_p(g_am) 
        V_imp,val = get_info_ip(p)
        print('Iteration {} most important vertex: {}, with p = {}'.format(i+1,V_imp,val))
        remove_influence_ip(g_am,V_imp)
    
    

    
    
    
    