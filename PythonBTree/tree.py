from node import BNode
import math

class BTree:
    def __init__ (self):
        self.root = None
    
    def search(self, val):
        return self.get_node(val, self.root)
    
    def get_node(self, val, node):
        if node == None:
            return None
        elif node.get_data() == val:
            return node
        else:
            if val >= node.get_data():
                if node.get_right() != None:
                    return self.get_node(val, node.get_right())
                else:
                    return None
            elif val <= node.get_data():
                if node.get_left() != None:
                    return self.get_node(val, node.get_left())
                else:
                    return None        
        
        return None
    
    def insert(self, val):        
        self.find_empty_and_insert(val, self.root)

    def find_empty_and_insert(self, val, cur_node):
        if cur_node == self.root and cur_node == None:
            new_node = BNode(val)
            self.root = new_node
            return
        
        elif val <= cur_node.get_data():
            if cur_node.get_left() == None:
                new_node = BNode(val)
                new_node.set_parent(cur_node)
                cur_node.set_left(new_node)
            else:
                self.find_empty_and_insert(val, cur_node.get_left())
                return

        elif val >= cur_node.get_data():
            if cur_node.get_right() == None:
                new_node = BNode(val)
                new_node.set_parent(cur_node)
                cur_node.set_right(new_node)
            else:
                self.find_empty_and_insert(val, cur_node.get_right())
                return

    def remove_by_val(self, val):
        self.remove(self.search(val))

    def remove(self, cur_node):
        if cur_node == None:
            return

        # Leaf removal
        if cur_node.get_left() == None and cur_node.get_right() == None:
            if cur_node == self.root:
                self.root = None
                return
            else:
                par = cur_node.get_parent()
                if par.get_left() == cur_node:
                    par.set_left(None)
                    return
                if par.get_right() == cur_node:
                    par.set_right(None)
                    return
        
        # Node with one child removal
        # Has Left
        if cur_node.get_left() != None and cur_node.get_right() == None:
            if cur_node == self.root:
                self.root = cur_node.get_left()
                return
            else:
                par = cur_node.get_parent()
                par.set_left(cur_node.get_left())
                return
        
        # Has Right
        if cur_node.get_left() == None and cur_node.get_right() != None:
            if cur_node == self.root:
                self.root = cur_node.get_right()
                return
            else:
                par = cur_node.get_parent()
                par.set_right(cur_node.get_right())
                return
        
        # Node with two children removal - find the successor and remove recursively to shift the tree
        if cur_node.get_left() != None and cur_node.get_right() != None:
            # Get the successor
            successor = cur_node.get_right()
            if successor.get_left() != None:
                successor = successor.get_left()
            
            cur_node.set_data(successor.get_data())
            self.remove(successor)
            return

    def traverse(self):
        self.traverse_and_print(self.root)

    def traverse_and_print(self, node):
        if node == None:
            return
        else:
            self.traverse_and_print(node.get_left())
            print(f"{node.get_data()}")
            self.traverse_and_print(node.get_right())

    def height(self):
        return self.get_height(self.root)
    
    def get_height(self, node):
        if node == None:
            return -1
        
        left_side_height = self.get_height(node.get_left())
        right_side_height = self.get_height(node.get_right())
        return 1 + max(left_side_height, right_side_height)