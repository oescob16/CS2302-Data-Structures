#   Course: CS 2302
#   Assignment: Lab III
#   Author: Oswaldo Escobedo 
#   Instructor: Dr. Fuentes
#   TA: Harshavardhini Bagavathyraj
#   Date of Last Modification: 02/28/2020
#   Purpose of the Program: to implement functions 
#   to the List Class. 

import matplotlib.pyplot as plt
import numpy as np
import math

class ListNode: 
    # Constructor
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor
    def __init__(self,head = None,tail = None):
        self.head = head
        self.tail = tail

    def print(self):
        t = self.head
        while t is not None:
            print(t.data,end=' ')
            t = t.next
        print()

#%% Lab 3
        
    def append(self,x):
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next

    def extend(self,python_list):
        for d in python_list:
            self.append(d) 
            
    def insert(self,i,x):
        if self.head is None: # List is empty
            self.append(x)
            return
        if i == 0: # Inserts a node at the beginning of the list
            self.head = ListNode(x,self.head)
            if self.head.next is None: # Updates tail
                self.tail = self.head.next
            return
        t = self.head
        pos = 0
        while t.next is not None and pos < i - 1: # Traverses list until t is None and 
            pos += 1                        # pos is less than the index
            t = t.next
        t.next = ListNode(x,t.next) # Inserts Node
        if t.next.next is None: # If the inserted node was the last one, then update tail
            self.tail = t.next
            
    def remove(self,x):
        if self.head is None: # List is empty
            raise ValueError
        if self.head.data == x: # Item is at the beginning of the list
            self.head = self.head.next # Updates head
            if self.head is None:
                self.tail = None
            return
        t = self.head
        while t.next is not None:
            if t.next.data == x: # If the current node has the item we are looking for,
                break         # then break
            t = t.next
        if t.next is None: # Item was not in the list
            raise ValueError
        else:
            next_node = t.next.next
            t.next = next_node # Removes the node containing x
            if next_node is None: # If the node we are removing is the last,
                self.tail = t   # then update tail
     
    def pop(self,i=-1): # If no parameter was given then set i to -1
        if self.head is None: # List is empty
            return -1
        if self.head.next is None: # Only one node in list, therefore we must pop it
            item = self.head.data # Stores the node's data before pop it
            self.head = None
            self.tail = None
            return item
        if i == 0: # Pops the first node in the list
            item = self.head.data 
            self.head = self.head.next
            return item
        t = self.head
        if i < 0: # i == -1, therefore we must pop the last node in the list
            while t.next.next is not None:
                t = t.next
            item = t.next.data 
            self.tail = t # Updates tail
            t.next = None
            return item
        else: # i is a valid index
            pos = 0
            while t.next.next is not None and pos < i - 1: 
                pos += 1
                t = t.next
            item = t.next.data 
            next_node = t.next.next # Pops the node
            t.next = next_node
            if next_node is None: # If the node we are removing is the last, then
                self.tail = t # update tail.
            return item
        
    def clear(self):
        self.head = None
        self.tail = None
        
    def index(self,x,start=0,end=math.inf): 
        if start > end or self.head is None: # List is empty or start is bigger than end
            raise ValueError
        t = self.head
        i = 0
        while t is not None and i != start: # While loop that helps us traverse 
            i += 1                       # until the desired start.
            t = t.next
        index = 0
        while t is not None and i != end: # While loop that stops when we have reach end.
            if x == t.data: # If the current node has the data we are looking for
                return index # then return its index
            t = t.next
            index += 1 
            i += 1
        raise ValueError # Value was not in the list
            
    def count(self,x):
        if self.head is None: # List is empty
            return 0
        t = self.head
        counter = 0
        while t is not None:
            if t.data == x: # Current node has x, so increment counter.
                counter += 1
            t = t.next
        return counter
          
    def sort(self):
        if self.head is None or self.head.next is None: # List is empty or has one node.
            return
        currNode = self.head 
        nextNode = None
        while currNode is not None: # Creates the boundary of the unsorted array
            nextNode = currNode.next
            while nextNode is not None: # Help us find the minimum element of unsorted array.
                if currNode.data > nextNode.data: # Compares curr and next nodes data.
                    currNode.data,nextNode.data = nextNode.data,currNode.data # swaps node data
                nextNode = nextNode.next 
            currNode = currNode.next
            
    def reverse(self):
        if self.head is None: # List is empty
            return
        curr_node = self.head
        prev_node = None
        next_node = next 
        tail = self.head # Variable that keeps a reference to head
        while curr_node is not None:
            next_node = curr_node.next # Saves next node of the curr node in the next pointer.
            curr_node.next = prev_node # Changes the next of the curr node to prev node.
            prev_node = curr_node # Makes prev point to curr
            curr_node = next_node # Makes curr to next
        self.head = prev_node # Sets head to be the last node we reached
        self.tail = tail # Sets tail to the first element we visit. For instance, the head of the original list.
        
    def copy(self):
        clone = List() # Creates an empty list
        t = self.head
        while t is not None:
            if clone.head is None: # Clone is empty
                clone.head = ListNode(t.data) # Creates a node which has the value of the original list
                clone.tail = clone.head # Updates tail
                t = t.next
            else:
                clone.append(t.data) # Copies and creates a node containing the data of the original list
                t = t.next
        return clone
            
#%%        
    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y

    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail: 
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()
#%%
if __name__ == "__main__":
    
    plt.close('all') 
    
    L = List()
    #L.draw('Empty List')
    
    L.insert(10,10)
    #L.draw('Insert in Empty List')
    
    L.insert(0,3)
    #L.draw('Insert at Index Zero')
    
    L.insert(1,5)
    #L.draw('Insert at Index i')
    
    L.insert(10,20)
    #L.draw('Insert at Last Index')
    
    L.remove(20)
    #L.draw('Removing Last Node')
    
    L.remove(5)
    #L.draw('Remove Middle Element')
    
    L.remove(3)
    #L.draw('Remove Head')
    
    L.remove(10)
    #L.draw('Remove Only Node in the List')
    
    #L.remove(30)
    # Throws a RaiseValue Error Exception
    
    L.clear()
    
    L.extend([12,32,68,79,80])
    #L.draw('Initial List')
    
    # Pops last element
    print(L.pop())
    #L.draw('i = -1')
    
    print(L.pop(0))
    #L.draw('Pops first element')
    
    # Pops user input index
    print(L.pop(2))
    #L.draw('User Input')
    
    # Pops only element in the list
    print(L.pop(10))
    #L.draw('Only Element in List')
    
    print(L.pop(10))
    
    # Returns a -1, because the list is empty
    print(L.pop(10))
    #L.draw('Empty List')
    
    for i in range(15):
        L.append(i)
    #L.draw('Initial List')
    L.clear()
    #L.draw('Deletes All Elements')
    
    L.clear()
    #L.draw('There is Nothing to Delete')
    
    
    L.extend(['a','b','c','d','e'])
    #L.draw('Initial List')
    
    # Returns the position of a from 0 to math.inf
    print(L.index('a'))
    # Returns the position of c from 0 to math.inf
    print(L.index('c'))
    # Returns the position of b from 1 to math.inf
    print(L.index('b',1))
    # Item was not found, throws a RaiseValue Exc.
    #print(L.index('f'))
    #returns the position of d from 2 to 4
    print(L.index('d',2,4))
    
    L.clear()
    
    for i in range(7):
        L.append(0)
    #L.draw('Seven Zeros')
    
    # Counts how many times 0 appears in the List
    print('\n\n\n\n')
    print(L.count(0))
    # Counts how many times 1 appears in the List
    print(L.count(1))
    
    L.clear()
    L.extend([1,23,1,30,23,1,4,1,6,8,9,1])
    #L.draw('Initial List')
    
    # Counts how many times 1 appears in the list
    print(L.count(1))
    
    L.clear()
    L.extend([3,2,1])
    #L.draw('Unsorted List 1')
    L.sort()
    #L.draw('Sorted List 1')
    
    L.clear()
    L.extend([4,68,45,78,1,3,986,4])
    #L.draw('Unsorted List 2')
    L.sort()
    #L.draw('Sorted List 2')
    
    L.clear()
    #L.draw('Unsorted List 3')
    L.sort()
    #L.draw('Sorted List 3')
    
    L.clear()
    L.extend(['a','e','i','o','u'])
    
    #L.draw('Original List')
    L.reverse()
    
    #L.draw('Reversed List')
    # We reverse the reversed list to return
    # to original list
    L.reverse()
    #L.draw('Reversed Reversed List')
    
    L.clear()
    L.append(0)
    #L.draw('Original List 2')
    L.reverse()
    #L.draw('Reversed List 2')
    
    L.clear()
    #L.draw('Original List3')
    L.reverse()
    #L.draw('Reversed List 3')
    
    L1 = List()
    L1.extend([0,1,2,3,4])
    L1.draw('List 1')
    L2 = L1.copy()
    L2.draw('List 2')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    