class mygraph:
    def __init__(self):
        self.nodes = []

    def add(self, newnode):
        self.nodes.append(newnode)
    
    def remove(self, key):
        self.nodes.remove(key)
        self.clean_edges(key)
    
    def clean_edges(self, key):
        for node in self.nodes:
            weight = 0
            for edge in node.edges:
                if edge[0] == key:
                    weight = edge[1]
                    break
            
            node.edges.remove((key, weight))
            break
    
    def dfsearch(self, key):
        print("df search")
        queue = []
        visited = []

        for node in self.nodes:
            if node.key == key:
                queue.insert(0, node)
                break

        while len(queue) > 0:
            current = queue.pop(0)
            if current not in visited:
                print(f"{current.key} | {current.getpathweight()}")
                visited.append(current)
                for edge in current.edges:
                    for node in self.nodes:
                        if node.key == edge[0]:
                            queue.insert(0, node)
                            break
    
    def bfsearch(self, key):
        print("bf search")
        queue = []
        visited = []

        for node in self.nodes:
            if node.key == key:
                queue.append(node)
                break
        
        while len(queue) > 0:
            current = queue.pop(0)
            if current not in visited:
                print(f"{current.key} | {current.getpathweight()}")
                visited.append(current)
                for edge in current.edges:
                    for node in self.nodes:
                        if node.key == edge[0]:
                            queue.append(node)
                            break
    
    def dijkstra(self, key):
        print("dijkstra")
        queue = self.nodes[:]
        start = None

        for node in queue:
            if node.key == key:
                start = node
                break
        
        start.setpathweight(0)
        current = queue[0]

        while len(queue) > 0:
            current = queue[0]
            for node in queue:      
                if node.getpathweight() < current.getpathweight():
                    current = node

            queue.remove(current)

            for edge in current.edges:
                for node in self.nodes:
                    if edge[0] == node.key:
                        if current.getpathweight() + edge[1] < node.getpathweight():
                            node.setpathweight(current.getpathweight() + edge[1])
                            node.setpred(current)