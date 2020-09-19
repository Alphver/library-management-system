#this is the client side file
import sys
import Pyro4
import Pyro4.util

if sys.version_info < (3, 0):
	input = raw_input

#By selecting 1~7, you choose one of the function
sys.excepthook = Pyro4.util.excepthook
library = Pyro4.Proxy("PYRONAME:assignment2.library")
while(True):
	print("1: Return booklist 		2: Add book")
	print("3: Set on loan 			4: Set not loan")
	print("5: Return book in dec order	6: Search book by ISBN")
	print("7: Search by year")
	item = input("Type the number of function you wish or press q to quit: ").strip()
	
	if(item=="1"):
		infoList = library.return_books()
		for element in infoList:
			print(element)

	elif(item=="2"):
		author = input("Author: ")
		title = input("Title: ")
		ISBN = input("ISBN: ")
		year = input("Year: ")
		library.add_book(author,title,ISBN,year)

	elif(item=="3"):
		bookname = input("Type the name of the book you wish to set on loan: ")
		library.set_on_loan(bookname)

	elif(item=="4"):
		bookname = input("Type the name of the book you wish to set not on loan: ")
		library.set_not_loan(bookname)

	elif(item=="5"):
		infoList = library.return_books_sorted()
		for element in infoList:
			print(element)

	elif(item=="6"):
		searchISBN = input("Type the ISBN of the book you wish to search: ")
		infoList = library.return_books_ISBN(searchISBN)
		for element in infoList:
			print(element)

	elif(item=="7"):
		begin,end = input("Type the year duration(e.g. 2000-3000): ").split("-")
		infoList = library.select_by_year(begin,end)
		for element in infoList:
			print(element)

	elif(item=="q"):
		print("Goodbye")
		break
	else:
		print("Invalid input!")
