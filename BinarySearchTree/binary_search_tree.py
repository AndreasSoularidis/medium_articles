import random
class Node:
  def __init__(self, value, left_child=None, right_child=None):
    """
      Create a node (vertex) of the tree
      Parameters
      ----------
      value : int
        Represent the value stored in the node
      left_node : Node
        Represent the left child of the node
      right_node : Node
        Represent the right child of the node
    """
    self.value = value
    self.left_child = left_child
    self.right_child = right_child


  def is_leaf(self):
    """
      Return True if the node is a leaf (no children) or False if it has at least one child
      Return 
      ----------
      boolean
    """
    return self.left_child is None and self.right_child is None

  
  def __eq__(self, other):
    """
      Return True if the compared nodes are equal. Otherwise it return False
      Return 
      ----------
      boolean
    """
    if isinstance(other, Node):
      if self.value == other.value:
        return True
      return False
    
    if self.value == other:
      return True
    return False


  def __gt__(self, other):
    """
      Return True if the current node is greater than the other node
      Otherwise return False
      Return 
      ----------
      boolean
    """
    if isinstance(other, Node):
      if self.value > other.value:
        return True
      return False

    if self.value > other:
      return True
    return False

  def __str__(self):
    """
      Return the value of the node and its child or children if exist
      Otherwise return False
      Return 
      ----------
      boolean
    """
    s = f"Node {self.value}"
    if self.left_child is not None:
      s += f"\n Left Child: {self.left_child.value}"
    else:
      s += f"\n Left Child: -"
    if self.right_child is not None:
      s += f"\n Right Child: {self.right_child.value}"
    else:
      s += f"\n Right Child: -"
    s+= "\n"
    return s

  

class BinarySearchTree:
  """
    Create a new Binary Search Tree 
    Parameters
    ----------
    nodes : A list of nodes
      Represent the nodes of the tree
  """
  def __init__(self, nodes):
    self.nodes = nodes
    self.root = None


  def insert_node(self, node):
    """
      Insert a node to the Binary Search Tree, satisfying the properties of BST.
      Return True if the node is inserted successfully, otherwise it return False
      Parameters
      ----------
      node: Node
      Represent the inserted Node
      Return
      --------
      Boolean
    """
    # Insert the node in the list of nodes
    if node not in self.nodes:
      self.nodes.append(node)
    # Insert the root 
    if self.root is None:
      self.root = node
      return True

    # Find the right place for the node
    current_node = self.root
    while True:
      # The node already exists
      if node == current_node:
        return False
      # Search on the left subtree of current node
      if node < current_node:
        if not current_node.left_child:
          current_node.left_child = node
          return True
        current_node = current_node.left_child
      # Search on the right subtree of the current node
      else:
        if not current_node.right_child:
          current_node.right_child = node
          return True
        current_node = current_node.right_child


  def create_binary_tree(self):
    """
      Create the Binary Search Tree using the list of nodes 
    """
    for node in self.nodes:
      self.insert_node(node)

  
  def search(self, value):
    """
      Search if exist a node with the given value in the Binary Search Tree
      Parameters. Return True if the node with the given value exist, otherwise 
      return False
      ----------
      value: int
        Represent the value of the given node
      Return 
      ------
      Boolean
    """
    current_node = self.root

    while True:
      # The node was not found in the tree
      if current_node is None:
        return False

      # The node was founed in the tree
      if current_node.value == value:
        return True

      # Search in the left subtree of the current node
      if value < current_node.value:
        current_node = current_node.left_child
      
      # Search in the right subtree of the current node
      if value > current_node.value:
        current_node = current_node.right_child


  def delete(self, value):
    """
      Delete the node with the given value
      Return True if the node was deleted successfully, otherwise it returns False
      Parameters
      ----------
      value : int
        Represent the value of the given node
      Return 
      ------
      Boolean
    """
    current_node = self.root
    parent_node = None

    # Search for the given node
    while True:
      # The node was not found
      if current_node is None:
        return False
      
      # The node was found
      if current_node == value:
        break

      if value < current_node:
        parent_node = current_node
        current_node = current_node.left_child
      
      if value > current_node:
        parent_node = current_node
        current_node = current_node.right_child  

    if parent_node is None:
      parent_node = self.root
    # Node has no children
    if current_node.is_leaf():
      if parent_node.left_child == value:
        parent_node.left_child = None
        self.nodes.remove(current_node)
        return True
      
      parent_node.right_child = None
      self.nodes.remove(current_node)
      return True

    # Node has one child
    if current_node.left_child is not None and current_node.right_child is None:
      if parent_node.left_child == current_node:
        parent_node.left_child = current_node.left_child
      else:
        parent_node.right_child = current_node.left_child
      self.nodes.remove(current_node)
    
    elif current_node.left_child is None and current_node.right_child is not None:
      if parent_node.left_child == current_node:
        parent_node.left_child = current_node.right_child
      else:
        parent_node.right_child = current_node.right_child
      self.nodes.remove(current_node)
    else: # has two children
      if current_node.right_child.left_child is None:
        if parent_node.left_child == current_node:
          parent_node.left_child = current_node.right_child
          current_node.right_child.left_child = current_node.left_child
        else:
          parent_node.right_child = current_node.right_child
          current_node.right_child.left_child = current_node.left_child
        self.nodes.remove(current_node)
      else:
        next_node = current_node.right_child
        while next_node.left_child is not None:
          prev_node = next_node
          next_node = next_node.left_child

        prev_node.left_child = next_node.right_child
        
        next_node.right_child = current_node.right_child
        next_node.left_child = current_node.left_child

        if parent_node.left_child == current_node:
          parent_node.left_child = next_node
        else:
          parent_node.right_child = next_node
        self.nodes.remove(current_node)
    
  
  def __str__(self):
    """
      Return the structure of the Binary Search Tree
    """
    s = ""
    for node in self.nodes:
      s += node.__str__() + "\n"
    return s



#  Create nodes
numbers = [17, 24, 29, 4, 25, 2, 8, 23, 20, 21]
nodes = [Node(number) for number in numbers]

# Create Binary Tree
t = BinarySearchTree(nodes)
t.create_binary_tree()
print("Initial Binary Search Tree")
print(t)

# Insert node with value 9
t.insert_node(Node(9))
print("Binary Search Tree after the insertion of Node with value 9")
print(t)

# Search
values = [9, 30]
for value in values:
  print(f"Search the Node with value {value}")
  found = t.search(value)
  if found:
    print(f"The node with value {value} was found\n")
  else:
    print(f"The node with value {value} wasn't found\n")

# Deletion
values = [9, 8, 4, 17]
for value in values:
  print(f"Deletion of node with value {value}")
  t.delete(Node(value))
  print(t)
  # insert the node again to have the same examples with the article
  t.insert_node(Node(value))
