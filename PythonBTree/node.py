class BNode:
    def __init__ (self, initialdata, parent=None, left=None, right=None):
        self.data = initialdata
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0
    
    def get_parent(self):
        return self.parent
    
    def set_parent(self, parent):
        self.parent = parent
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data

    def set_height(self, height):
        self.height = height
    
    def get_height(self):
        return self.height
    
    def get_balance_factor(self):
        l = 0
        r = 0

        if self.left == None:
            l = -1
        if self.right == None:
            r = -1
        
        return l - r
