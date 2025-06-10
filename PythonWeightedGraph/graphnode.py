class graphnode:
    def __init__(self, key, edges):
        self.key = key
        self.edges = edges
        self.predecessor = None
        self.path = 500000
    
    def setpred(self, pred):
        self.predecessor = pred
    
    def getpred(self):
        return predecessor
    
    def setpathweight(self, weight):
        self.path = weight
    
    def getpathweight(self):
        return self.path
    