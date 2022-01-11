from graph import Graph, Node

''' 
    Edge class represents each each of a graph.
    It takes three values as attributes
    node1  : type of Node represents the first node
    node2  : type of Node represents the second node
    weight : type of int represents the wight of the edge 
'''
class Edge():
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


    '''__gt__ it is used to define the > between two edges based on the weight'''
    def __gt__(self, other):
        return self.weight > other.weight


    '''__lt__ it is used to define the < between two edges based on the weight'''
    def __lt__(self, other):
        return self.weight < other.weight


    '''__eq__ it is used to define the == between two edges based on the weight'''
    def __eq__(self, other):
        return self.weight == other.weight


    def __str__(self):
        return f"{self.node1.value} {self.node2.value} {self.weight}"


''' Represent the Kruskal's Algorithm '''
class Kruskal:
    def __init__(self, graph):
        self.graph = graph
        # create a new empty tree (in a form of graph)
        self.tree = Graph()
        # Add all the nodes to the new tree
        for node in self.graph.nodes:
            self.tree.add_node(node)
        
        # For each vertex of the graph we create a set and store them in a list
        self.sets = [set(node.value) for node in self.graph.nodes]
        self.edges = []
        self.number_of_vetices = len(graph.nodes)
        # Sort the edges in a ascend order based on the weight
        self.sort_edges()
        # Remove the edges from the nodes in the tree
        for node in self.tree.nodes:
            node.neighbors.clear()

       
    ''' Sort the edges of the list based in the weight of each edge '''
    def sort_edges(self):
        for node in self.graph.nodes:
            for edge in node.neighbors:
                self.edges.append(Edge(node, edge[0], edge[1]))
        self.edges.sort()


    ''' Return the index of the set in the list of sets, in which node is contained'''
    def find_set(self, node):
        for index, s in enumerate(self.sets):
            if node.value in s:
                return index


    ''' Union the given sets and delete them from the list '''
    def union_set(self, set1, set2):
        # Get the sets based on their index in the list
        selected_set1 = self.sets[set1]
        selected_set2 = self.sets[set2]
        # Union the two sets
        new_set = selected_set1.union(selected_set2)
        # Delete the individual sets
        self.sets.remove(selected_set1)       
        self.sets.remove(selected_set2)
        # Add the union of the set in the list of sets
        self.sets.append(new_set)   


    ''' The core of the algorithm. Execute the repetitive steps of Kruskal's Algorithm'''
    def execution(self):
        # intitialize the values
        inserted_edges = 0
        total_cost = 0
        while True:
            # Select the edge with the minimum weight
            selected_edge = self.edges.pop(0)

            set1 = self.find_set(selected_edge.node1)
            set2 = self.find_set(selected_edge.node2)

            # If the vertices og the edge are not in the same set
            # the edge does not form a cyrcle, so it is added to the tree
            if set1 != set2:
                # update the values
                inserted_edges += 1
                total_cost += selected_edge.weight
                self.union_set(set1, set2)
                self.tree.add_edge(selected_edge.node1.value, selected_edge.node2.value, selected_edge.weight)
            # Check if the necessary number of edges are inserted on the tree
            if inserted_edges == self.number_of_vetices - 1:
                return self.tree, total_cost
                

def main():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('A'))
    graph.add_node(Node('B'))
    graph.add_node(Node('C'))
    graph.add_node(Node('D'))
    graph.add_node(Node('E'))
    graph.add_node(Node('F'))
    graph.add_node(Node('G'))
    graph.add_node(Node('H'))
    graph.add_node(Node('I'))
    # Add edges
    graph.add_edge('A', 'B', 9)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 1)
    graph.add_edge('B', 'E', 7)
    graph.add_edge('C', 'D', 4)
    graph.add_edge('C', 'F', 3)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 5)
    graph.add_edge('E', 'F', 6)
    graph.add_edge('E', 'G', 3)
    graph.add_edge('F', 'G', 8)
    graph.add_edge('F', 'H', 5)
    graph.add_edge('G', 'H', 1)
    graph.add_edge('G', 'I', 3)
    graph.add_edge('H', 'I', 2)

    # Execute the algorithm
    alg = Kruskal(graph)
    min_spanning_tree, cost = alg.execution()
    print("The minimum spanning tree is the following")
    print(min_spanning_tree)
    print(f"The total cost of the minimum spanning tree is {cost}")

if __name__ == '__main__':
    main()

# The minimum spanning tree is the following
# A -> C
# B -> D B -> C
# C -> F
# D -> E
# E -> G
# F -> None
# G -> H
# H -> I
# I -> None

# The total cost of the minimum spanning tree is 18