#   Course: CS 2302
#   Assignment: Lab I
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 01/31/2020
#   Purpose of the Program: to practice and 
#   use recursion to draw fractal figures

import numpy as np
import matplotlib.pyplot as plt
import math

def circle(center,rad):
    # Returns the coordinates of the points in a circle given center and radius
    n = int(4*rad*math.pi)
    t = np.linspace(0,6.3,n)
    x = center[0]+rad*np.sin(t)
    y = center[1]+rad*np.cos(t)
    return x,y

def draw_squares(ax,n,p,w):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k') # Draw rectangle
        i1 = [1,2,3,0,1]
        q = p*(1-w) + p[i1]*w
        draw_squares(ax,n-1,q,w)

def draw_four_circles(ax,n,center,radius):
    if n>0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_four_circles(ax,n-1,[center[0],center[1]+radius],radius/2)
        draw_four_circles(ax,n-1,[center[0],center[1]-radius],radius/2)
        draw_four_circles(ax,n-1,[center[0]+radius,center[1]],radius/2)
        draw_four_circles(ax,n-1,[center[0]-radius,center[1]],radius/2)

'''   Figure No. 1   '''

def draw_inside_circles(ax,n,center,radius,w):
    if n > 0:
        x,y = circle(center,radius)
        ax.plot(x,y,linewidth=0.5,color='k')
        new_radius = radius * w   # We decrement the length of the radius 
        draw_inside_circles(ax,n-1,[center[0],center[1]],new_radius,w)

'''   Figure No. 2   '''

def draw_inside_triangle(ax,n,p):
    if n > 0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        i1 = [1,2,3,1]   # We swap the elements to the left, to flip the figure
        q = p/2 + p[i1]/2   # We divide the coordinates by two so that the figure 
        draw_inside_triangle(ax,n-1,q)   # is twice as small as the previous one

'''   Figure No. 3   '''

def draw_triangles(ax,n,p):
    if n>0:
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        i1 = [1,2,3,1]
        q = p/2 + p[i1]/2
        draw_triangles(ax,n-1,q)   # Center Triangle
        draw_triangles(ax,n-1,np.array([p[0],q[0],q[2],p[0]]))   # Left Triangle
        draw_triangles(ax,n-1,np.array([q[0],p[1],q[1],q[0]]))   # Top Triangle
        draw_triangles(ax,n-1,np.array([q[2],q[1],p[2],q[2]]))   # Right Triangle
        
'''   Figure No. 4   '''

def draw_four_squares(ax,n,C,L):
    if n>0:
        p0 = [C[0]-L,C[1]-L]    # Bottom left corner point
        p1 = [C[0]-L,C[1]+L]    # Upper left corner point
        p2 = [C[0]+L,C[1]+L]    # Upper right corner point
        p3 = [C[0]+L,C[1]-L]    # Bottom right corner point
        p = np.array([p0,p1,p2,p3,p0])   # Coordinates to create the square
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        draw_four_squares(ax,n-1,p0,L/2)    # Bottom left corner square
        draw_four_squares(ax,n-1,p1,L/2)    # Upper left corner square
        draw_four_squares(ax,n-1,p2,L/2)    # Upper right corner square
        draw_four_squares(ax,n-1,p3,L/2)    # Upper right corner square

'''   Figure No. 5   '''

def draw_root(ax,n,x,y,dx,dy):
    if n>0:
        ax.plot(x,y,linewidth=0.5,color='k')
        draw_root(ax,n-1,[x[0]-dx,x[0],x[2]-dx],[y[0]-dy,y[0],y[2]-dy],dx/2,dy) # Left line
        draw_root(ax,n-1,[x[0]+dx,x[0],x[2]+dx],[y[0]-dy,y[0],y[2]-dy],dx/2,dy) # Right line

'''   Figure No. 6   '''

def draw_tree(ax,n,p,L,m1,alpha,beta,m2):
    if n > 0:
        x0 = p[0]
        y0 = p[1]
        x1 = x0 + L*round(math.cos(math.radians(alpha)),2)  # Formula to find x1 (ending point).
        y1 = y0 + L*round(math.sin(math.radians(alpha)),2)  # Formula to find y1 (ending point).
        p = np.array([[x0,y0],[x1,y1],[x0,y0]]) # We create an array with the coordinates.
        ax.plot(p[:,0],p[:,1],linewidth=0.5,color='k')
        draw_tree(ax,n-1,[x1,y1],L*m1,m1,alpha+beta,beta*m2,m2)
        draw_tree(ax,n-1,[x1,y1],L*m1,m1,alpha-beta,beta*m2,m2) 

if __name__ == "__main__":  
    
    plt.close("all") # Close all figures
    
    orig_size = 1000.0
    p = np.array([[0,0],[0,orig_size],[orig_size,orig_size],[orig_size,0],[0,0]])
    print('Points in original square:')
    print(p)
    
    fig, ax = plt.subplots()
    draw_squares(ax,6,p,.1)
    ax.set_aspect(1.0)
    ax.axis('off') # Uncomment to see coordinates in drawing
    plt.show()
    fig.savefig('squaresa.png')
    
    fig, ax = plt.subplots()
    draw_squares(ax,10,p,.2)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('squaresb.png')
    
    fig, ax2 = plt.subplots()
    draw_squares(ax2,5,p,0.3)
    ax2.set_aspect(1.0)
    ax2.axis('off')
    plt.show()
    fig.savefig('squaresc.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 2, [0,0], 100)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_circlesa.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 3, [0,0], 100)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_circlesb.png')
    
    fig, ax = plt.subplots() 
    draw_four_circles(ax, 4, [0,0], 100)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_circlesc.png')
    
    
    '''   Figure No. 1   '''
    
    fig, ax = plt.subplots() 
    draw_inside_circles(ax, 3, [0,0], 100, 0.7)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_circlea.png')
    
    fig, ax = plt.subplots() 
    draw_inside_circles(ax, 6, [0,0], 100, 0.8)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_circleb.png')
    
    fig, ax = plt.subplots() 
    draw_inside_circles(ax, 9, [0,0], 100, 0.9)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_circlec.png')
    
    '''   Figure No. 2   '''
     
    triangle_height = 1000.0
    triangle_base = 500.0
    p = np.array([[0,0],[triangle_base,triangle_height],[triangle_height,0],[0,0]])
    
    fig, ax = plt.subplots()
    draw_inside_triangle(ax,3,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_trianglea.png')
    
    fig, ax = plt.subplots()
    draw_inside_triangle(ax,5,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_triangleb.png')
    
    fig, ax = plt.subplots()
    draw_inside_triangle(ax,7,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('inside_trianglec.png')
    
    '''   Figure No. 3   '''
    
    triangle_height = 1000.0
    triangle_base = 500.0
    p = np.array([[0,0],[triangle_base,triangle_height],[triangle_height,0],[0,0]])
    
    fig, ax = plt.subplots()
    draw_triangles(ax,2,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangle_of_trianglesa.png')
    
    fig, ax = plt.subplots()
    draw_triangles(ax,3,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangle_of_trianglesb.png')
    
    fig, ax = plt.subplots()
    draw_triangles(ax,4,p)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('triangle_of_trianglesc.png')
    
    '''   Figure No. 4   '''
    
    fig, ax = plt.subplots()
    draw_four_squares(ax,2,[0,0],1000.0)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_squaresa.png')
    
    fig, ax = plt.subplots()
    draw_four_squares(ax,3,[0,0],1000.0)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_squaresb.png')
    
    fig, ax = plt.subplots()
    draw_four_squares(ax,4,[0,0],1000.0)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('four_squaresc.png')
    
    '''   Figure No. 5   '''
    
    delta_x = 800
    delta_y = 200
    center = np.array([[0,0],[0,0],[0,0]])
    
    fig, ax = plt.subplots()
    draw_root(ax,5,center[:,0],center[:,1],delta_x,delta_y)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('roota.png')
    
    fig, ax = plt.subplots()
    draw_root(ax,6,center[:,0],center[:,1],delta_x,delta_y)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('rootb.png')
    
    fig, ax = plt.subplots()
    draw_root(ax,7,center[:,0],center[:,1],delta_x,delta_y)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('rootc.png')
    
    '''   Figure No. 6   '''

    fig, ax = plt.subplots()
    draw_tree(ax,6,[0,0],100,0.6,90.0,45.0,0.9)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treea.png')
    
    fig, ax = plt.subplots()
    draw_tree(ax,10,[0,0],100,0.7,90.0,60.0,0.7)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treeb.png')
    
    fig, ax = plt.subplots()
    draw_tree(ax,9,[0,0],100,0.82,90.0,45.0,0.75)
    ax.set_aspect(1.0)
    ax.axis('off')
    plt.show()
    fig.savefig('treec.png')