# Practice adjacency list representation of the graph

class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices "V"

class Graph(__name__):
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

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    # def print_graph(self):
    #     for i in range(self.V):
    #         print("Adjacency list of vertex {}\n head".format(i))
    #         temp = self.graph[i]
    #         while temp:
    #             print(" -> {}".format(temp.vertex))
    #             temp = temp.next
    #         print(" \n")

    if __name__ == "__main__":

        V = 5
        graph = Graph(V)
        graph.add_edge(0,1)
        graph.add_edge(0,4)
        graph.add_edge(1,2)
        graph.add_edge(1,3)
        graph.add_edge(1,4)
        graph.add_edge(2,3)
        graph.add_edge(3,4)

        graph.print_graph()
