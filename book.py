class Book(object):
	def __init__(self, id, author, title, ISBN, year):
		self.id = id
		self.author = author
		self.title = title
		self.ISBN = ISBN
		self.year = year
		self.status = False
		self.times = 0

	#this part return books information as a string.
	def printInfo(self):
		loan = "On loan" if self.status==True else "Not on loan"
		info = "----------------------------------------\n|  Title : %s \n|  ID    : %s \n|  Author: %s \n|  ISBN  : %s \n|  Year  : %s \n|  Status: %s \n|  Times : %s \n"%(self.title, self.id, self.author,  self.ISBN, self.year, loan, self.times)
		return(info)

	def set_on_loan(self):
		self.status = True
		self.times+=1

	def set_not_loan(self):
		self.status = False

