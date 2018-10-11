from bst import BST

"""
The test tree should look like:
              hello
          are       world
       and        how    you
                    war
                  peace
"""
values = [ 'hello', 'world', 'how', 'are', 'you', 'war', 'and', 'peace' ]

print( 'original data ...' )

mydata = BST()
for v in values:
    print( v, end = ', ' )
    mydata.add( v, v )    # v is both key and data
print()

mydata.print()

print( 'inorder traversal should be in sorted order ...' )
print( 'the result should be : and, are, hello, how, peace, war, world, you' )
print( 'the result is : ', end = '' )
for x in mydata:
    print( x, end = ', ' )
print()

print( 'search for "world", should be True : ', 'world' in mydata )
print( 'search for "and", should be True: ', 'and' in mydata )
print( 'search for "you", should be True : ', 'you' in mydata )
print( 'search for "me", should be False : ', 'me' in mydata )
print( 'find minimum "and", should be found : ', mydata.findMin() )
print( 'find minimum "you", should be found : ', mydata.findMax() )

mydata.remove( 'war' )
print( 'deleting "war", the result should be: and, are, hello, how, peace, world, you' )
print( 'the result is : ', end = '' )
for x in mydata:
    print( x, end = ', ' )
print()
    
mydata.remove( 'world' )
print( 'deleting "world", the result should be: and, are, hello, how, peace, you' )
print( 'the result is : ', end = '' )
for x in mydata:
    print( x, end = ', ' )
print()
    

