import numpy as np
import matplotlib.pyplot as plt
import math
import singly_linked_list as sll

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid) 
    plt.show()

def nested_squares(ax,n,x0,y0,size):
    if n > 0:
        x = [x0-size,x0-size,x0+size,x0+size,x0-size]
        y = [y0-size,y0+size,y0+size,y0-size,y0-size]
        ax.plot(x,y,linewidth=2,color='b')
        nested_squares(ax,n-1,x0+size,y0,size/2)
        nested_squares(ax,n-1,x0-size,y0,size/2)

def list_n_to_0(n):
    if n == 0:
        return [0]
    return [n] + list_n_to_0(n-1)
    
def sum_first_n(L,n):
    t = L.head
    i = 0
    sum_list = 0
    while t is not None:
        if i >= n:
            break
        sum_list += t.data
        i += 1
        t = t.next
    return sum_list

def sum_until(L,i):
    t = L.head 
    sum_list = 0
    while t is not None:
        if i == t.data:
            break
        sum_list += t.data
        t = t.next
    return sum_list

def next_to_last(L):
    t = L.head
    while t is not None:
        if t.next.next is None:
            return t.data
        t = t.next
    return None

if __name__ == "__main__":

    plt.close("all") # Close all figures
    
    fig, ax = plt.subplots()
    nested_squares(ax,2,0,0,100)
    set_drawing_parameters_and_show(ax)
    
    fig2, ax2 = plt.subplots()
    nested_squares(ax2,5,0,0,100)
    set_drawing_parameters_and_show(ax2)
    
    print(list_n_to_0(0)) # [0]
    print(list_n_to_0(5)) # [5, 4, 3, 2, 1, 0]
    
    L= sll.List()
    L.extend([3,6,1,2,5])
    L.draw()
    
    print(sum_first_n(L,4))  # 12
    print(sum_first_n(L,10)) # 17
    
    print(sum_until(L,3))  # 0
    print(sum_until(L,1))  # 9
    print(sum_until(L,10)) # 17
    
    L1= sll.List()
    print(next_to_last(L1)) # None
    print(next_to_last(L))  # 2

