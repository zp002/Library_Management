"""The test file for the AVL Tree and GUI"""
print("Testing AVL Tree...")
from testavl import *
from gui import *
'''CSCI 204 Project 4 – Search and Sorting
    Due date: phase1: 12/5/2017
    Lab section: CSCI 204.L60, Tuesday 13-15:50
    Student name: Judy Peng
    Instructor name: Professor Hamid
'''  

# create "root" widget a.k.a. main window
root = Tk()

htmlFile = input("Please enter the html source file. ") #enter test.html
    
pickleFile = input("Please enter the pickle source file. Hit enter to skip. ")# enter test.pickle

print("-------------------------")
# create the app
app = App( root, "Library Menu",htmlFile, pickleFile, True)

# enter main program loop - display window until it's closed
root.mainloop()

# write the renewed data to html file
writeHtml = input("""Enter 'y' to renew the data in html file. """)
if writeHtml == "y":
    app.writeHtml()

# dump the renewed data to pickle file
if app.pickleF != "":
    writePickle = input("""Enter 'y' to renew the data in pickle file. """)
    if writePickle == "y":
        app.dumpPickle()
else:
    writePickle = input("""Enter the pickle file you want to store your data. """)
    try:
        app.dumpPickle(writePickle)
    except Exception:
        print("Cannot dump your data. Invalid file name.")
if app.test:
    print( " results of the set of operations = ", app.getResult() )

##-------------------------------------------##

