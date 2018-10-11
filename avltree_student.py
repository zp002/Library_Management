from bstiter import _BSTIterator
from bst import BST,_BSTNode
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
'''CSCI 204 Project 4 – Search and Sorting
    Due date: phase1: 12/5/2017
    Lab section: CSCI 204.L60, Tuesday 13-15:50
    Student name: Judy Peng
    Instructor name: Professor Hamid
''' 
class AVLTree(BST):
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
    if subtree is None:  
      return subtree
    if key < subtree.key :
      subtree.left = self._avlRemove( subtree.left, key )
    elif key > subtree.key :
      subtree.right = self._avlRemove( subtree.right, key)     
    else :     # We found the node containing the item, delete it.
      subtree = self._avlDeleteNode( subtree )
    if subtree is None:  
      return subtree
    # 2. update the height of this node
    subtree.height = max( self.getHeight( subtree.left ), \
                            self.getHeight( subtree.right ) ) + 1

    # 3. get the balance factor
    balance = self.getBalance( subtree )

    # If the subtree becomes unbalanced, four cases need to be dealt with
    # Refer to discussions in page 431 - 433 of textbook Necaise
    # Case 1: new node in branch of subtree.left.left, height of 
    #         that branch is too big, rotate right
    if balance > 1 and self.getBalance( subtree.left ) >= 0:
      subtree = self._avlRotateRight( subtree )
      return subtree
    # Case 2: new node in branch of subtree.left.right, height of
    #         that branch is too big, rotate left around subtree.left,
    #         then rotate right around subtree
    elif balance > 1 and self.getBalance( subtree.left ) < 0:
      subtree.left = self._avlRotateLeft( subtree.left )
      subtree = self._avlRotateRight( subtree )
      return subtree
    # Case 3: new node in branch of subtree.right.right, height of 
    #         that branch is too big, rotate left
    elif balance < -1 and self.getBalance( subtree.right ) <= 0:
      subtree = self._avlRotateLeft( subtree )
      return subtree
    # Case 4: new node in branch of subtree.right.left, height of
    #         that branch is too big, rotate right around subtree.right,
    #         then rotate left around subtree
    elif balance < -1 and self.getBalance( subtree.right ) > 0:
      subtree.right = self._avlRotateRight( subtree.right )
      subtree = self._avlRotateLeft( subtree )
      return subtree
    
    return subtree

    
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
class _AVLTreeNode(_BSTNode):                       
  def __init__( self, key, value ):
    super().__init__(key, value)
    self.height = 1
