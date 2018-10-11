from bstiter import _BSTIterator
"""
This is a partial implementation of the AVL tree ADT.
All functionality of an AVL tree is present except AVL tree
deletion, which may be left as an exercise for students.

This implementation of avl tree is based on the following notes
http://www.geeksforgeeks.org/archives/18009
and the notes from our textbook by Necaise

There are other, possibly better implementations. But this
one closely follow the notion in our textbook.

CSCI 204 Fall 2012
A. Kurdia and X. Meng
"""
class AVLTree:

  def __init__( self ):
    """ Creates an empty binary search tree."""
    self._root = None
    self._size = 0
      
  def __len__( self ):
    """Returns the number of entries in the bst."""
    return self._size

  def __iter__( self ):
    """Returns an iterator for traversing the keys in the bst. """
    return _BSTIterator( self._root )

  def print( self ):
    if self._root != None:
      self._root.print()

  def __contains__( self, key ):
    """Determines if the map contains the given key."""
    return self._bstSearch( self._root, key ) is not None

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
  
  def _avlRotateRight( self, pivot ):
    """ Rotates the pivot to the right around its left child.   """
    # Set C to be the left of pivot and S2 to be the right of C
    # See Necaise Fig 14.17, page 431
    C  = pivot.left
    S2 = C.right

    C.right = pivot   # C.left and pivot.right unchanged
    pivot.left = S2

    # update the height
    pivot.height = max( self.getHeight( pivot.left ), \
                          self.getHeight( pivot.right ) ) + 1
    C.height = max( self.getHeight( C.left ), \
                      self.getHeight( C.right ) ) + 1

    # return the new root
    return C
    
  def _avlRotateLeft( self, pivot ):
    """ Rotates the pivot to the left around its right child.  """
    # Set C to be the right of pivot and S2 to be left of C
    # See Necaise Fig 14.19, page 433
    C  = pivot.right
    S2 = C.left

    C.left = pivot    # C.right and pivot.left unchanged
    pivot.right = S2

    # update the height
    pivot.height = max( self.getHeight( pivot.left ), \
                          self.getHeight( pivot.right ) ) + 1
    C.height = max( self.getHeight( C.left ), \
                      self.getHeight( C.right ) ) + 1

    # return the new root
    return C
            
  def getHeight( self, node ):
    """Return the height of the node"""
    if node == None:
      return 0
    else:
      return node.height
  
  def getBalance( self, node ):
    """Return the 'balance factor'"""
    if node == None:
      return 0
    return self.getHeight( node.left ) - self.getHeight( node.right )

  def add( self, key, value ):
    """Add a new node with key and value into this avl tree."""
    node = self._bstSearch( self._root, key )    
    if node is not None :
      node.value = value
      return False
    else :
      self._root = self._avlInsert( self._root, key, value )
      self._size += 1
      return True
    
  def _avlInsert( self, subtree, key, newitem ):  
    """Help method to insert the node into the tree"""

    # 1. perform normal BST insertion
    # See if we have found the insertion point. 
    if subtree is None :    
      subtree = _AVLTreeNode( key, newitem )
      return subtree

    # See if we need to navigate to the left.
    elif key < subtree.key : 
      subtree.left = self._avlInsert( subtree.left, key, newitem )      
          
    # Otherwise, navigate to the right.
    else : # key > subtree.key
      subtree.right = self._avlInsert( subtree.right, key, newitem )      
  
    # 2. update the height of this node
    subtree.height = max( self.getHeight( subtree.left ), \
                            self.getHeight( subtree.right ) ) + 1

    # 3. get the balance factor
    balance = self.getBalance( subtree )

    # If the subtree becomes unbalanced, four cases need to be dealt with
    # Refer to discussions in page 431 - 433 of textbook Necaise
    # Case 1: new node in branch of subtree.left.left, height of 
    #         that branch is too big, rotate right
    if balance > 1 and key < subtree.left.key:
      subtree = self._avlRotateRight( subtree )
      return subtree
    # Case 2: new node in branch of subtree.left.right, height of
    #         that branch is too big, rotate left around subtree.left,
    #         then rotate right around subtree
    elif balance > 1 and key > subtree.left.key:
      subtree.left = self._avlRotateLeft( subtree.left )
      subtree = self._avlRotateRight( subtree )
      return subtree
    # Case 3: new node in branch of subtree.right.right, height of 
    #         that branch is too big, rotate left
    elif balance < -1 and key > subtree.right.key:
      subtree = self._avlRotateLeft( subtree )
      return subtree
    # Case 4: new node in branch of subtree.right.left, height of
    #         that branch is too big, rotate right around subtree.right,
    #         then rotate left around subtree
    elif balance < -1 and key < subtree.right.key:
      subtree.right = self._avlRotateRight( subtree.right )
      subtree = self._avlRotateLeft( subtree )
      return subtree

    # Return the results. 
    return subtree
    
  def remove( self, key ):
    """Remove a node from the tree"""
    assert key in self, "Invalid map key."
    self._root = self._avlRemove( self._root, key )
    self._size -= 1
    
  def _avlRemove( self, subtree, key ):
    """Helper method to remove the node"""
    assert False, "Method needs to be implemented."

  def _avlDeleteNode( self, node ):
    """Delete this AVL node"""

    if node.left is None and node.right is None :   # leaf node
        return None
    elif node.left is None or node.right is None :  # one child
      if node.left is not None :
        return node.left
      else :
        return node.right
    else :  # two children, find in-order successor, replace current with it
      successor = self._avlFindMin( node.right )
      node.key = successor.key
      node.value = successor.value
      node.right = self._avlRemove( node.right, successor.key )
      return node

  def _avlFindMin( self, subtree ):
    """Helper method for finding the node containing the minimum key."""
    if subtree is None :     
      return None
    elif subtree.left is None : 
      return subtree
    else :
      return self._avlFindMin( subtree.left )
  


# Storage class for the binary search tree nodes
class _AVLTreeNode :                       
  def __init__( self, key, value ):
    self.key = key
    self.height = 1
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
    strings.append( str(self.key) + "\n")
        
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

