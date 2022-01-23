class Book: 
	#Book class was used to create new instances of new books 
	def __init__(self,book_id):
		self.book_id=book_id
		print("Enter the book name")
		self.Title=input()
		print("Enter the book description")
		self.description=input()
		print("Enter the book Author name")
		self.Author_details=input()
		print("Enter the book date of publicatoion")
		self.publication_date=input()
		print("Enter the book edition")
		self.edition=int(input())
		print("Enter the book price")
		self.price=float(input())
		print("Enter the book count")
		self.count=int(input())  
		print("book created successfully")

	