from math import inf 

class Node:
    """ 
        This class used to represent each Vertex in the graph 
        ...
        Attributes
        ----------
        value : str
            Represent the value of the node
        x : int
            Represent the x-coordinate of the node
        y : int
            Represent the y-coordinate of the node
        heuristic_value : int
            Coresponds to the manhattan distance plus the distance from the inital node to the current node. Default value is -1
        distance_from_start
            Corresponds to the distance of the node from the initial node. Defaul value is -1
        neighbors : list
            A list with the nodes the current node is connected
        parent : Node
            Represents the parent-node of the current node. Default value is None

        ...
        Methods
        -------
        has_neighbors(self) -> Boolean
            Check if the current node is connected with other nodes (return True). Otherwise return False
        number_of_neighbors(self) -> int
            Calculate and return the number the of the neighbors 
        add_neighboor(self, neighboor) -> None
            Add a new neighbor in the list of neighbors
        extend_node(self) -> list
            return a list of nodes with which the current node is connected 
        __eq__(self, other) -> Boolean
            Determines if two nodes are equal or not, checking their values
        __str__(self) -> str
            Prints the node data
    """

    def __init__(self, value, cordinates, neighbors=None):
        self.value = value
        self.x = cordinates[0]
        self.y = cordinates[1]
        self.heuristic_value = -1
        self.distance_from_start = inf
        if neighbors is None:
            self.neighbors = []
        else:
            self.neighbors = neighbors
        self.parent = None


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

    ''' '''
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
    

    def extend_node(self):
        """
            Extends the current node, creating and returning a list with all connected nodes
            Returns
            -------
                List
        """
        children = []
        for child in self.neighbors:
            children.append(child[0])
        return children
    

    def __gt__(self, other):
        """
            Define which node, between current node and other node, has the greater value. 
            First examine the heuristic value. If this value is the same for both nodes 
            the function checks the lexicographic series
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        if isinstance(other, Node):
            if self.heuristic_value > other.heuristic_value:
                return True
            if self.heuristic_value < other.heuristic_value:
                return False
            return self.value > other.value
            

    def __eq__(self, other):
        """
            Define if current node and other node are equal, checking their values. 
            Parameters
            ----------
                other: Node:
                    Represent the other node with which the current node is compared
            Returns
            -------
                Boolean
        """
        if isinstance(other, Node):
            return self.value == other.value
        return self.value == other


    def __str__(self):
        """
            Define that a node is printed with its value. 
            Returns
            -------
                str
        """
        return self.value
        

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