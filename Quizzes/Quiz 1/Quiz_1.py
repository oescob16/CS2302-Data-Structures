import numpy as np

def replace(S,a,b):
    #Your code goes here
    s = ''
    for i in range(len(S)):
        if S[i] == a:
            s += b
        else: 
            s += S[i]
    return s

def divisors(n):
    #Your code goes here
    divisors = []
    for i in range(1,n+1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def set_largest_to_zero(A):
    #Your code goes here
    max = A[0][0]
    row = 0
    col = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] > max:
                max = A[i][j]
                row = i
                col = j
    A[row][col] = 0
    return A

if __name__ == "__main__":  
      
    S = replace('data structures', 'a', 's')
    print(S)    # dsts structures
        
    d = divisors(20)
    print(d)   #  [1, 2, 4, 5, 10, 20]
    d = divisors(23)
    print(d)   #  [1, 23]
    
    L = [1, 5, 8, 7, 9, 3, 0, 4, 2, 6]  
    A = np.array(L).reshape(2,5) 
    print(A)   
    set_largest_to_zero(A)
    print(A)
    ''' 
    Output: 
    [[1 5 8 7 0]
     [3 0 4 2 6]] 
    '''
    
    
    
