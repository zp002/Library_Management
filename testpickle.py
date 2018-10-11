import pickle
"""
This is a simple example of using Python pickle
"""
class Book:
    """A piece of data"""
    def __init__( self, t, a ):
        """Constructor with a title and an author"""
        self.title = t
        self.author = a

    def __str__( self ):
        """String representation of the object"""
        return self.author + ' ' + self.title


b = Book( 'hello', 'someone' )
c = Book( 'world', 'someone else' )
print( 'before pickle ' )
print( b )
print( c )
## To create a pickle file, uncomment the following three lines.
f = open( 'data.pickle', 'wb' )
pickle.dump( b, f )
pickle.dump( c, f )

## The following three lines are used after the pickle file has been created.
f = open( 'data.pickle', 'rb' )
b = pickle.load( f )
c = pickle.load( f )
print( 'after pickle ' )
print( b )
print( c )

f.close()
