#This is the server side file, it store all of the book objcet
#it can also change book objects' attributes.
from book import Book
import Pyro4


@Pyro4.expose
class Library(object):
	def __init__(self):
		self.bookList = []
		self.bookID=1

	def return_books(self):
		infoList = []
		for book in self.bookList:
			infoList.append(book.printInfo())
		print("return books information")
		return infoList

	def add_book(self, author, title, ISBN, year):
		book = Book(self.bookID,author,title,ISBN,year)
		self.bookList.append(book)
		self.bookID+=1
		print("add a new book {0} {1} {2} {3}".format(author,title,ISBN,year))


	def set_on_loan(self, title):
		for book in self.bookList:
			if(book.title==title):
				book.set_on_loan()
		print("{0} set to on loan".format(title))

	def set_not_loan(self, title):
		for book in self.bookList:
			if(book.title==title):
				book.set_not_loan()
		print("{0} set to not loan".format(title))

	def return_books_sorted(self):
		#using a simple selection sort
		decList = []
		decList = self.bookList[:]
		for i in range(len(decList)):
			maxIndex = i
			for j in range(i+1,len(decList)):
				if decList[i].year < decList[j].year:
					maxIndex = j
			decList[i], decList[maxIndex] = decList[maxIndex], decList[i]
		infoList = []
		for book in decList:
			infoList.append(book.printInfo())
		print("return dec order book list")
		return infoList

	def return_books_ISBN(self, intValue):
		infoList = []
		for book in self.bookList:
			if(book.ISBN==intValue):
				infoList.append(book.printInfo())
		print("search intValue: {0}".format(intValue))
		return infoList

	def select_by_year(self, begin, end):
		infoList = []
		for book in self.bookList:
			if(int(book.year)>=int(begin) and int(book.year)<=int(end)):
				infoList.append(book.printInfo())				
		print("search by year {0} - {1}".format(begin,end))
		return infoList

def main():
	library = Library()		
	Pyro4.Daemon.serveSimple(
		{
			library: "assignment2.library"
		},
		ns=True)

if __name__ == "__main__":
		main()
	

