'''CSCI 204 Project 4 – Search and Sorting
    Due date: phase1: 12/5/2017
    Lab section: CSCI 204.L60, Tuesday 13-15:50
    Student name: Judy Peng
    Instructor name: Professor Hamid
''' 
Note:
*******Run testdb.py for testing, run gui.py for the main program********

In test mode, additional message/trees will be printed in the python shell with a series of input during the operation.

For testing purposes, the pickle files could be deleted. The two original html files are in the “original_html” folder in case anything was messed up.

-In search
Please make sure you enter your search parameters one at a time. If you enter something in both text boxes, a message will appear to prompt another entry.

When searching for an author, please make sure you enter the author's name as "lastname firstname" with a space between the two names and with no extra symbols.[For example, “austen jane”, “Austen jane”, “AUSTEN Jane” will work, but “austen, jane” or “jane austen” will not] It is not case sensitive.

When searching for a book, please make sure you enter every letter in the title of the book, including any symbol or space if necessary. It is not case sensitive. If there is a “*” in the book title or author name for no reason, (At least I don’t quite understand why…) please make sure you enter the “*” to get the correct search result.[For example, “Chekhov Anton*” will give you a result, but “Chekhov Anton” will not. If you search for “collections of short stories*” it is only going to give you 

Maupassant, Guy*
|collections of short stories*|

even though Chekhov, Anton* also wrote collections of short stories*. Since “M”>”C”, the entry was overwritten in the bookAVL, but the searching for “Chekhov Anton*” will give you the correct result:

Chekhov, Anton*
|collections of short stories*|

-In Add

Please make sure you enter BOTH the author’s name the form[Last, First] and his/her publications [Pub1,Pub2,Pub3…] in the correct field otherwise the output will prompt for a re-entry.

The author’s name must be in the format[Last, First] with both names capitalized separated by a comma and a space.

The publications must be entered with no extra spaces. However you may include any symbol or space if they are in the title. If you want to enter multiple publications, please separate them by comma with no space. [Pub1,Pub2,Pub3…]

-In Remove

Only the input in the “Author” line will be considered. The input must follow the same format as that of search described above. [For example, “austen jane”, “Austen jane”, “AUSTEN Jane” will work, but “austen, jane” or “jane austen” will not]



Two consecutive sample runs:

python testdb.py


Testing AVL Tree...
original data ...
9, 5, 10, 0, 6, 11, -1, 1, 2,      
          
          
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
               
               
          
     


inorder traversal should be in sorted order ...
the result should be :  [-1, 0, 1, 2, 5, 6, 9, 10, 11]
the result is : -1, 0, 1, 2, 5, 6, 9, 10, 11, 
search for "17", should be False :  False
search for "100", should be False :  False
search for "35", should be False :  False
search for "0", should be True :  True
     
          
          
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
               
               
          
     


removing 10 from the avl tree ...
the result should be  [-1, 0, 1, 2, 5, 6, 9, 11]
-1, 0, 1, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

removing 1 from the avl tree ...
the result should be  [-1, 0, 2, 5, 6, 9, 11]
-1, 0, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

removing -1 from the avl tree ...
the result should be  [0, 2, 5, 6, 9, 11]
0, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

Please enter the html source file. test.html
Please enter the pickle source file. Hit enter to skip. 
-------------------------
Here's what you entered for author : Austen Jane
Displaying the search result for author: Austen Jane
Austen, Jane
|Emma|Mansfield Park|Persuasion|Pride and Prejudice|

-------------------------
Here's what you entered for author : peng judy
The author peng judy is not in our data base.
-------------------------
Here's what you entered for book : Therese RaquiN
Displaying the search result for book: Therese RaquiN
Zola, Emile
|L'Assommoir|Therese Raquin|

-------------------------
Here's what you entered for book : csci204
The book csci204 is not in our data base.
-------------------------
Here's what you entered for author : Qwe, Rty
Here's what you entered for publications : Just,To,Test
The original Author AVL Tree:
     
          
          
       +--zola emile
       |  
  +--bronte charlotte
  |    |  
  |    +--braddon mary elizabeth
  |       
  |       
blackmore richard doddridge
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The original Book AVL Tree:
     
          
               
               
            +--villette
            |    |  
            |    +--therese raquin
            |       
            |       
       +--the human comedy
       |    |  
       |    +--pride and prejudice
       |       
       |       
  +--persuasion
  |    |  
  |    +--mansfield park
  |         |  
  |         +--lorna doone
  |            
  |            
  |       
little women
  |       
  |       
  |    +--lady audley's secret
  |    |    |  
  |    |    +--l'assommoir
  |    |       
  |    |       
  +--jane eyre
       |  
       +--emma
          
          
     

The resulting Author AVL Tree:
You should see 'qwe rty' in the author tree.
     
          
          
       +--zola emile
       |    |  
       |    +--qwe rty
       |       
       |       
  +--bronte charlotte
  |    |  
  |    +--braddon mary elizabeth
  |       
  |       
blackmore richard doddridge
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The resulting Book AVL Tree:
You should see 'just,' 'to,' 'test,'  added in the book tree.
     
          
               
                    
                    
                 +--villette
                 |  
            +--to
            |    |  
            |    +--therese raquin
            |       
            |       
       +--the human comedy
       |    |       
       |    |       
       |    |    +--test
       |    |    |  
       |    +--pride and prejudice
       |       
       |       
  +--persuasion
  |    |  
  |    +--mansfield park
  |         |  
  |         +--lorna doone
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |    |  
  |    |    +--just
  |    |       
  |    |       
  +--jane eyre
       |  
       +--emma
          
          
     

-------------------------
Here's what you entered for author : Blackmore Richard Doddridge
The original Author AVL Tree:
     
          
          
       +--zola emile
       |    |  
       |    +--qwe rty
       |       
       |       
  +--bronte charlotte
  |    |  
  |    +--braddon mary elizabeth
  |       
  |       
blackmore richard doddridge
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The original Book AVL Tree:
     
          
               
                    
                    
                 +--villette
                 |  
            +--to
            |    |  
            |    +--therese raquin
            |       
            |       
       +--the human comedy
       |    |       
       |    |       
       |    |    +--test
       |    |    |  
       |    +--pride and prejudice
       |       
       |       
  +--persuasion
  |    |  
  |    +--mansfield park
  |         |  
  |         +--lorna doone
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |    |  
  |    |    +--just
  |    |       
  |    |       
  +--jane eyre
       |  
       +--emma
          
          
     

The resulting Author AVL Tree:
You shouldn't see 'blackmore richard doddridge' in the tree.
     
          
          
       +--zola emile
       |  
  +--qwe rty
  |    |  
  |    +--bronte charlotte
  |       
  |       
braddon mary elizabeth
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The resulting Book AVL Tree:
You shouldn't see 'lorna doone,'  in the tree.
     
          
               
               
            +--villette
            |  
       +--to
       |    |  
       |    +--therese raquin
       |       
       |       
  +--the human comedy
  |    |       
  |    |            
  |    |            
  |    |         +--test
  |    |         |  
  |    |    +--pride and prejudice
  |    |    |  
  |    +--persuasion
  |         |  
  |         +--mansfield park
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |    |  
  |    |    +--just
  |    |       
  |    |       
  +--jane eyre
       |  
       +--emma
          
          
     

-------------------------
Here's what you entered for author : abc
The author is not in our database.
-------------------------
Enter 'y' to renew the data in html file. y
Enter the pickle file you want to store your data. test.pickle
 results of the set of operations =  ['Austen Jane', 'peng judy', 'Therese RaquiN', 'csci204', ('Qwe, Rty', 'Just,To,Test'), 'Blackmore Richard Doddridge', 'abc']
>>> 
======= RESTART: /Users/judypeng/Documents/2 year/CS 204/p4/testdb.py =======
Testing AVL Tree...
original data ...
9, 5, 10, 0, 6, 11, -1, 1, 2,      
          
          
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
               
               
          
     


inorder traversal should be in sorted order ...
the result should be :  [-1, 0, 1, 2, 5, 6, 9, 10, 11]
the result is : -1, 0, 1, 2, 5, 6, 9, 10, 11, 
search for "17", should be False :  False
search for "100", should be False :  False
search for "35", should be False :  False
search for "0", should be True :  True
     
          
          
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
               
               
          
     


removing 10 from the avl tree ...
the result should be  [-1, 0, 1, 2, 5, 6, 9, 11]
-1, 0, 1, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

removing 1 from the avl tree ...
the result should be  [-1, 0, 2, 5, 6, 9, 11]
-1, 0, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

removing -1 from the avl tree ...
the result should be  [0, 2, 5, 6, 9, 11]
0, 2, 5, 6, 9, 11, 
     
          
          
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
          
          
     

Please enter the html source file. test.html
Please enter the pickle source file. Hit enter to skip. test.pickle
-------------------------
Here's what you entered for author : Qwe Rty
Displaying the search result for author: Qwe Rty
Qwe, Rty
|Just|To|Test|

-------------------------
Here's what you entered for author : Blackmore Richard Doddridge
The author Blackmore Richard Doddridge is not in our data base.
-------------------------
Here's what you entered for book : Lorna Doone
The book Lorna Doone is not in our data base.
-------------------------
Here's what you entered for book : Just
Displaying the search result for book: Just
Qwe, Rty
|Just|To|Test|

-------------------------
Here's what you entered for author : Qwe Rty
The original Author AVL Tree:
     
          
          
       +--zola emile
       |  
  +--qwe rty
  |    |  
  |    +--bronte charlotte
  |       
  |       
braddon mary elizabeth
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The original Book AVL Tree:
     
          
               
               
            +--villette
            |  
       +--to
       |    |  
       |    +--therese raquin
       |       
       |       
  +--the human comedy
  |    |       
  |    |            
  |    |            
  |    |         +--test
  |    |         |  
  |    |    +--pride and prejudice
  |    |    |  
  |    +--persuasion
  |         |  
  |         +--mansfield park
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |    |  
  |    |    +--just
  |    |       
  |    |       
  +--jane eyre
       |  
       +--emma
          
          
     

The resulting Author AVL Tree:
You shouldn't see 'qwe rty' in the tree.
     
     
  +--zola emile
  |    |  
  |    +--bronte charlotte
  |       
  |       
braddon mary elizabeth
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The resulting Book AVL Tree:
You shouldn't see 'just,' 'to,' 'test,'  in the tree.
     
          
          
       +--villette
       |    |  
       |    +--therese raquin
       |       
       |       
  +--the human comedy
  |    |       
  |    |       
  |    |    +--pride and prejudice
  |    |    |  
  |    +--persuasion
  |         |  
  |         +--mansfield park
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |  
  +--jane eyre
       |  
       +--emma
          
          
     

-------------------------
Here's what you entered for author : Qwe Rty
The author Qwe Rty is not in our data base.
-------------------------
Here's what you entered for book : to
The book to is not in our data base.
-------------------------
Here's what you entered for author : Blackmore, Richard Doddridge
Here's what you entered for publications : Lorna Doone
The original Author AVL Tree:
     
     
  +--zola emile
  |    |  
  |    +--bronte charlotte
  |       
  |       
braddon mary elizabeth
  |       
  |       
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The original Book AVL Tree:
     
          
          
       +--villette
       |    |  
       |    +--therese raquin
       |       
       |       
  +--the human comedy
  |    |       
  |    |       
  |    |    +--pride and prejudice
  |    |    |  
  |    +--persuasion
  |         |  
  |         +--mansfield park
  |            
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |  
  +--jane eyre
       |  
       +--emma
          
          
     

The resulting Author AVL Tree:
You should see 'blackmore richard doddridge' in the author tree.
     
     
  +--zola emile
  |    |  
  |    +--bronte charlotte
  |       
  |       
braddon mary elizabeth
  |       
  |            
  |            
  |         +--blackmore richard doddridge
  |         |  
  |    +--balzac honore
  |    |  
  +--austen jane
       |  
       +--alcott louisa may
          
          
     

The resulting Book AVL Tree:
You should see 'lorna doone,'  added in the book tree.
     
          
          
       +--villette
       |    |  
       |    +--therese raquin
       |       
       |       
  +--the human comedy
  |    |       
  |    |       
  |    |    +--pride and prejudice
  |    |    |  
  |    +--persuasion
  |         |  
  |         +--mansfield park
  |              |  
  |              +--lorna doone
  |                 
  |                 
  |            
  |       
little women
  |       
  |            
  |            
  |         +--lady audley's secret
  |         |  
  |    +--l'assommoir
  |    |  
  +--jane eyre
       |  
       +--emma
          
          
     

-------------------------
Please enter one at a time.
-------------------------
Here's what you entered for author : Blackmore, Richard Doddridge
The author Blackmore, Richard Doddridge is not in our data base.
-------------------------
Here's what you entered for author : Blackmore Richard Doddridge
Displaying the search result for author: Blackmore Richard Doddridge
Blackmore, Richard Doddridge
|Lorna Doone|

-------------------------
Here's what you entered for book : Lorna Doone
Displaying the search result for book: Lorna Doone
Blackmore, Richard Doddridge
|Lorna Doone|

-------------------------
Enter 'y' to renew the data in html file. y
Enter 'y' to renew the data in pickle file. test.pickle
 results of the set of operations =  ['Qwe Rty', 'Blackmore Richard Doddridge', 'Lorna Doone', 'Just', 'Qwe Rty', 'Qwe Rty', 'to', ('Blackmore, Richard Doddridge', 'Lorna Doone'), 'Blackmore, Richard Doddridge', 'Blackmore Richard Doddridge', 'Lorna Doone']