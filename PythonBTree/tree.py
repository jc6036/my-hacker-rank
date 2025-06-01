from node import BNode
import math

# 05/31 - Modified into self balancing AVL Tree

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
                self.recalc_parent_height(new_node.get_parent())
                self.balance_node(new_node)
            else:
                self.find_empty_and_insert(val, cur_node.get_left())
                return

        elif val >= cur_node.get_data():
            if cur_node.get_right() == None:
                new_node = BNode(val)
                new_node.set_parent(cur_node)
                cur_node.set_right(new_node)
                self.recalc_parent_height(new_node.get_parent())
                self.balance_node(new_node)                
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
                    self.recalc_parent_height(par)
                    self.balance_node(par)
                    return
                if par.get_right() == cur_node:
                    par.set_right(None)
                    self.recalc_parent_height(par)
                    self.balance_node(par)
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
                self.recalc_parent_height(par)
                self.balance_node(par)
                return
        
        # Has Right
        if cur_node.get_left() == None and cur_node.get_right() != None:
            if cur_node == self.root:
                self.root = cur_node.get_right()
                return
            else:
                par = cur_node.get_parent()
                par.set_right(cur_node.get_right())
                self.recalc_parent_height(par)
                self.balance_node(par)
                return
        
        # Node with two children removal - find the successor and remove recursively to shift the tree
        if cur_node.get_left() != None and cur_node.get_right() != None:
            # Get the successor
            successor = cur_node.get_right()
            if successor.get_left() != None:
                successor = successor.get_left()
            
            cur_node.set_data(successor.get_data())
            self.recalc_parent_height(cur_node)
            self.balance_node(cur_node)
            self.remove(successor)
            return

    def traverse(self):
        self.traverse_and_print(self.root)

    def traverse_and_print(self, node):
        if node == None:
            return
        else:
            self.traverse_and_print(node.get_left())
            print(f"d:{node.get_data()} | h:{node.get_height()} | bf:{node.get_balance_factor()}")
            self.traverse_and_print(node.get_right())

    def height(self):
        return self.get_height(self.root)
    
    def get_height(self, node):
        if node == None:
            return -1
        
        left_side_height = self.get_height(node.get_left())
        right_side_height = self.get_height(node.get_right())
        return 1 + max(left_side_height, right_side_height)
    
    def recalc_heights(self):
        self.set_heights(self.root)
    
    def set_heights(self, node):
        if node == None:
            return
        
        node.set_height(self.get_height(node))
        if node.get_left() != None:
            self.set_heights(node.get_left())
        if node.get_right() != None:
            self.set_heights(node.get_right())
    
    def recalc_parent_height(self, node):        
        if node != None:
            node.set_height(self.get_height(node))
            self.recalc_parent_height(node.get_parent())
    
    def rotate_right(self, node):
        nleft = node.get_left()
        nleftright = nleft.get_right()

        if node.get_parent() != None:
            npar = node.get_parent()
            npar.set_left(nleft)
            nleft.set_parent(npar)
        else:
            nleft.set_parent(None)
            self.root = nleft

        node.set_parent(nleft)
        node.set_left(nleftright)

        nleft.set_right(node)

        if nleftright != None:
            nleftright.set_parent(node)

    def rotate_left(self, node):
        nright = node.get_right()
        nrightleft = nright.get_left()

        if node.get_parent() != None:
            npar = node.get_parent()
            npar.set_right(nright)
            nright.set_parent(npar)
        else:
            nright.set_parent(None)
            self.root = nright
        
        node.set_parent(nright)
        node.set_right(nrightleft)

        nright.set_left(node)

        if nrightleft != None:
            nrightleft.set_parent(node)
    
    def balance_node(self, node):
        if node != None:
            if node.get_balance_factor() >= 2:
                if node.get_left().get_balance_factor() == -1:
                    self.rotate_left(node.get_left())
                self.rotate_right(node)
                self.recalc_parent_height(node)
            elif node.get_balance_factor() <= -2:
                if node.get_right().get_balance_factor() == 1:
                    self.rotate_right(node.get_right())
                self.rotate_left(node)
                self.recalc_parent_height(node)
            
            self.balance_node(node.get_parent())
