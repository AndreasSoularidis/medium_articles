from graph import Graph, Node
from a_star import AStar

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('S', (1,1)))
    graph.add_node(Node('B', (1,2)))
    graph.add_node(Node('C', (1,4)))
    graph.add_node(Node('D', (2,1)))
    graph.add_node(Node('E', (2,2)))
    graph.add_node(Node('F', (2,3)))
    graph.add_node(Node('G', (2,4)))
    graph.add_node(Node('H', (3,1)))
    graph.add_node(Node('I', (3,4)))
    graph.add_node(Node('J', (4,1)))
    graph.add_node(Node('K', (4,2)))
    graph.add_node(Node('T', (4,3)))
    graph.add_node(Node('L', (4,4)))
    
    # Add edges
    graph.add_edge('S', 'B', 4)
    graph.add_edge('S', 'D', 5)
    graph.add_edge('B', 'E', 1)
    graph.add_edge('C', 'G', 1)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'H', 3)
    graph.add_edge('E', 'F', 6)
    graph.add_edge('F', 'G', 4)
    graph.add_edge('G', 'I', 3)
    graph.add_edge('H', 'J', 1)
    graph.add_edge('I', 'L', 4)
    graph.add_edge('J', 'K', 6)
    graph.add_edge('K', 'T', 2)
    graph.add_edge('T', 'L', 3)

    # Execute the algorithm
    alg = AStar(graph, "S", "T")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")

if __name__ == '__main__':
  run()

# S -> D -> H -> J -> K -> T
# Length of the path: 17