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


  def set_child(self, branch, child):
    """
      Add a child node as left or right child to the current node

      Parameters
      ----------
      branch : str
        Determine if the child will be either on the left or on the right 
      child : Node
        Represent the child node
    """
    if branch == "left":
      self.left_child = child
    else:
      self.right_child = child


  def __str__(self):
    return str(self.value)

  

class MyTree:
  """
    Create a new tree

    Parameters
    ----------
    root : Node
      Represent the root of the tree
  """
  def __init__(self, root):
    self.root = root

  
  def preorder(self, node):
    """
      Generate the preorder traverse of the tree

      Parameters
      ----------
      node : Node
        Represent the current node in the traversal
      
      Returns
      -------
      The preorder traversal
    """
    if node:
      print(node, end=" ")
      self.preorder(node.left_child)
      self.preorder(node.right_child)


  def inorder(self, node):
    """
      Generate the inroder traverse of the tree

      Parameters
      ----------
      node : Node
        Represent the current node in the traversal
      
      Returns
      -------
      The inorder traversal
    """
    if node:
      self.inorder(node.left_child)
      print(node, end=" ")
      self.inorder(node.right_child)


  def postorder(self, node):
    """
      Generate the postorder traverse of the tree

      Parameters
      ----------
      node : Node
        Represent the current node in the traversal
      
      Returns
      -------
      The postorder traversal
    """
    if node:
      self.postorder(node.left_child)
      self.postorder(node.right_child)
      print(node, end=" ")
      
# Create the nodes of the tree
a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")

# Set the hierarchy between the nodes
a.set_child("left", b)
a.set_child("right", c)

b.set_child("left", d)
b.set_child("right", e)

c.set_child("right", f)

# Creata the tree setting up the root node
tree = MyTree(a)

# Execute the traversal
print("Preorder Traversal")
tree.preorder(a)
print("\n")

# >>> Preorder Traversal
# >>> A B D E C F

print("Inorder Traversal")
tree.inorder(a)
print("\n")

# >>> Inorder Traversal  
# >>> D B E A C F  

print("Postorder Traversal")
tree.postorder(a)

# >>> Postorder Traversal
# >>> D E B F C A 




