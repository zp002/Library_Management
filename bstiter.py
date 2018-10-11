class _BSTIterator :      
  def __init__( self, root ):
     # Creates the Python list and fills it with the keys.
    self._theKeys = list()
    self._curItem = 0    # Keep track of the next location in the array.
    self._bstTraversal( root )     
    self._curItem = 0    # Reset the current item index.
    
  def __iter__( self ):
    return self

   # Returns the next key from the array of keys 
  def __next__( self ):
    if self._curItem < len( self._theKeys ) :
      key = self._theKeys[ self._curItem ]
      self._curItem += 1
      return key
    else :
      raise StopIteration
      
   # Performs an inorder traversal used to build the array of keys. 
  def _bstTraversal( self, subtree ):
    if subtree is not None :
      self._bstTraversal( subtree.left )
      self._theKeys.append( subtree.key )
      self._curItem += 1
      self._bstTraversal( subtree.right )       
