# Practice adjacency list representation of the graph

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V # Not sure if I understand this

    # Function to add an edge in an undirected graph
    def
