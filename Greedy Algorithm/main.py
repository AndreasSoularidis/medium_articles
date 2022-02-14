from graph import Graph, Node
from greedy_algorithm import Greedy

def run():
    # Create graph
    graph = Graph()
    # Add vertices
    graph.add_node(Node('S', (0, 0)))
    graph.add_node(Node('B', (0, 1)))
    graph.add_node(Node('C', (0, 3)))
    graph.add_node(Node('D', (1, 0)))
    graph.add_node(Node('E', (1, 1)))
    graph.add_node(Node('F', (1, 2)))
    graph.add_node(Node('G', (1 ,3)))
    graph.add_node(Node('H', (2, 0)))
    graph.add_node(Node('I', (2, 3)))
    graph.add_node(Node('J', (3, 0)))
    graph.add_node(Node('K', (3, 1)))
    graph.add_node(Node('T', (3, 2)))
    graph.add_node(Node('M', (3, 3)))
    
    # Add edges
    graph.add_edge('S', 'B')
    graph.add_edge('S', 'D')
    graph.add_edge('B', 'E')
    graph.add_edge('C', 'G')
    graph.add_edge('D', 'E')
    graph.add_edge('D', 'H')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'G')
    graph.add_edge('G', 'I')
    graph.add_edge('H', 'J')
    graph.add_edge('I', 'M')
    graph.add_edge('J', 'K')
    graph.add_edge('K', 'T')
    graph.add_edge('T', 'M')

    # Execute the algorithm
    alg = Greedy(graph, "S", "T")
    path, path_length = alg.search()
    print(" -> ".join(path))
    print(f"Length of the path: {path_length}")

if __name__ == '__main__':
  run()

# S -> B -> E -> F -> G -> I -> M -> T
# Length of the path: 8