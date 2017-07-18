#this is the function where you need to store the information of the book details
class adding_Books(object):
     def __init__(self,title,author,isbn=None):
         self.title = title #input('Enter the title of the book: ')
         self.author = author#input('Enter the name of the author: ')
         if isbn is None:
            isbn = [] #input('Enter the ID of book: ')


#
print(
"""
	 	Welcome to Miller Nicholas Library System.
	  	a To add a new book
	  	b To add a new member
	 	c To return a book
	 	d To remove a book from the collection
	  	e To remove a member from the system
	 """)

user_option = input('Enter your choice now:')
user_option = user_option.lower()
if user_option == 'a':
	adding_Books()
else:
        print("You Entered Invalid Choice")