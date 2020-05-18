import numpy as np

def subsetsum(S,goal):
    if goal == 0:
        return []
    if goal<0 or len(S)==0:
        return None # There is no solution
    subset = subsetsum(S[1:],goal-S[0]) # Take S[0]
    if subset != None: # There is a solution when taking S[0]
        return [S[0]] + subset
    else: # There is no solution when taking S[0], try leaving S[0]
        return subsetsum(S[1:],goal) # Don't take S[0]

# Problem 4
def partition_problem(S):
    setsum = sum(S)
    if setsum % 2 != 0:
        return None
    goal = setsum/2 
    S1 = subsetsum(S,goal)
    if S1 is not None:
        S2 = S.copy()
        for i in S1:
            S2.remove(i)
        return S1,S2

# Problem 5
def edit_distance5(s1,s2):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1) # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1) # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]: # Match
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1], # Insert
                                 d[i+1,j]) # Delete 
    return d

# Problem 6
def edit_distance6(s1,s2):
    d = np.zeros((len(s1)+1,len(s2)+1),dtype=int)
    d[-1,:] = len(s2)-np.arange(len(s2)+1) # Fill out last row
    d[:,-1] = len(s1)-np.arange(len(s1)+1) # Fill out last column
    for i in range(len(s1)-1,-1,-1):
        for j in range(len(s2)-1,-1,-1):
            if s1[i] ==s2[j]: # Match
                d[i,j] =d[i+1,j+1]
            else:
                d[i,j] = 1 + min(d[i,j+1]+2, # Insert
                                 d[i+1,j+1]+3, # Replace
                                 d[i+1,j]+2) # Delete
    return d       

if __name__ == "__main__": 
    
    print('\nProblem 4')
    print(partition_problem([0,1,2,3])) # ([0, 1, 2], [3])
    print(partition_problem([1,2,3,4,6])) # ([1, 3, 4], [2, 6])
    print(partition_problem([1,5,11,5])) # ([1, 5, 5], [11])
    print(partition_problem([1,1,1,6,3])) # ([1, 1, 1, 3], [6])
    print(partition_problem([2,1,8,3])) # None
     
    print('\nProblem 5')
    print(edit_distance5('WHALES','WASH'),'\n') 
    print(edit_distance5('MINER','ONLINE'))
    
    
    print('\nProblem 6')
    print(edit_distance6('WHALES','WASH'),'\n') 
    print(edit_distance6('MINER','ONLINE'))
            