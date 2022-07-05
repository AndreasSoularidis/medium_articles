class MaxHeap:
  def __init__(self):
    """
      This class represent a Max Heap data structure
    """
    self.heap = []

  def insert(self, node):
    """
      Insert a new node in the heap data strucutre
      
      Parameters
      ----------
      node : int
        Represent the new node
    """
    # Add the new node at the end of the list
    self.heap.append(node)
    # Get the index of the node
    position_of_node = self.heap.index(node)
    
    # Place the node in the proper position
    while True:
      if position_of_node == 0:
        break
      parent_of_node = (position_of_node - 1) // 2
      if self.heap[position_of_node] <= self.heap[parent_of_node]:
        break 
      else:
        self.heap[position_of_node], self.heap[parent_of_node] = self.heap[parent_of_node], self.heap[position_of_node]
        # Get the updated index of the node
        position_of_node = self.heap.index(node)


  def delete(self):
    """
      Delete and return the root node from the heap data strucutre

      Return
      ------
      node : int
    """
    # Remove the root
    deleted_node = self.heap.pop(0)

    if len(self.heap) == 0:
      return deleted_node

    # Set the last node as root
    node = self.heap.pop()
    self.heap.insert(0, node)

    # Place the new root node in its right position
    index_node = 0
    while True:
      # Get the index of each child of node
      index_of_children = self._find_children(index_node)
      # The node has two children
      if(len(index_of_children) == 2):
        if self.heap[index_node] >= self.heap[index_of_children[0]] and self.heap[index_node] >= self.heap[index_of_children[1]]:
          break
        # Find the node with the greatest value between its children
        max_child = max(self.heap[index_of_children[0]], self.heap[index_of_children[1]])
        max_index = self.heap.index(max_child)
        # Swap 
        self.heap[index_node], self.heap[max_index] = self.heap[max_index], self.heap[index_node]
        index_node = self.heap.index(node)
      # The node has one child
      elif(len(index_of_children) == 1):
        if self.heap[index_node] >= self.heap[index_of_children[0]]:
          break
        # Swap
        self.heap[index_node], self.heap[index_of_children[0]] = self.heap[index_of_children[0]], self.heap[index_node]
        index_node = self.heap.index(node)
      # The node has not any child
      else: break

    return deleted_node


  def heap_sort(self):
    """
      Execute the heap sort algorithm, calling iteratively the delete method of the class
      that remove and return the root node from the structure. The returned value is stored 
      in a list. Finally the list is retuned

      Return
      ------
      List : int
    """
    sorted_list = []
    for _ in range(len(self.heap)):
      sorted_list.append(self.delete())
    return sorted_list


  def _find_children(self, index_node):
    """
      Find and return the nuber of children of the given node
      
      Parameters
      ----------
      index_node : int
        Represent the node, about which we are interested in learning about its children
      
      Return
      ------
      list : int
    """
    children = [2 * index_node + 1, 2 * index_node + 2]
    return [child for child in children if child <= len(self.heap)-1]


  def initialize(self, nodes):
    """
      Create the max heap calling iteratively the insert method. In each iteration the method insert
      a new node into the strucure
      
      Parameters
      ----------
      nodes : list
        Represent the nodes that must be inserted into the structure
      
    """
    for node in nodes:
      self.insert(node)   
  

  def __str__(self):
    """
      Print the heap data structure
    """
    return "[" + ", ".join([str(node) for node in self.heap]) + "]"


# Create the Max Heap
myHeap = MaxHeap()
nodes = [15, 9, 18, 26, 21, 12, 25, 16]
myHeap.initialize(nodes)
print("Initial Heap")
print(myHeap)

# Delete the root
print("\nDelete Node")
value = myHeap.delete()
print(f"The node with value {value} was deleted. The structure has the following form")
print(myHeap)

# Insert node 
print("\nInsert Node 26. The structure has the following form")
myHeap.insert(26)
print(myHeap)

# Heap Sort Algorithm
print("\nHeap Sort Algorithm")
sorted_list = myHeap.head_sort()
print("The sorted list is the following:")
print(sorted_list)