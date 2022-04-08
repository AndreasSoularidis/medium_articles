from graph import Graph, Node
from prim import Prim

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
    alg = Prim(graph, "A")
    tree, total_cost = alg.execution()
    print("Produced Minimum Spaning Tree by Prim's Algorithm")
    for node in tree:
        print(node)
    print(f"Total Cost: {total_cost}")

if __name__ == '__main__':
    main()

# Produced Minimum Spaning Tree by Prim's Algorithm
# None -> A
# A -> C
# C -> B
# B -> D
# D -> E
# C -> F
# E -> G
# G -> H
# H -> I
# Total Cost: 18