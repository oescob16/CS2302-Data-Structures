import numpy as np
from math import *
import time

def quicksort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def quicksort_random(x):
    if len(x) < 2:
        return x
    else:
        rand_index = np.random.randint(len(x))
        x[0],x[rand_index] = x[rand_index],x[0] 
        pivot = x[0]
        less = [i for i in x[1:] if i <= pivot]
        greater = [i for i in x[1:] if i > pivot]
        return quicksort_random(less) + [pivot] + quicksort_random(greater)
    
def are_equal_int(f,g):
    x = np.random.randint(100)
    f_n = eval(f)
    g_n = eval(g)
    return np.isclose(f_n,g_n)

def are_equal_trig(f,g):
    t = np.random.randint(100)
    f_t = eval(f)
    g_t = eval(g)
    return np.isclose(f_t,g_t)
    
if __name__ == "__main__":  
    n= 1000
    L = list(np.arange(n))  # Sorted list
    start = time.time()
    Ls1 = quicksort(L)
    end = time.time()
    print('running time with sorted list input:{:6.3f} seconds'.format(end-start))
    #print(Ls1)   # Uncomment for debugging. Both sorting algorithms must produce the same results
    
    L = list(np.random.randint(0,n,n))
    start = time.time() 
    Ls2 = quicksort(L)
    end = time.time()
    print('running time with random list input:{:6.3f} seconds'.format(end-start))
    #print(Ls2)   # Uncomment for debugging. Both sorting algorithms must produce the same results

    L = list(np.arange(n))  # Sorted list
    start = time.time()
    Ls1 = quicksort_random(L)
    end = time.time()
    print('running time with sorted list input:{:6.3f} seconds'.format(end-start))
    #print(Ls1)   # Uncomment for debugging. Both sorting algorithms must produce the same results

    L = list(np.random.randint(0,n,n))
    start = time.time()
    Ls2 = quicksort_random(L)
    end = time.time()
    print('running time with random list input:{:6.3f} seconds'.format(end-start))
    #print(Ls2)   # Uncomment for debugging. Both sorting algorithms must produce the same results
    
    f1 = 'x*x + x - 12'
    f2 = '(x+4)*(x-3)'
    f3 = '(x+4)*(x+3)'
    f4 = 'sin(t)**2 + cos(t)**2 - 1'
    f5 = 'sin(t)*(1/cos(t) + 1/sin(t))'
    f6 = 'tan(t)+1'
    
    for i in range(5):
        x = np.random.randint(100)
        y1 = eval(f1)
        y2 = eval(f2)
        y3 = eval(f3)
        print()
        print('function: y = {}; x = {}; y= {} '.format(f1,x,y1))
        print('function: y = {}; x = {}; y= {} '.format(f2,x,y2))
        print('function: y = {}; x = {}; y= {} '.format(f3,x,y3))
          
    print()
    print(are_equal_int(f1,f2)) # True
    print(are_equal_int(f2,f3)) # False
    print(are_equal_int(f1,f3)) # False
    
    for i in range(5):
        t = np.random.rand()*2*pi  
        y4 = eval(f4)
        y5 = eval(f5)
        y6 = eval(f6)
        print()
        print('function: y = {}; t = {}; y = {} '.format(f4,t,y4))
        print('function: y = {}; t = {}; y = {} '.format(f5,t,y5))
        print('function: y = {}; t = {}; y = {} '.format(f6,t,y6))
    
    print()
    print(are_equal_int(f4,f5)) # False
    print(are_equal_int(f5,f6)) # True
    print(are_equal_int(f4,f6)) # False
 