class myheap:
    def __init__(self):
        self.core = []
    
    
    def insert(self, val):
        self.core.append(val)
        self.percolate_up(len(self.core)-1)
        
    def remove(self):
        self.core[0] = self.core[-1]
        self.core.pop()
        self.percolate_down(0)
    
    def print_out(self):
        print(self.core)
    
    def heapsort_list_out(self):
        out_list = []
        
        while len(self.core) > 0:
            out_list.append(self.core[0])
            self.remove()
        
        return out_list
        
    def percolate_up(self, index):
        if index == 0:
            return

        parent = (index-1) // 2
        if self.core[parent] < self.core[index]:
            tmp = self.core[parent]
            self.core[parent] = self.core[index]
            self.core[index] = tmp
            self.percolate_up(parent)
        else:
            return
    
    def percolate_down(self, index):
        childleft = 2 * index + 1
        childright = 2 * index + 2
        leftval = 0
        rightval = 0
        
        if childleft < len(self.core):
            leftval = self.core[childleft]
        if childright < len(self.core):
            rightval = self.core[childright]
        
        if leftval > rightval and leftval > self.core[index]:
            self.core[childleft] = self.core[index]
            self.core[index] = leftval
            self.percolate_down(childleft)
        elif rightval > leftval and rightval > self.core[index]:
            self.core[childright] = self.core[index]
            self.core[index] = rightval
            self.percolate_down(childright)
        
        return
    

if __name__ == '__main__':
    heap = myheap()
    
    for i in [5, 123, 66, 121, 7, 10, 20, 596, 49, 324, 587]:
        heap.insert(i)
    
    heap.print_out()
    heap.remove()
    heap.print_out()
    
    sorted = heap.heapsort_list_out()
    print(sorted)
