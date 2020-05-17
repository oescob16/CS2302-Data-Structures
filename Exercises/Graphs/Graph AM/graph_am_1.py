import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as graphAL
import graph_AM as graphAM

#Question 1
def num_vertices(G):
    return len(G.am)

#Question 2
def count_edges(G):
    edges = 0
    for v in range(G.am.shape[0]):
        for e in range(G.am.shape[1]):
            if G.am[v][e] != -1:
                edges += 1
    if not G.directed:
        return edges//2
    return edges

#Question 3
def highest_weight_edge(G):
    biggest = [0,0,-math.inf]
    for v in range(G.am.shape[0]):
        for e in range(G.am.shape[1]):
            if G.am[v][e] > biggest[2]:
                biggest[0] = v
                biggest[1] = e
                biggest[2] = G.am[v][e]
    return biggest

#Question 4
def out_degrees(G):
    L = [0 for i in range(G.am.shape[0])]
    for v in range(G.am.shape[0]):
        for e in range(G.am.shape[1]):
            if G.am[v][e] != -1:
                L[v] += 1
    return L

#Question 5
def in_degrees(G):
    L = [0 for i in range(G.am.shape[0])]
    for v in range(G.am.shape[0]):
        for e in range(G.am.shape[1]):
            if G.am[v][e] != -1:
                L[e] += 1
    return L

#Question 6
def reverse_edges(G):
    if not G.directed:
        return
    G.am = np.flip(np.rot90(G.am,1),0)
    return 

#Question 7
def al_to_am(g_al):
    g_am = graphAM.Graph(len(g_al.al),directed=g_al.directed,weighted=g_al.weighted)
    for v in range(len(g_al.al)):
        for e in g_al.al[v]:
            g_am.insert_edge(v,e.dest,e.weight)
    return g_am
            
#Question 8
def am_to_al(g_am):
    g_al = graphAL.Graph(g_am.am.shape[0],directed=g_am.directed,weighted=g_am.weighted)
    for v in range(g_am.am.shape[0]):
        for e in range(g_am.am.shape[1]):
            w = g_am.am[v][e]
            if w != -1 and v < e:
                g_al.insert_edge(v,e,w)
    return g_al
                 
if __name__ == "__main__":   
    plt.close("all")   
    g_uduw =graphAM.Graph(5)
    g_uduw.insert_edge(0,1)
    g_uduw.insert_edge(0,2)
    g_uduw.insert_edge(1,2)
    g_uduw.insert_edge(2,3)
    g_uduw.insert_edge(3,4)
    g_uduw.insert_edge(4,1)
    g_uduw.display()
    g_uduw.draw()
    
    g_duw = graphAM.Graph(5,directed = True)
    g_duw.insert_edge(0,1)
    g_duw.insert_edge(0,2)
    g_duw.insert_edge(1,2)
    g_duw.insert_edge(2,3)
    g_duw.insert_edge(3,4)
    g_duw.insert_edge(4,1)
    g_duw.display()
    g_duw.draw()
    
    g_udw = graphAM.Graph(6, weighted=True)
    g_udw.insert_edge(0,1,4)
    g_udw.insert_edge(0,2,3)
    g_udw.insert_edge(1,2,2)
    g_udw.insert_edge(2,3,1)
    g_udw.insert_edge(3,4,5)
    g_udw.insert_edge(4,1,4)
    g_udw.insert_edge(5,0,6)
    g_udw.display()
    g_udw.draw()
    
    g_dw = graphAM.Graph(6,directed = True, weighted=True)
    g_dw.insert_edge(0,1,4)
    g_dw.insert_edge(0,2,3)
    g_dw.insert_edge(1,2,2)
    g_dw.insert_edge(2,3,1)
    g_dw.insert_edge(3,4,5)
    g_dw.insert_edge(4,1,4)
    g_dw.insert_edge(5,0,6)
    g_dw.display()
    g_dw.draw()
    
    print('Question 1')
    print("Vertices: ",num_vertices(g_uduw))  # 5
    print("Vertices: ",num_vertices(g_duw))   # 5
    print("Vertices: ",num_vertices(g_udw))   # 6
    print("Vertices: ",num_vertices(g_dw))    # 6
    
    print('Question 2')
    print("Edges: ",count_edges(g_uduw))  # 6
    print("Edges: ",count_edges(g_duw))   # 6
    print("Edges: ",count_edges(g_udw))   # 7
    print("Edges: ",count_edges(g_dw))    # 7
    
    print('Question 3')
    print("Highest weight edge: ",highest_weight_edge(g_uduw))  # [0, 1, 1]
    print("Highest weight edge: ",highest_weight_edge(g_duw))   # [0, 1, 1]
    print("Highest weight edge: ",highest_weight_edge(g_udw))   # [0, 5, 6]
    print("Highest weight edge: ",highest_weight_edge(g_dw))    # [3, 4, 5]
    
    print('Question 4')
    print("Out degrees: ",out_degrees(g_uduw))  # [2, 3, 3, 2, 2]
    print("Out degrees: ",out_degrees(g_duw))   # [2, 1, 1, 1, 1]
    print("Out degrees: ",out_degrees(g_udw))   # [3, 3, 3, 2, 2, 1]
    print("Out degrees: ",out_degrees(g_dw))    # [2, 1, 1, 1, 1, 1]
    
    print('Question 5')
    print("In degrees: ",in_degrees(g_uduw))  # [2, 3, 3, 2, 2]
    print("In degrees: ",in_degrees(g_duw))   # [0, 2, 2, 1, 1]
    print("In degrees: ",in_degrees(g_udw))   # [3, 3, 3, 2, 2, 1]
    print("In degrees: ",in_degrees(g_dw))    # [1, 2, 2, 1, 1, 0]

    print('Question 6')
    reverse_edges(g_duw)
    g_duw.display()
    g_duw.draw()
    #Graph representation
    #directed: True, weighted: False
    #Adjacency matrix:
    #[[-1 -1 -1 -1 -1]
    # [ 1 -1 -1 -1  1]
    # [ 1  1 -1 -1 -1]
    # [-1 -1  1 -1 -1]
    # [-1 -1 -1  1 -1]]
    
    reverse_edges(g_dw)
    g_dw.display()
    g_dw.draw()
    #Graph representation
    #directed: True, weighted: True
    #Adjacency matrix:
    #[[-1 -1 -1 -1 -1  6]
    # [ 4 -1 -1 -1  4 -1]
    # [ 3  2 -1 -1 -1 -1]
    # [-1 -1  1 -1 -1 -1]
    # [-1 -1 -1  5 -1 -1]
    # [-1 -1 -1 -1 -1 -1]]    

    
    g = graphAL.Graph(5,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,0)
    g.display()
    g.draw()
    
    print('Question 7')
    gm = al_to_am(g)
    gm.display()
    gm.draw()
    
    #Graph representation
    #directed: True, weighted: False
    #Adjacency matrix:
    #[[-1  1 -1 -1 -1]
    # [-1 -1  1 -1 -1]
    # [-1 -1 -1  1 -1]
    # [-1 -1 -1 -1  1]
    # [ 1 -1 -1 -1 -1]]
    
    print('Question 8')
    g_udw.display()
    gl = am_to_al(g_udw)
    gl.display()
    gl.draw()
    
    #Graph representation
    #directed: False, weighted: True
    #Adjacency list:
    #al[0]=[(1,4)(2,3)(5,6)]
    #al[1]=[(0,4)(2,2)(4,4)]
    #al[2]=[(0,3)(1,2)(3,1)]
    #al[3]=[(2,1)(4,5)]
    #al[4]=[(1,4)(3,5)]
    #al[5]=[(0,6)]
    
    
    
