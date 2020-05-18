# Implementation of disjoint set forest (or union/find data structure)
# Programmed by Olac Fuentes
# Last modified April 20, 2020

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

class DSF:
    # Constructor
    def __init__(self, sets):
        # Creates forest with 'sets' root nodes
        self.parent = np.zeros(sets,dtype=int)-1
      
    def find(self,i):
        # Returns root of tree that i belongs to
        if self.parent[i]<0:
            return i
        return self.find(self.parent[i])

    def union(self,i,j):
        # Makes root of j's tree point to root of i's tree if they are different
        # Return 1 if a parent reference was changed, 0 otherwise
        root_i = self.find(i)
        root_j = self.find(j)
        print('i={}, j={}, root_i={}, root_j={}'.format(i,j,root_i,root_j))
        if root_i != root_j:
            self.parent[root_j] = root_i
            return 1
        return 0 
    
    def set_list(self):
        # Returns a list of lists containing the elements of each set
        set_list = [ [] for i in range(len(self.parent))]
        for i in range(len(self.parent)):
            set_list[self.find(i)].append(i)
        set_list = [s for s in set_list if len(s)>0] # Remove empty lists
        return set_list
    
    def draw(self,title=''):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.parent)):
            if self.parent[i]<0:
                ax.plot([i*scale,i*scale],[0,scale],linewidth=1,color='k')
                ax.plot([i*scale-1,i*scale,i*scale+1],[scale-2,scale,scale-2],linewidth=1,color='k')
            else:
                x = np.linspace(i*scale,self.parent[i]*scale)
                x0 = np.linspace(i*scale,self.parent[i]*scale,num=5)
                diff = np.abs(self.parent[i]-i)
                if diff == 1:
                    y0 = [0,0,0,0,0]
                else:
                    y0 = [0,-6*diff,-8*diff,-6*diff,0]
                f = interp1d(x0, y0, kind='cubic')
                y = f(x)
                ax.plot(x,y,linewidth=1,color='k')
                ax.plot([x0[2]+2*np.sign(i-self.parent[i]),x0[2],x0[2]+2*np.sign(i-self.parent[i])],[y0[2]-1,y0[2],y0[2]+1],linewidth=1,color='k')
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
        fig.suptitle(title, fontsize=16)
    
if __name__ == "__main__":    
    plt.close("all")      
    s = DSF(6)
    print(s.parent)
    s.draw()
    
    s.union(0,1)
    print(s.parent)
    s.draw()
    
    s.union(4,2)
    print(s.parent)
    s.draw()
    
    s.union(3,5)
    print(s.parent)
    s.draw()
    
    s.union(1,5)
    print(s.parent)
    s.draw()
    
    for i in range(6):
        print('Element:',i,'root:',s.find(i))
        
    print(s.set_list())
    
