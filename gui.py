"""The main file the run the GUI for classical search"""

from tkinter import *
from messagebox import *    # for 'showinfo()'
from read_html import HTMLReader, _Record, HtmlPage
from avltree_student import AVLTree, _AVLTreeNode
import pickle   

'''CSCI 204 Project 4 – Search and Sorting
    Due date: phase1: 12/5/2017
    Lab section: CSCI 204.L60, Tuesday 13-15:50
    Student name: Judy Peng
    Instructor name: Professor Hamid
'''       
        
class App:
    """This program demonstrates the use of GUI in a relatively simple way"""

    def __init__( self, master, title, file = 'test.html', pickleF = "", test = False):

        # set window parameters
        self.master = master

        self.master.title( title )
        self.master.maxsize(800,600)
        self.result = []
        self.test = test
        self.pickleF = pickleF
        self._file = file


        # display the UI
        self._setUpDisplay()
        # take action based on the button clicks
        self._takeAction()
        if self.pickleF != "":
            try: #Try to find a valid pickle file to read
                f = open( pickleF, 'rb' )
                self.authorAVL = pickle.load( f )
                self.bookAVL = pickle.load( f )
            
            except Exception: #If a valid pickle file is not found, use the html file specified
                try:
                    h = HTMLReader(file)
                except Exception:
                    h = HTMLReader("test.html")
                self.authorAVL = AVLTree()
                for x in h._data:
                    key = x.lastName.lower() + " " + x.firstName.lower()
                    value = x
                    self.authorAVL.add(key, value)
                self.bookAVL = AVLTree()
                for x in h._data:
                    author = x.lastName.lower() + " " + x.firstName.lower()
                    for book in x.pubs:
                        key = book.lower()
                        value = x
                        self.bookAVL.add(key, value)
        else:
            #if a user doesn't enter anything for pickle file
            #build trees directly from html file provided (if not vaild, use "test.html")
            try:
                h = HTMLReader(file)
            except Exception:
                h = HTMLReader("test.html")
            self.authorAVL = AVLTree()
            for x in h._data:
                key = x.lastName.lower() + " " + x.firstName.lower()
                value = x
                self.authorAVL.add(key, value)
            self.bookAVL = AVLTree()
            for x in h._data:
                author = x.lastName.lower() + " " + x.firstName.lower()
                for book in x.pubs:
                    key = book.lower()
                    value = x
                    self.bookAVL.add(key, value)
            

                    
    def getResult( self ):
        """This is a mechanism to pass the result from the UI"""
        # return the result(s) of action
        return self.result
    
    def remove(self) :
        """Remove the author and his or her publications from the database."""
        self.outputresult.delete( 1.0, END )
        authorName = self.inputauthor.get()
        if self.test:
            print( "Here's what you entered for author : ", end = '' )
            print( authorName )
        self.result.append( authorName)
        if authorName == "":
            if self.test:
                    print("Please enter the author's name you want to remove.")
                    print("-------------------------")
            self.outputresult.insert( INSERT, "Please enter the author's name you want to remove.")
        else:
            data = self.authorAVL.getValue( authorName.lower() )
            if data is None:
                if self.test:
                    print("The author is not in our database.")
                    print("-------------------------")
                self.outputresult.insert( INSERT, "The author is not in our database.")
            else:
                if self.test:
                    print("The original Author AVL Tree:")
                    self.authorAVL.print()
                    print("The original Book AVL Tree:")
                    self.bookAVL.print()
                self.authorAVL.remove(authorName.lower())
                bookStr = ""
                for books in data.pubs:
                    self.bookAVL.remove(books.lower())
                    bookStr += "'" + books.lower() + ",' "
                self.outputresult.insert( INSERT, "The author " + data.lastName \
                                          + ", " + data.firstName + " and his/her publications are now removed.")
                if self.test:
                    print("The resulting Author AVL Tree:")
                    print("""You shouldn't see '""" + authorName.lower() + """' in the tree.""")
                    self.authorAVL.print()
                    print("The resulting Book AVL Tree:")
                    print("You shouldn't see " + bookStr + " in the tree.")
                    self.bookAVL.print()
                    print("-------------------------")
    def add(self) :
        """Add an author and his or her publications to our database"""
        self.outputresult.delete( 1.0, END )
        authorName = self.inputauthor.get()
        book = self.inputtitle.get()
        if self.test:
            print( "Here's what you entered for author : ", end = '' )
            print( authorName )
            print( "Here's what you entered for publications : ", end = '' )
            print( book )
            
        result = authorName,book
        self.result.append( result )
        if authorName == "" or "," not in authorName:
            if self.test:
                print("Please enter the author's name [Ex. Last, First] you want to add.")
                print("-------------------------")
            self.outputresult.insert( INSERT, "Please enter the author's name [Ex. Last, First] you want to add.")
        elif book == "":
            if self.test:
                print("Please enter the publications of the author you want to add, separate by commas if there are more than one publication. Please make sure that there is no space before and after the comma(s).")
                print("-------------------------")
            self.outputresult.insert( INSERT, "Please enter the publications of the author you want to add, separate by commas if there are more than one publication. Please make sure that there is no space before and after the comma(s).")
        else:
            if self.test:
                print("The original Author AVL Tree:")
                self.authorAVL.print()
                print("The original Book AVL Tree:")
                self.bookAVL.print()
            value = _Record(authorName)
            value.pubs = book.split(",")
            key = value.lastName.lower() + " " + value.firstName.lower()
            self.authorAVL.add(key, value)
            bookStr = ""
            for books in value.pubs:
                self.bookAVL.add(books.lower(), value)
                bookStr += "'" + books.lower() + ",' "
            self.outputresult.insert( INSERT, "The author " + authorName \
                                      + " and his/her publication(s) have been added to our database.")
            if self.test:
                print("The resulting Author AVL Tree:")
                print("""You should see '""" + value.lastName.lower() \
                                          + " " + value.firstName.lower() + """' in the author tree.""")
                self.authorAVL.print()
                print("The resulting Book AVL Tree:")
                print("You should see " + bookStr + " added in the book tree.")
                self.bookAVL.print()
                print("-------------------------")
                



    def _takeAction( self ):
        """Listen to buttons, take appropriate actions as specified"""

        # create a button and associate a method (action) with the button
        self.checkbutton = Button( self.master, text = "Search", command = self.printinput )
        # put the button in the grid
        self.checkbutton.grid( row = 3, column = 0 )

        # create two more buttons that don't do anything yet, as an example
        self.button1 = Button( self.master, text = "Add", command = self.add )
        self.button2 = Button( self.master, text = "Remove", command = self.remove )
        self.button1.grid( row = 3, column = 1 )
        self.button2.grid( row = 3, column = 2 )

    def _setUpDisplay( self ):
        """Set up various buttons and input boxes for the UI"""
        # in this example, we have five rows and four columns in a grid
        # row 0: some prompt/message
        # row 1: 'author', input box, image (across col 2 and 3, row 1 and 2)
        # row 2: 'title', input box
        # row 3: 'ok' button (col 0), 'zoom in' (col 2), 'zoom out' (col 3)
        # row 4: output textbox

        # create labels and set them in the grid
        self.hellolabel = Label( self.master, text = "Please enter what you want to search for in the text field below!" ).grid( row = 0, column = 0, columnspan = 4, padx = 4, pady = 4 )
        self.authorlabel = Label( self.master, text = "Author" ).grid( row = 1, sticky = W )
        self.titlelabel = Label( self.master, text = "Title" ).grid( row = 2, sticky = W)

        # create the input boxes
        self.inputauthor = Entry( self.master )
        self.inputtitle = Entry( self.master )
        
        # put the input boxes in the grid
        self.inputauthor.grid( row = 1, column = 1 )
        self.inputtitle.grid( row = 2, column = 1 )

        # create output field
        self.outputresult = Text( self.master, height = 4, padx = 4, pady = 4 )
        # put the output field in the grid
        self.outputresult.grid( row = 4, column = 0, columnspan = 4, padx = 4, pady = 4 )

        # load an image to display
        photo = PhotoImage( file = "books.gif" )

        # associate the image with a label
        self.label3 = Label( self.master, image = photo, height = 50, width = 80 )
        self.label3.phto = photo
        # position the image (as a lable) in the grid
        self.label3.grid( row = 1, column = 2, columnspan = 2, rowspan = 2,\
                    sticky = W+E+N+S, padx = 5, pady = 5 )
        

    def printinput( self ):
        """A more useful callback method"""

        author=self.inputauthor.get()
        book=self.inputtitle.get()
        if author != "" and book != "":
            self.outputresult.delete( 1.0, END )
            if self.test:
                print("Please enter one at a time.")
                print("-------------------------")
            self.outputresult.insert( INSERT, "Please enter one at a time.")
        elif author != "":
            # print user input to console, e.g., Linux command window
            if self.test:
                print( "Here's what you entered for author : ", end = '' )
                print( author )

            # store the result so we can set the value in the object
            self.result.append( author )

            # clean input field
            self.inputauthor.delete( 0, END )
            
            # also print user input to output window
            self.printoutputAuthor( author )
            
        elif book != "":
            if self.test:
                print( "Here's what you entered for book : ", end = '' )
                print( book )

            # store the result so we can set the value in the object
            self.result.append( book )

            # clean input field
            self.inputtitle.delete( 0, END )
            
            # also print user input to output window
            self.printoutputBook( book )
            

    def printoutputAuthor(self,s):
        """another sample callback method"""

        # delete previous content of output box, 
        # starting from line 1 column 0 till the end
        self.outputresult.delete( 1.0, END )
        
        # insert new text at starting position
        out = self.authorAVL.getValue( s.lower() )         
        if out is not None:
            if self.test:
                print("Displaying the search result for author: " \
                                      + s + "\n"  + str(out))
                print("-------------------------")
            self.outputresult.insert( INSERT, "Displaying the search result for author: " \
                                      + s + "\n"  + str(out))
            
        else:
            if self.test:
                print("The author " + s + " is not in our data base.")
                print("-------------------------")
            self.outputresult.insert( INSERT, "The author " + s \
                                      + " is not in our data base.")
            

        
    def printoutputBook(self,s):
        """another sample callback method"""

        # delete previous content of output box, 
        # starting from line 1 column 0 till the end
        self.outputresult.delete( 1.0, END )
        
        # insert new text at starting position
        out = self.bookAVL.getValue( s.lower() )         
        if out is not None:
            if self.test:
                print("Displaying the search result for book: " + s + "\n"  + str(out))
                print("-------------------------")
            self.outputresult.insert( INSERT, "Displaying the search result for book: " \
                                      + s + "\n"  + str(out))
            
        else:
            if self.test:
                print("The book " + s + " is not in our data base.")
                print("-------------------------")
            self.outputresult.insert( INSERT, "The book " + s \
                                      + " is not in our data base.")


    def writeHtml(self):
        """Write the added or removed data in html file"""
        text = HtmlPage("List of classic novels") #use class HtmlPage
        text.setHead("<html>\n<head>\n<title>" + \
                     text.title +"</title>\n</head>\n<body>")
        text.setTrailer("</body>\n</html>")
        bodyStr = ""
        for key in self.authorAVL:
            data = self.authorAVL.getValue(key)
            bodyStr += "<p>" + data.lastName + ", " + data.firstName + "</p>\n<ul>"
            for book in data.pubs:
                bodyStr += "  <li>" + book + "</li>\n"
            bodyStr += "</ul>\n"
        text.setBody(bodyStr)
        f = open(self._file , "w")# overwrite the old file with the renewed file 
        f.write(text.buildPage())
        f.close()
        
    def dumpPickle(self, pickleF = None):
        """Write the added or removed data in pickle file"""
        if pickleF is None:
            pickleF = self.pickleF
        f = open(pickleF, 'wb')
        pickle.dump(self.authorAVL, f)
        pickle.dump(self.bookAVL, f)
        f.close()
        
        
        

####################################################
#main code, testing the GUI

if __name__ == "__main__":

    # create "root" widget a.k.a. main window
    root = Tk()

    # create the app
    app = App( root, "Library Menu", "classicliterature.html", "classical.pickle")

    # enter main program loop - display window until it's closed
    root.mainloop()

    # write the renewed data to html file
    app.writeHtml()

    # dump the renewed data to pickle file
    app.dumpPickle()
    # if in the test mode, print result
    if app.test:
        print( " results of the set of operations = ", app.getResult() )

    ##-------------------------------------------##

