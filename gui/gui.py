
from tkinter import *
from messagebox import *    # for 'showinfo()'

class App:
    """This program demonstrates the use of GUI in a relatively simple way"""

    def __init__( self, master, title ):

        # set window parameters
        self.master = master

        self.master.title( title )
        self.master.maxsize(800,600)
        self.result = []      # this Python list stores the result of callback


        # display the UI
        self._setUpDisplay()
        # take action based on the button clicks
        self._takeAction()


    def getResult( self ):
        """This is a mechanism to pass the result from the UI"""
        # return the result(s) of action
        return self.result


    def _takeAction( self ):
        """Listen to buttons, take appropriate actions as specified"""

        # create a button and associate a method (action) with the button
        self.checkbutton = Button( self.master, text = "OK", command = self.printinput )
        # put the button in the grid
        self.checkbutton.grid( columnspan = 2, sticky = W )

        # create two more buttons that don't do anything yet, as an example
        self.button1 = Button( self.master, text = "Zoom in", command = self.callback )
        self.button2 = Button( self.master, text = "Zoom out", command = self.callback )
        self.button1.grid( row = 3, column = 2 )
        self.button2.grid( row = 3, column = 3 )

    def _setUpDisplay( self ):
        """Set up various buttons and input boxes for the UI"""
        # in this example, we have five rows and four columns in a grid
        # row 0: some prompt/message
        # row 1: 'author', input box, image (across col 2 and 3, row 1 and 2)
        # row 2: 'title', input box
        # row 3: 'ok' button (col 0), 'zoom in' (col 2), 'zoom out' (col 3)
        # row 4: output textbox

        # create labels and set them in the grid
        self.hellolabel = Label( self.master, text = "Please enter something in the text field below!" ).grid( row = 0, column = 0, columnspan = 4, padx = 4, pady = 4 )
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
        

    def callback( self ):
        """A sample callback method when a button is clicked"""
        print( "Click!" )

    def printinput( self ):
        """A more useful callback method"""

        st=self.inputauthor.get()

        # print user input to console, e.g., Linux command window
        print ( "Here's what you entered for author : ", end = '' )
        print( st )

        # store the result so we can set the value in the object
        self.result.append( st )

        # clean input field
        self.inputauthor.delete( 0, END )
        
        # also print user input to output window
        self.printoutput( st )

    def printoutput(self,s):
        """another sample callback method"""

        # delete previous content of output box, 
        # starting from line 1 column 0 till the end
        self.outputresult.delete( 1.0, END )
        
        # insert new text at starting position
        self.outputresult.insert( INSERT, "Here's what you entered: " + s )

        # display a messagebox, just for fun
        # The 'showinfo()' method comes from the 'message' package
        showinfo( "Messagebox","Have a nice day" )

####################################################
#main code, testing the GUIs


# create "root" widget a.k.a. main window
root = Tk()

# create the app
app = App( root, "Library Menu" )

# enter main program loop - display window until it's closed
root.mainloop()

# extract the result from first GUI
print( " results of first set of operations = ", app.getResult() )

##-------------------------------------------##
## Use the GUI second time ##

# create "root" widget a.k.a. main window
root = Tk()

# create the app
app = App( root, "Author Title Menu" )

# enter main program loop - display window until it's closed
root.mainloop()

# extract the result from previous GUI
print( " results of second set of operations = ", app.getResult() )

