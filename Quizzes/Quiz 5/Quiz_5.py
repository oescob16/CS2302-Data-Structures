import btree

def nodeRange(t):
    if len(t.data) == 0:
        return 0
    return t.data[-1] - t.data[0]

def countFullNodes(t):
    if type(t) == btree.BTree:
        t = t.root
    if t.is_leaf:
        if t.is_full():
            return 1
        return 0
    full_count = 0
    if t.is_full():
        full_count += 1
    for i in t.child:
        full_count += countFullNodes(i)
    return full_count

def itemsAtDepthD(t,d):
    if type(t) == btree.BTree:
        t = t.root
    if d == 0:
        return t.data
    list_item = []
    for i in t.child:
        list_item += itemsAtDepthD(i,d-1)
    return list_item

if __name__ == "__main__":
    plt.close('all')
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T2 = btree.BTree()   
    for num in [32,12,58,7,43]:
        T2.insert(num)
        
    T_empty = btree.BTree()
    
    T.draw()
    T2.draw()
    
    print(nodeRange(T.root))  # 0
    t = T.find(4)
    print(nodeRange(t))       # 4
    t = T.find(25)
    print(nodeRange(t))       # 2
    print(nodeRange(T_empty.root)) # 0
    print(nodeRange(T2.root)) # 51
    
    print(countFullNodes(T))        # 3
    print(countFullNodes(T_empty))  # 0
    print(countFullNodes(T2))       # 1
    
    print(itemsAtDepthD(T,0))   # [17]
    print(itemsAtDepthD(T,1))   # [6, 11, 23, 27]
    print(itemsAtDepthD(T,2))   # [1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20, 21, 22, 24, 25, 26, 28, 29, 30]
    print(itemsAtDepthD(T,3))   # []
    print(itemsAtDepthD(T2,0))  # [7, 12, 32, 43, 58]
    print(itemsAtDepthD(T2,1))  # []