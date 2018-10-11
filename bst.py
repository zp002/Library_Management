from bstiter import _BSTIterator

"""Binar Search Tree"""
class BST:

  def __init__( self ):
    """ Creates an empty binary search tree."""
    self._root = None
    self._size = 0
      
  def __len__( self ):
    """Returns the number of entries in the bst."""
    return self._size

  def print( self ):
    if self._root != None:
      self._root.print()

  def __contains__( self, key ):
    """Determines if the map contains the given key."""
    return self._bstSearch( self._root, key ) is not None

  def getValue( self, key ):
    """Look for the value for a given key"""
    node = self._bstSearch( self._root, key )
    if node != None:
      return node.value
    else:
      return None

  def sort( self ):
    """Produce a sorted list of entries based on the 'key'"""
    result = []    # result list
    result = self._sort( self._root, result )
    return result

  def add( self, key, value ):
    """Adds a new entry to binary search tree."""
    # Find the node containing the key, if it exists.
    node = self._bstSearch( self._root, key )    
    # If the key is already in the tree, update its value.
    if node is not None :
      node.value = value
      return False
    # Otherwise, add a new entry.
    else :
      self._root = self._bstInsert( self._root, key, value )
      self._size += 1
      return True
     
  def remove( self, key ):
    """Removes the entry associated with the given key."""
#    assert key in self, "Invalid key to remove."
    node = self._bstRemove( self._root, key )
    if node != None:
      self._root = node
    self._size -= 1

  def findMin( self ):
    """Find the minimum of this bst"""
    return self._bstFindMin( self._root )

  def findMax( self ):
    """Find the maximum of this bst"""
    return self._bstFindMax( self._root )

  def __iter__( self ):
    """Returns an iterator for traversing the keys in the bst. """
    return _BSTIterator( self._root )

  def _sort( self, node, result ):
    """Helper function to produce a sorted list based on 'key'"""
    if node != None:
      self._sort( node.left, result )
      result.append( node.value )
      self._sort( node.right, result )
      return result

  def _bstInsert( self, subtree, key, value ):
    """Helper method that inserts a new item, recursively."""
    if subtree is None :   
      subtree = _BSTNode( key, value )
    elif key < subtree.key :
      subtree.left = self._bstInsert( subtree.left, key, value )
    elif key > subtree.key :
      subtree.right = self._bstInsert( subtree.right, key, value )
    return subtree

  def _bstSearch( self, subtree, target ):        
    """Helper method that recursively searches the tree for a target key."""
    if subtree is None :         # base case, not found
      return None
    elif target < subtree.key :  # target is left of the subtree root.
      return self._bstSearch( subtree.left, target )
    elif target > subtree.key :  # target is right of the subtree root.
      return self._bstSearch( subtree.right,target )       
    else :                       # base case, found!
      return subtree                                
  
  def _bstFindMin( self, subtree ):
    """Helper method for finding the node containing the minimum key."""
    if subtree is None :     
      return None
    elif subtree.left is None : 
      return subtree
    else :
      return self._bstFindMin( subtree.left )
  
  def _bstFindMax( self, subtree ):
    """Helper method for finding the node containing the maximum key."""
    if subtree is None :     
      return None
    elif subtree.right is None : 
      return subtree
    else :
      return self._bstFindMax( subtree.right )
  
  def _bstRemove( self, subtree, target ):
    """Helper method that removes an existing item recursively."""
    # Search for the item in the tree.
    if subtree is None :  
      return subtree
    elif target < subtree.key :
      subtree.left = self._bstRemove( subtree.left, target )
      return subtree
    elif target > subtree.key :
      subtree.right = self._bstRemove( subtree.right, target )
      return subtree      
    else :     # We found the node containing the item, delete it.
      return self._bstDeleteNode( subtree )
        
  def _bstDeleteNode( self, node ):
    """Delete this BST node"""

    if node.left is None and node.right is None :   # leaf node
        return None
    elif node.left is None or node.right is None :  # one child
      if node.left is not None :
        return node.left
      else :
        return node.right
    else :  # two children, find in-order successor, replace current with it
      successor = self._bstFindMin( node.right )
      node.key = successor.key
      node.value = successor.value
      node.right = self._bstRemove( node.right, successor.key )
      return node

# Storage class for the binary search tree nodes
class _BSTNode :                       
  def __init__( self, key, value ):
    self.key = key
    self.value = value
    self.left = None
    self.right = None

  def __str__( self ):
    return str( self.value )

  def print(self):
    """ Print out the tree rooted at this node. """
    lines = []
    strings = []
    self.printNodes(lines, strings)
    st = ""
    for string in strings:
      st = st + string
    print(st)
      
  def printNodes(self, lines, strings):
    """ Helper function for print(). """
    level = len(lines)
    if self.right != None:
      lines.append(False)
      self.printLines(lines, strings, "\n")
      self.right.printNodes(lines, strings)
      lines.pop(level)
    else:
      self.printLines(lines, strings, "\n")

    if level>0:
      old = lines.pop(level-1)
      self.printLines(lines, strings, "  +--")
      lines.append(not old)
    strings.append(str(self.key) + "\n")
        
    if self.left != None:
      lines.append(True)
      self.left.printNodes(lines, strings)
      self.printLines(lines, strings, "\n")
      lines.pop(level)
    else:
      self.printLines(lines, strings, "\n")

  def printLines(self, lines, strings, suffix):
    """ Helper function for print(). """
    for line in lines:
      if line: strings.append("  |  ")
      else:    strings.append("     ")
    strings.append(suffix)

