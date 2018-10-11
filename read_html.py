class HTMLReader:

    def __init__( self, fname = 'test.html' ):
        self._infname = fname        # name of the data file
        self._html = HtmlPage()      # initialize an html page

        # self._data is a Python list of records, one for each author
        self._data = self._readData( self._infname )

    def __str__( self ):
        """ Build and return a string form of the data"""
        s = ''
        for x in self._data:
            s += str(x) + '\n'      # x is a Book object
        return s

    def _readData( self, filename ):
        """Read information from the input file
        The input file has the format of
        <p>author last name, first name</p>
        <ul>
           <li>book title 1</li>
           <li>book title 2</li>
        </ul>
        """

        # Create an empty list, each node is an author plus its books
        dataSet = []

        # Open file and read the entire contents as text
        f = open( filename, 'r' )
        lines = f.readlines()
        f.close()

        text = ''
        for line in lines:
            text += line
        
        # Skip to the beginning of <body>, copy it to 'head' of html
        headIndex = text.find( '<body>' )
        head = text[ 0 : (headIndex + 6) ]  # including '<body>'
        self._html.setHead( head )

        # Find trailer '</body>...', copy it to 'trailer' of html
        trailerIndex = text.rfind( '</body>' )
        trailer = text[ trailerIndex : len( text ) ]
        self._html.setTrailer( trailer )

        nextIndex = headIndex
        authorStart= text.find( '<p>', nextIndex )   # find the next author
        while authorStart > 0 and authorStart < len( text ):
            # extract author
            authorStart += 3   # skip over '<p>'
            authorEnd = text.find( '</p>', authorStart )
            author = text[ authorStart : authorEnd ]

            # extract book titles, assume each author has at least one title
            nextIndex = authorEnd + 1
            titles = []
            # find where the list of titles stop
            titleStop = text.find( '</ul>', nextIndex )
            titleStart = text.find( '<li>', nextIndex )
            titleEnd = text.find( '</li>', titleStart )
            while nextIndex > 0 and nextIndex < titleStop \
                    and nextIndex < len( text ):
                aTitle = text[ titleStart+4 : titleEnd ]
                titles.append( aTitle )
                titleStart = text.find( '<li>', titleEnd + 1 )
                titleEnd = text.find( '</li>', titleStart )
                nextIndex = titleEnd + 1
            
            authorStart= text.find( '<p>', titleStop )   # find the next author

            # We finished extracting one author and her book titles
            author = self._fixName( author )
            oneRecord = _Record( author )
            for name in titles:
                oneRecord.addBook( name.strip() )
            # Add this record to data set
            dataSet.append( oneRecord )

        # Finished reading data source 'text'
        return dataSet

    def _fixName( self, fullName ):
        """Make sure the author name is in the form of 'last, first'"""
        index = fullName.find( ',' )
        lname = fullName[ 0:index ]
        fname = fullName[ index+1:len(fullName) ]
        return lname + ', ' + fname

        
"""=====================================================
   Storage classes
"""
class _Record:
    def __init__( self, author ):
        commaLoc = author.find( ',' )  # locating ',' for first and last name
        if commaLoc > 0:
            self.lastName = author[ 0:commaLoc ].strip()
            self.firstName = author[ commaLoc+1:len(author) ].strip()
        else:
            self.lastName = author.strip()
            self.firstName = 'U'    # unknown

        self.pubs = []

    def __str__( self ):
        s = self.lastName + ', ' + self.firstName + '\n'
        for book in self.pubs:
            s += '|' + book
        s += '|\n'
        return s
        
    def addBook( self, title ):
        self.pubs.append( title )

    def getAuthor( self ):
        return self.lastName + ' ' + self.firstName

    def getAuthorFName( self ):
        return self.firstName

    def getAuthorLName( self ):
        return self.lastName

    def getBooks( self ):
        return self.pubs

class HtmlPage:
    def __init__( self, title = 'html' ):
        """An HTML page here is defined as a three-part entity
        1. head: from <html> to </head><body>
        2. body: from the position after <body> to right before </body>,
                 essentially the content of the page
        3. trailer: anything from </body> to </html>
        """
        self.title = title
        self._head = None
        self._body = None
        self._trailer = None

    def setHead( self, head ):
        """Set the head portion to be 'head'"""
        self._head = head

    def setBody( self, body ):
        """Set the body portion to be 'body'"""
        self._body = body

    def setTrailer( self, trailer ):
        """Set the trailer portion to be 'trailer'"""
        self._trailer = trailer

    def getHead( self ):
        """Get the head"""
        return self._head

    def getBody( self ):
        """Get the body portion"""
        return self._body

    def getTrailer( self ):
        """Get the trailer portion"""
        return self._tailer

    def buildPage( self ):
        """Build a complete HTML page out of 'head', 'body', and 'trailer'"""
        return self._head + '\n' + self._body + '\n' + self._trailer


# test

"""
h = HTMLReader()
print(h)
input('Hit <return> to continue ...')
h = HTMLReader('classicliterature.html')
print(h)
"""
