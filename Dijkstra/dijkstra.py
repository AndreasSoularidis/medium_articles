import math
from graph import Graph, Node

''' Vertex extends the class Node and represents each vertex in the graph'''
class Vertex(Node):
    def __init__(self, value, neighbors=None):
        super().__init__(value, neighbors)
        self.length_from_start = math.inf
        self.previous_node = None
        self.visited = False
    

    ''' Return the distance from a given neighbor'''
    def distance_from_neighbor(self, node):
        for neighbor in self.neighbors:
            if neighbor[0].value == node.value:
                return neighbor[1]
        return None

    def __str__(self):
       return f"{self.value} {self.length_from_start} {self.previous_node} {self.visited}"



''' Represent the Dijkstra Algorithm '''
class Dijkstra:
    def __init__(self, graph, start, target):
        self.graph = graph
        self.start = start
        self.target = target
        self.intialization()

    ''' Initialize the labels of each vertex '''
    def intialization(self):
        for node in self.graph.nodes:
            if node == self.start:
                node.length_from_start = 0
    

    ''' Calculate the return the node with the minimum distance from the source node '''
    def minimum_distance(self):
        next_node = None
        min_value = math.inf
        for node in self.graph.nodes:
            if node.length_from_start < min_value and node.visited == False:
                min_value = node.length_from_start
                next_node = node

        return next_node                


    ''' The core of the algorithm. Execute the repetitive steps of Dijkstra'''
    def execution(self):
        target_node = self.graph.find_node(self.target)
        while not target_node.visited:
            # # Select the node with the minimun distrance from start
            selected_node = self.minimum_distance()
            # Update the status of the node (visited = True)
            selected_node.visited = True
            # Update the labels of the neighbors
            for node in selected_node.neighbors:
                connected_node = self.graph.find_node(node[0])
                
                if (selected_node.length_from_start + node[1]) < connected_node.length_from_start:
                    connected_node.length_from_start = selected_node.length_from_start + node[1]
                    connected_node.previous_node = selected_node.value

        # Calculate the path from the source node to target node
        path = [target_node.value]
        while True:
            node = self.graph.find_node(path[-1])
            if node.previous_node is None:
                break
            path.append(node.previous_node)
        
        path.reverse()    
        return path, target_node.length_from_start
        


def main():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Vertex('V1'))
    graph.add_node(Vertex('V2'))
    graph.add_node(Vertex('V3'))
    graph.add_node(Vertex('V4'))
    graph.add_node(Vertex('V5'))
    graph.add_node(Vertex('V6'))
    # Add edges
    graph.add_edge('V1', 'V2', 9)
    graph.add_edge('V1', 'V3', 4)
    graph.add_edge('V2', 'V3', 2)
    graph.add_edge('V2', 'V4', 7)
    graph.add_edge('V2', 'V5', 3)
    graph.add_edge('V3', 'V4', 1)
    graph.add_edge('V3', 'V5', 6)
    graph.add_edge('V4', 'V5', 4)
    graph.add_edge('V4', 'V6', 8)
    graph.add_edge('V5', 'V6', 2)

    # Execute the algorithm
    alg = Dijkstra(graph, "V1", "V6")
    path, path_lenght = alg.execution()
    print(" -> ".join(path))
    print(f"Length of the path: {path_lenght}")

if __name__ == '__main__':
    main()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 11