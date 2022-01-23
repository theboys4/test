from books import Book
from members import Member

class Admin:
	#to display the admin actions needed to perform
	def actions(self,Member_id,member,book_id,books):
		self.Member_id=Member_id
		self.member=member
		self.book_id=book_id
		self.books=books
		print()
		print("Choose The Action need to perform")
		print("1 - Add new book")
		print("2 - remove an existing book")
		print("3 - view list of books")
		print("4 - add a new user") 
		print("5 - remove an existing user") 
		print("6 - view list of users")
		print("7 - back to login page")
		action_number=int(input())  
		if action_number==1: 
			self.books.append(Book(self.book_id)) 
			
		if action_number==2:
			self.remove_book()
		if action_number==3:
			self.listview_ofbooks()
		if action_number==4:
			self.member.append(Member(self.Member_id))
			
		if action_number==5:
			self.remove_user()
		if action_number==6:
			self.listview_ofuser()
		if action_number==7:
			return action_number
		return action_number
		
	#used to display the list of books
	def listview_ofbooks(self): 
		# to check whether books are available
		if len(self.books)==0:
			print("No books Available")
		# print all books
		for i in self.books:
			print("book id",i.book_id)
			print("book name",i.Title)
			print("description",i.description)
			print("Author Details",i.Author_details)
			print("publication_date",i.publication_date)
			print("edition",i.edition)
			print("price",i.price)
			print("count",i.count)
			print()
			print()


	#	used to remove the books 	
	def remove_book(self): 
		# checks for the presence of books
		if len(self.books)==0:
			print("No books Available")
			return
		print("Enter the book Title needed to be deleted")
		Title=input() 
		# removes that current book from books list
		for book in self.books:
			if book.Title==Title:
				self.books.remove(book) 
				print("removed Successful")
				return 
		else:
			print("That book is no longer Available")


	# used to remove users from member list
	def remove_user(self):
		if len(self.member)==0:
			print("No Users Available")
			return
		print("Enter the User id needed to be deleted")
		user_id=int(input())
		for user in self.member:
			if user.Member_id==user_id:
				self.member.remove(user) 
				print("user removed Successful")
				return 
		else:
			print("That user account is no longer Available")


	# To display the list of users
	def listview_ofuser(self):
		if len(self.member)==0:
			print("No User account Available")
		for i in self.member:
			print("User id",i.Member_id)
			print("user name",i.user_name)
			print("age",i.age)
			print("gender",i.gender)
			print("joining date",i.date)
			print()
			print()





		
		
