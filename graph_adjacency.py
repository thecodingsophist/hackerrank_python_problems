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
        self.graph = [None] * self.V # Q: Not sure if I understand this

    # Function to add an edge in an undirected graph
    def add_edge (self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src] # Q: what is the next built in function (?) or do we define it?
        self.graph[src] = node

        # Adding the source node to the destination as it is the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        # THIS IS THE IMPORTANT PART + WHAT I"M AFTER
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")
