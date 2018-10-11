#from avltree_derived import AVLTree
from avltree_student import AVLTree


"""
The resultant test tree should look like:
       +--100
       |  
  +--80
  |    |  
  |    +--60
  |       
  |       
35
  |  
  +--25
       |  
       +--17
          
"""
#values = [ 60, 25, 35, 100, 17, 80 ] # textbook example p 434 f 14.20

"""
The next tree should look like:
            +--100
            |  
       +--80
       |    |  
       |    +--60
       |       
       |       
  +--35
  |    |       
  |    |       
  |    |    +--33
  |    |    |  
  |    +--30
  |       
  |       
28
  |       
  |       
  |    +--27
  |    |  
  +--25
       |  
       +--17
            |  
            +--12
"""
#values = [ 60, 25, 35, 100, 17, 80, 30, 28, 27, 33, 12 ] # modified example

"""
       +--11
       |  
  +--10
  |  
9
  |       
  |            
  |            
  |         +--6
  |         |  
  |    +--5
  |    |    |  
  |    |    +--2
  |    |       
  |    |       
  +--1
       |  
       +--0
            |  
            +---1

"""
values = [ 9, 5, 10, 0, 6, 11, -1, 1, 2 ]
print( 'original data ...' )

mydata = AVLTree()

for v in values:
    print( v, end = ', ' )
    mydata.add( v, v )    # v is both key and data
mydata.print()
print()


print( 'inorder traversal should be in sorted order ...' )
#print( 'the result should be : [ 17, 25, 35, 60, 80, 100 ]' )
print( 'the result should be : ', sorted( values ) )
print( 'the result is : ', end = '' )
for x in mydata:
    print( x, end = ', ' )
print()

print( 'search for "17", should be False : ', 17 in mydata )
print( 'search for "100", should be False : ', 100 in mydata )
print( 'search for "35", should be False : ', 35 in mydata )
print( 'search for "0", should be True : ', 0 in mydata )


values = [ 9, 5, 10, 0, 6, 11, -1, 1, 2 ]
for v in values:
    mydata.add( v, v)
mydata.print()
print()
"""
       +--11
       |  
  +--10
  |  
9
  |       
  |            
  |            
  |         +--6
  |         |  
  |    +--5
  |    |    |  
  |    |    +--2
  |    |       
  |    |       
  +--1
       |  
       +--0
            |  
            +---1
          
"""
values.remove( 10 )
mydata.remove( 10 )
print( 'removing 10 from the avl tree ...')
print( 'the result should be ', sorted( values ) )
for x in mydata:
    print( x, end = ', ' )
print()
mydata.print()
"""
          
       +--11
       |  
  +--9
  |    |       
  |    |       
  |    |    +--6
  |    |    |  
  |    +--5
  |         |  
  |         +--2
  |            
  |            
  |       
1
  |  
  +--0
       |  
       +---1
          
"""
values.remove( 1 )
mydata.remove( 1 )
print( 'removing 1 from the avl tree ...')
print( 'the result should be ', sorted( values ) )
for x in mydata:
    print( x, end = ', ' )
print()
mydata.print()
"""
          
       +--11
       |  
  +--9
  |    |       
  |    |       
  |    |    +--6
  |    |    |  
  |    +--5
  |       
  |       
2
  |  
  +--0
       |  
       +---1
"""
values.remove( -1 )
mydata.remove( -1 )
print( 'removing -1 from the avl tree ...')
print( 'the result should be ', sorted( values ) )
for x in mydata:
    print( x, end = ', ' )
print()
mydata.print()
"""
       +--11
       |  
  +--9
  |    |  
  |    +--6
  |       
  |       
5
  |  
  +--2
       |  
       +--0
"""
