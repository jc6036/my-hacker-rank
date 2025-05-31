class BNode:
    def __init__ (self, initialdata, parent=None, left=None, right=None):
        self.data = initialdata
        self.parent = parent
        self.left = left
        self.right = right
    
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