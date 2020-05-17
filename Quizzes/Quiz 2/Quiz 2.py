import numpy as np
import matplotlib.pyplot as plt
import math

def set_drawing_parameters_and_show(ax):
    show_axis = 'on'
    show_grid = 'True'
    ax.set_aspect(1.0)
    ax.axis(show_axis)
    plt.grid(show_grid)
    plt.show()

def nested_squares(ax,n,x0,y0,size):
    if n>0:
        ax.plot([0],[0],linewidth=1.0,color='b') 
        x_coordinates = [x0-size,0,x0+size,0,x0-size]
        y_coordinates = [0,y0+size,0,y0-size,0]
        ax.plot(x_coordinates,y_coordinates,linewidth=1.0,color='b') 
        nested_squares(ax,n-1,x0,y0,size/2)

def x_array(n):
    D = np.zeros((n,n),dtype=int)
    for i in range(len(D)):
        D[i][i] = 1
        D[i][len(D)-1-i] = 1
    return D

def remove_i(L,i):
    if len(L) == 0:
        return []
    if L[0] == i:
        return remove_i(L[1:],i)
    return [L[0]] + remove_i(L[1:],i)

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    fig, ax = plt.subplots()
    
    print(x_array(3))
    # =============================================================================
    #  [[1 0 1]
    #  [0 1 0]
    #  [1 0 1]]
    # =============================================================================

    print(x_array(4))
    # =============================================================================   
    # [[1 0 0 1]
    #  [0 1 1 0]
    #  [0 1 1 0]
    #  [1 0 0 1]]    
    # =============================================================================
    
    L = [3,1,4,6,7,8,9,3,6,2,1,4,5,6]
    print(remove_i(L,3))  # [1, 4, 6, 7, 8, 9, 6, 2, 1, 4, 5, 6]
    print(remove_i(L,6))  # [3, 1, 4, 7, 8, 9, 3, 2, 1, 4, 5]
    print(remove_i(L,10)) # [3, 1, 4, 6, 7, 8, 9, 3, 6, 2, 1, 4, 5, 6]
    
    nested_squares(ax,4,0,0,100)
    set_drawing_parameters_and_show(ax)
    fig.savefig('escobedo_oswaldo_quiz2.png')



