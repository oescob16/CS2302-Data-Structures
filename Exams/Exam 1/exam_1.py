import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def draw_circle(ax,center,rad):
    # Draws a circle in object ax given center and radius
    n = int(4*rad*math.pi)*2
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    ax.plot(x,y,linewidth=2.0,color='b')

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_circles(ax, n, x0, y0, r):
    if n > 0:
        draw_circle(ax,[x0,y0],r)
        nested_circles(ax, n-1, x0-(r*1.5), y0, r/2)
        nested_circles(ax, n-1, x0+(r*1.5), y0, r/2)

def multiples(L,k): 
    if len(L) == 0:
        return 0
    if L[0] % k == 0:
        return 1 + multiples(L[1:],k)
    else:
        return multiples(L[1:],k)

def first_plus_third(L):
    t = L.head
    if t is None:
        return 0
    if t.next is None or t.next.next is None:
        return t.data
    else:
        return t.data + t.next.next.data

def sll_to_list(L):
    if L.head is None:
        return []
    t = L.head 
    List = []
    while t is not None:
        List.append(t.data)
        t = t.next
    return List

def sum_non_edge(A):
    sum_l = 0
    for i in range(1,A.shape[0]-1):
        for j in range(1,A.shape[1]-1):
            sum_l += A[i][j]
    return sum_l

if __name__ == "__main__":

    print('Question 1')
    plt.close("all") # Close all figures
    fig, ax = plt.subplots()
    nested_circles(ax,2,0,0,100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('fig1.png')
    
    fig, ax = plt.subplots()
    nested_circles(ax,5,0,0,100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('fig2.png')
    
    L1 = [2,5,7,4,1,6]
    L2 = [2302]
    L3 = []
    
    print('Question 2')
    print(multiples(L1,2)) # 3 
    print(multiples(L1,3)) # 1
    print(multiples(L2,2)) # 1
    print(multiples(L3,3)) # 0
    
    L1 = sll.List()
    L2 = sll.List()
    L2.extend([2302])
    L3 = sll.List()
    L3.extend([2,302])
    L4 = sll.List()
    L4.extend([2,5,7,4,1,6])
    
    print('Question 3')
    print(first_plus_third(L1)) # 0
    print(first_plus_third(L2)) # 2302
    print(first_plus_third(L3)) # 2
    print(first_plus_third(L4)) # 9
    
    print('Question 4')
    print(sll_to_list(L1)) # []
    print(sll_to_list(L2)) # [2302]
    print(sll_to_list(L3)) # [2, 302]
    print(sll_to_list(L4)) # [2, 5, 7, 4, 1, 6]
    
    print('Question 5')
    A = np.arange(20).reshape((4,5))
    print(A)
    print(sum_non_edge(A)) # 57
   