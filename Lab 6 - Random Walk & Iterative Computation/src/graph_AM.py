import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d
import graph_AL 


class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int)-1
        self.weighted = weighted
        self.directed = directed
        
    def insert_edge(self,source,dest,weight=1):
        self.am[source,dest]=weight
        if not self.directed:
            self.am[dest,source]=weight
        return
        
    def delete_edge(self,source,dest):
        self.am[source,dest]=-1
        if not self.directed:
            self.am[dest,source]=-1
        return 
                
    def display(self):
        print('Graph representation')
        print('directed: {}, weighted: {}'.format(self.directed,self.weighted))
        print('Adjacency matrix:')
        print(self.am)

    def draw(self,title=''):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(self.am.shape[0]):
            for d in range(self.am.shape[1]):
                w = self.am[i,d]
                if w>0:
                    if self.directed or d>i:
                        x = np.linspace(i*scale,d*scale)
                        x0 = np.linspace(i*scale,d*scale,num=5)
                        diff = np.abs(d-i)
                        if diff == 1:
                            y0 = [0,0,0,0,0]
                        else:
                            y0 = [0,-6*diff,-8*diff,-6*diff,0]
                        f = interp1d(x0, y0, kind='cubic')
                        y = f(x)
                        s = np.sign(i-d)
                        ax.plot(x,s*y,linewidth=1,color='k')
                        if self.directed:
                            xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                            yd = [y0[2]-1,y0[2],y0[2]+1]
                            yd = [y*s for y in yd]
                            ax.plot(xd,yd,linewidth=1,color='k')
                        if self.weighted:
                            xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                            yd = [y0[2]-1,y0[2],y0[2]+1]
                            yd = [y*s for y in yd]
                            ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
                ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
                ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
                 bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        if title=='':
            dp, wp = 'Undirected ', 'unweighted '
            if self.directed:
                dp='Directed '
            if self.weighted:
                wp='weighted '    
            title = dp + wp + 'graph'
        fig.suptitle(title, fontsize=16)
            
if __name__ == "__main__":   
    plt.close("all")   
    g = Graph(5)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    
    g = Graph(5,directed = True)
    g.insert_edge(0,1)
    g.insert_edge(0,2)
    g.insert_edge(1,2)
    g.insert_edge(2,3)
    g.insert_edge(3,4)
    g.insert_edge(4,1)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(5,weighted=True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    g = Graph(5,weighted=True,directed = True)
    g.insert_edge(0,1,4)
    g.insert_edge(0,2,3)
    g.insert_edge(1,2,2)
    g.insert_edge(2,3,1)
    g.insert_edge(3,4,5)
    g.insert_edge(4,1,4)
    g.display()
    g.draw()
    g.delete_edge(1,2)
    g.display()
    g.draw()
    
    
        

