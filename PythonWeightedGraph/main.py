from mygraph import mygraph
from graphnode import graphnode

if __name__ == '__main__':
    graph = mygraph()

    graph.add(graphnode('A', [('B',5), ('D', 2), ('E', 8)]))
    graph.add(graphnode('B', [('D', 12), ('C', 16)]))
    graph.add(graphnode('C', [('A', 2)]))
    graph.add(graphnode('D', [('B', 12)]))
    graph.add(graphnode('E', [('C', 22), ('D', 10), ('F', 1)]))
    graph.add(graphnode('F', [('C', 50)]))

    graph.bfsearch('A')
    print("-----")
    graph.dfsearch('A')
