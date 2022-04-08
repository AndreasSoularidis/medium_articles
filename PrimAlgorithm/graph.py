import math 
class Node:
    """ 
        This class used to represent each Vertex in the graph 
        ...
        Attributes
        ----------
        value : str
            Represent the value of the node
        neighbors : list
            A list with the nodes the current node is connected
        length_from_previous_node
            The weight of the edge from the previous node
        previous_node
            Represents the previous node
        visited
            Indicates whether the node has been visited or not
        ...
        Methods
        -------
        has_neighbors(self) -> Boolean
            Check if the current node is connected with other nodes (return True). Otherwise return False
        number_of_neighbors(self) -> int
            Calculate and return the number the of the neighbors 
        add_neighboor(self, neighboor) -> None
            Add a new neighbor in the list of neighbors
        __eq__(self, other) -> Boolean
            Determines if two nodes are equal or not, checking their values
        __gt__(self, other) -> Boolean
            Determines which of the node is greater than the other
        __str__(self) -> str
            Returns the node and the previous node in the produced tree
    """

    def __init__(self, value, neighbors=None):
        self.value = value
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.length_from_previous_node = math.inf
        self.previous_node = None
        self.visited = False


    def has_neighbors(self):
        """
            Return True if the current node is connected with at least another node.
            Otherwiese return false
        """
        if len(self.neighbors) == 0:
            return False
        return True


    def number_of_neighbors(self):
        """
            Return the number of nodes with which the current node is connected
        """
        return len(self.neighbors)


    def add_neighboor(self, neighboor):
        """
            Add a new node to the neighboor list. In other words create a new connection between the
            current node and the neighboor
            Paramenters
            ----------
            neighboor : node
                Represent the node with which a new connection is created
        """
        self.neighbors.append(neighboor)


    def __eq__(self, other):
        """
            Determines if two nodes are equal or not, checking their values
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        return self.value == other.value
    

    def __gt__(self, other):
        """
            Determines which of the two nodes are greater than the other, 
            comparing the length from the previous node for each of them. 
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        return self.length_from_previous_node > other.length_from_previous_node


    def __str__(self):
        """
           Return the node along with the previous node in the produced tree
            Returns
            -------
                str
        """
        return f"{self.previous_node} -> {self.value}"



class Graph:
    """ 
        This class used to represent the graph data structure.
        ...
        Attributes
        ----------
        nodes : list
            List with all the nodes of the graph
        ...
        Methods
        -------
        add_node(self, node) -> None
            Add a new node in the list of nodes
        find_node(self, value) -> Node
            Find and return the node of the graph with the given value.   
        add_edge(self, value1, value2, weight=1) -> None
            Add a new edge in the graph
        number_of_nodes(self) -> int
            Calculate and return the number of nodes of the graph
        are_connected(self, node_one, node_two) -> Boolean
            Check if the two given nodes are connected each other
        __str__(self) -> str
            Prints the nodes of the graph
    """
    def __init__(self, nodes=None):
        if nodes is None:
            self.nodes = []
        else:
            self.nodes = nodes


    def add_node(self, node):
        """
            Add a new node (vertex) in the grpah 
            Parameters
            ----------
                node: Node
                    Represent the nserted node in the graph
        """
        self.nodes.append(node)


    def find_node(self, value):
        """
            Return True if the node with the given value exist in the graph. Otherwise it return False
            Parameters
            ----------
                value: str
                    Is the value of the node we want to find
            ...
            Return
            ------
                Node
        """
        for node in self.nodes:
            if node.value == value:
                return node 
        return None


    def add_edge(self, value1, value2, weight=1):
        """
            Add a new edge between the two given nodes
            Parameters
            ----------
                value1: str
                    The value of the first node
                value2: str
                    The value of the second node 
                weight:
                    The weight of the edge. Default value 1
            ...
            Return
            ------
                Node
        """
        node1 = self.find_node(value1)        
        node2 = self.find_node(value2)

        if (node1 is not None) and (node2 is not None):
            node1.add_neighboor((node2, weight))
            node2.add_neighboor((node1, weight))
        else:
            print("Error: One or more nodes were not found")


    def number_of_nodes(self):
        """
            Return the number of nodes of the graph
            ...
            Return
            ------
                int
        """
        return f"The graph has {len(self.nodes)} nodes"


    def are_connected(self, node_one, node_two):
        """
            Return True if the given nodes are connected. Otherwise return False
            ...
            Parameters
            ----------
                node_one: str
                    The value of the first node
                node_two: str
                    The value of the second node
            Return
            ------
                Boolean
        """
        node_one = self.find_node(node_one)
        node_two = self.find_node(node_two)

        for neighboor in node_one.neighbors:
            if neighboor[0].value == node_two.value:
                return True
        return False


    def __str__(self):
        """
            Define the way the nodes of graph will be printed. 
            Return
            ------
                str
        """
        graph = ""
        for node in self.nodes:
            graph += f"{node.__str__()}\n" 
        return graph