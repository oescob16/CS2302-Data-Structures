#   Course: CS 2302
#   Assignment: Lab VII
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 05/11/2020
#   Purpose of the Program: To implement three different algorithms
#   to solve the knapsack problem. 

import numpy as np
import random

def knapsack_bt(W,D,v,w):
# W is the remaining knapsack capacity, D is the remaining debt, v and w are lists of the
# same length where item 0 has value v[0] and weight w[0], item 1 has value v[1] and
# weight w[1], and so on.
    if len(v) <= 0 or len(w) <= 0:
        return False
    if D <= 0: # debt paid
        return True
    if W <= 0: # knapsack capacity exceeded
        return False 
    return knapsack_bt(W-w[0],D-v[0],v[1:],w[1:]) or knapsack_bt(W,D,v[1:],w[1:])
    
def knapsack_g(W,D,v,w):  
    ratio = [ [v[i]/w[i],v[i],w[i]] for i in range(len(v))] # List that contains [Ratio (v[i]/w[i]), Value, Weight]
    vwr = sorted(ratio,reverse=True) # Sort in descending order
    #knapsack = [] # List that contains value[i] of item[i]
    for i in range(len(vwr)):
        weight = vwr[i][2]
        value = vwr[i][1]
        if W >= weight: # Add item to the knapsack if there is still room in W
            #knapsack.append(value)
            W -= weight # Decrease room of W
            D -= value # Decrease debt of D
    if D <= 0: # Debt paid
        return True
    return False

def knapsack_r(W,D,v,w,attempts=50000):
    items = [ [v[i],w[i]] for i in range(len(v))]
    for i in range(attempts):
        random.shuffle(items) # Randomly sort the items
        #knapsack = []
        Dc = D # Copy the value of D
        Wc = W # Copy the value of W
        for j in range(len(items)):
            weight = items[j][1]
            value = items[j][0]
            if Wc >= weight: # Add item to the knapsack if there is still room in W
                #knapsack.append(value)
                Wc -= weight # Decrease room of W
                Dc -= value # Decrease debt of D
            if Dc <= 0: # Debt paid
                return True
    return False
    
if __name__ == "__main__":
    
    # Sample knapsack datasets
    print('~~~~~~~~~ Problem 1 ~~~~~~~~~~~~~~')
    W = 35
    D = 270
    w = [10,  6, 10,  6, 14,  8,  5, 13,  4,  1]
    v = [39, 47, 47, 29, 71, 22, 50, 29, 51, 20]
    print('W is: ',W)
    print('w is: ',sum(w))
    print('D is: ',D)
    print('v is: ',sum(v))
    print('Backtracking --> ',knapsack_bt(W,D,v,w))
    print('Greedy --> ',knapsack_g(W,D,v,w))
    print('Random -->',knapsack_r(W,D,v,w))
    
    print('~~~~~~~~~ Problem 2 ~~~~~~~~~~~~~~')
    W =  10
    D = 130
    w = [10,  6, 10,  6, 14,  8,  5, 13,  4,  1]
    v = [39, 47, 47, 29, 71, 22, 50, 29, 51, 20]
    print('W is: ',W)
    print('w is: ',sum(w))
    print('D is: ',D)
    print('v is: ',sum(v))
    print('Backtracking --> ',knapsack_bt(W,D,v,w))
    print('Greedy --> ',knapsack_g(W,D,v,w))
    print('Random -->',knapsack_r(W,D,v,w))

    print('~~~~~~~~~ Problem 3 ~~~~~~~~~~~~~~')
    W = 102
    D = 404
    w = [10,  8,  5,  6,  9, 13, 13, 14, 13, 14,  6, 11, 12,  5, 13, 11,  9,
           10, 14,  9]
    v = [47, 15,  7, 17, 29, 12, 45, 24, 26, 10, 37, 38, 14, 35, 44, 37, 27,
           45, 36, 40]
    print('W is: ',W)
    print('w is: ',sum(w))
    print('D is: ',D)
    print('v is: ',sum(v))
    print('Backtracking --> ',knapsack_bt(W,D,v,w))
    print('Greedy --> ',knapsack_g(W,D,v,w))
    print('Random -->',knapsack_r(W,D,v,w))

    print('~~~~~~~~~ Problem 4 ~~~~~~~~~~~~~~')
    W = 150
    D = 600
    w = [10, 14,  4,  5,  8, 12,  5,  7,  7, 11,  9,  5, 10, 14,  4,  4, 14,
            7,  8,  9]
    v = [39, 49, 47, 40, 20, 27, 31, 34, 17, 10, 29, 36, 41, 48, 45, 24, 15,
           17, 14, 40]
    print('W is: ',W)
    print('w is: ',sum(w))
    print('D is: ',D)
    print('v is: ',sum(v))
    print('Backtracking --> ',knapsack_bt(W,D,v,w))
    print('Greedy --> ',knapsack_g(W,D,v,w))
    print('Random -->',knapsack_r(W,D,v,w))

    print('~~~~~~~~~ Problem 5 ~~~~~~~~~~~~~~')
    W = 200
    D = 960
    w = [ 8, 13, 13,  9,  5, 14, 13,  4,  8,  7, 13,  8, 12,  9, 13,  8,  5,
            9,  5,  7,  4,  7, 13, 13,  6,  8,  4,  5,  9, 10,  5,  4,  6, 10,
            7,  9, 13, 14, 12,  5, 10,  7,  9, 12,  9, 10,  5,  8, 11,  9]
    v = [21, 26, 25, 23, 42, 32, 45, 33, 40, 20, 44, 13,  9, 31, 47, 21, 31,
           18, 41, 36, 32, 43, 20, 40, 23, 16, 10, 44, 38,  6, 11, 13, 43,  7,
           35, 21,  7, 25, 47, 34, 33, 46, 26, 17, 23, 28, 42, 16, 28, 30]
    print('W is: ',W)
    print('w is: ',sum(w))
    print('D is: ',D)
    print('v is: ',sum(v))
    #print('Backtracking --> ',knapsack_bt(W,D,v,w))
    print('Greedy --> ',knapsack_g(W,D,v,w))
    print('Random -->',knapsack_r(W,D,v,w))
    
    
    
    
    
    
