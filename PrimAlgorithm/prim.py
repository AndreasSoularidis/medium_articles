
from graph import Graph, Node    

class Prim:
    """
        This class used to represent the Prim's Algorithm
        ...
        Attributes
        ----------
        graph : Graph
        Represent the graph (search space of the problem) 
        start : str
        Represent the starting point 
        tree : list
        Represent the the produced tree
        vertices : list
        Represent the list with all the vertices of the graph
       
        ...
        Methods
        -------
        calculate_total_cost(self) -> int
            Calculate the total cost of the Minimum Spanning Tree
        execution(self)
            Implements the core of algorithm. This method constructs step by step the minimum spanning tree of the given graph 
    """
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.tree = []
        self.vertices = self.graph.nodes


    def calculate_total_cost(self):
        """
            Calculate and return the total cost of the Minimum Spanning Tree
            Return 
            ------
                int
        """
        total_cost = 0
        for node in self.tree:
            total_cost += node.length_from_previous_node
        return total_cost


    def execution(self):
        """
            Is the main algorithm. Constructs the Minimum Spanning Tree of a given graph.
            ...
            Return
            ------
                list, int
        """
        # Set the length of the start node equals to 0
        selected_node = self.graph.find_node(self.start)
        selected_node.length_from_previous_node = 0
        # Mark the selected node as visisted
        selected_node.visited = True
        self.vertices.remove(selected_node)
        # Add the selected node to the tree
        self.tree.append(selected_node)
        # For each child of the selected node, calculate the distance between parent(selected_node) and child
        for node in selected_node.neighbors:
            child = node[0]
            if node[1] < child.length_from_previous_node:
                child.length_from_previous_node = node[1]
                child.previous_node = selected_node.value

        while len(self.vertices) > 0:
            # Select the node with the minimun distance from the previous node
            self.vertices.sort()
            selected_node = self.vertices[0]
            selected_node.visited = True
            # Remove the selected node from the vertices set
            self.vertices.remove(selected_node)
            # Add the selected node to the tree
            self.tree.append(selected_node)
            # For each child of the selected node, calculate the distance between parent(selected_node) and 
            for node in selected_node.neighbors:
                child = node[0]
                if not child.visited:
                    if node[1] < child.length_from_previous_node:
                        child.length_from_previous_node = node[1]
                        child.previous_node = selected_node.value

        total_cost = self.calculate_total_cost()
        return self.tree, total_cost
        

