from graph import Graph, Node
from ucs_algorithm import UCS

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('V1'))
    graph.add_node(Node('V2'))
    graph.add_node(Node('V3'))
    graph.add_node(Node('V4'))
    graph.add_node(Node('V5'))
    graph.add_node(Node('V6'))
    
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
    alg = UCS(graph, "V1", "V6")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")

if __name__ == '__main__':
  run()

# V1 -> V3 -> V4 -> V5 -> V6
# Length of the path: 6