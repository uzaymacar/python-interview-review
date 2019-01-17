class TreeNode(object):
    def __init__(self, name = "", children = []):
        self.name = name
        self.adjacent = [] # adjacency list
        self.visited = False

class Graph(object): # unlike in a tree, you can't necessarily reach all the nodes from a single node!
    def __init__(self):
        self.max_vertices = 6
        self.vertices = [0] * self.max_vertices
        self.count = 0
    
    def addNode(self, x):
        if self.count < self.max_vertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("Graph Full")
            
    def getNodes(self):
        return self.vertices

class Node():
    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("No more adjacent nodes can be added")

    def getAdjacent(self):
        return self.adjacent

    def getVertex(self):
        return self.vertex
    
class Tree(object):
    def __init__(self, root = TreeNode()):
        self.root = root

class Queue(object): # queue implementation using standard Python list
    def __init__(self, head = None): # initiliaze with a list containing head as its first element
        self.storage = []

    def enqueue(self, new_element): # append to the end of the queue
        self.storage.append(new_element)

    def peek(self): # get the top of the queue
        return self.storage[0]

    def dequeue(self): # remove the top element from the queue
        return self.storage.pop(0)
    
    def isEmpty(self):
        return self.storage == [] # test for this!
    
def is_route(graph, source_node, destination_node):
    q = Queue()
    source_node.visited = True
    q.enqueue(source_node)
    while not q.isEmpty():
        r = q.dequeue()  
        for node in r.adjacent:
            if node.visited == False:
                if node != destination_node:
                    node.visited = True
                    q.enqueue(node)
                else:
                    return True
    return False


def createNewGraph():
    g = Graph()
    sizegraph = 6
    temp = [0] * sizegraph

    temp[0] = Node("a", 3)
    temp[1] = Node("b", 0)
    temp[2] = Node("c", 0)
    temp[3] = Node("d", 1)
    temp[4] = Node("e", 1)
    temp[5] = Node("f", 0)

    temp[0].addAdjacent(temp[1])
    temp[0].addAdjacent(temp[2])
    temp[0].addAdjacent(temp[3])
    temp[3].addAdjacent(temp[4])
    temp[4].addAdjacent(temp[5])

    for i in range(sizegraph):
        g.addNode(temp[i])
    return g

g = createNewGraph()
n = g.getNodes()
start = n[0]
end = n[5]
print("Start at:", start.getVertex(), "End at: ", end.getVertex())
print(is_route(g, start, end))
