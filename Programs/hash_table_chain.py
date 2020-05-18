# Implementation of hash tables with chaining
# Programmed by Olac Fuentes
# Last modified March 25, 2020

class HashTableRecord:
    def __init__(self,key, data):  
        self.key = key
        self.data = data

class HashTableChain:
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]
        
    def h(self, key):
        if type(key)==int: # the key is an integer (easy case)
            return key%len(self.bucket)
        n = 0
        for s in key: # the key is a string (slightly more complicated to reduce collisions)
            n = (n*511 + ord(s))%len(self.bucket) 
        return n 
            
    def insert(self,key,data):
        # Inserts k in appropriate bucket (list) if k is not already in the table
        # Returns 1 in case of a successful insertion, -1 otherwise
        b = self.h(key)
        for rec in self.bucket[b]:
            if rec.key == key:
                #print('Insertion error, key',key,'is already in the table')
                return -1
        self.bucket[b].append(HashTableRecord(key,data))      
        return 1
        
    def retrieve(self, key):
        # Returns data associated with key, or None if the key is not in the table
        b = self.h(key)
        for rec in self.bucket[b]:
            if rec.key == key:
                return rec.data
        return None    # key is not in the table
    
    def update(self, key, data):
        # Updates data associated with key if it is in the table
        # Returns 1 in case of a successful update, -1 otherwise
        b = self.h(key)
        for rec  in self.bucket[b]:
            if rec.key == key:
                rec.data = data
                return 1
        return -1
                
    def delete(self, key):
        # Deletes record with given keyif it is in the table
        # Returns 1 in case of a successful deletion, -1 otherwise
        b = self.h(key)
        for i in range(len(self.bucket[b])):
            if key == self.bucket[b][i].key:
                self.bucket[b].pop(i)
                return 1
        return -1
    
    def print_table(self):
        print('Table contents:')
        for i in range(len(self.bucket)):
            print('bucket',i,end=': [ ')
            for rec in self.bucket[i]:
                print('[{}, {}]'.format(rec.key,rec.data),end=' ')
                #print('[',rec.key,rec.data,end=']')
            print(']')
       
if __name__ == "__main__":   
    
    table_size = 7
    print('Example 1, using student_number as key, name as data')
    print('table size =', table_size)
    h = HashTableChain(table_size)
    h.print_table()
    name = ['Alice','Bob','Carlos','Diana','Emma','Fred']
    student_number = [15, 27, 14, 10, 8, 7]
    
    for i in range(len(name)):
        h.insert(student_number[i], name[i])
        h.print_table()
        
    search_number = 10
    n = h.retrieve(search_number)
    if n!=None:
        print('The name of the student with number {} is {}'.format(search_number,n))
        
    print(h.update(8, 'Anthony'))
    
    h.update(8, 'Anthony')
    h.print_table()
    h.delete(14)
    h.print_table()
    
    print('Example 2, using name as key, grade as data') # This wouldn't work in practice as key is not unique
    print('table size =', table_size)
    h = HashTableChain(table_size)
    h.print_table()
    name = ['Alice','Bob','Carlos','Diana','Emma','Fred']
    grade = [85, 67, 94, 100, 80, 70]
    
    for i in range(len(name)):
        h.insert(name[i], grade[i])
        h.print_table()
       
    h.update('Bob', 75)
    h.print_table()
    
    h.delete('Diana')
    h.print_table()
    
    search_name = 'Carlos'
    g = h.retrieve(search_name)
    if g!=None:
        print('Student {} obtained a grade of {}'.format(search_name,g))