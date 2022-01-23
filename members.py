import datetime 
# Member class is used to create the instance of members
class Member:
	def __init__(self,Member_id):
		self.Member_id=Member_id
		print("enter user name")
		self.user_name=input()
		print("enter password")
		self.password=input()
		print("enter the age")
		self.age=input()
		print("enter the gender")
		self.gender=input()
		self.date=datetime.datetime.now()
		print("member created successfully")

class MemberOperations:
	#this  class contains the operations the member can perform
	#dictionary to store issued bookid for memberid
	issue_map={} 


	#used to provide the user actions
	def get_info(self,books,Member_id):
		self.books=books
		print("1 - search a book")
		print("2 - issue a book")
		print("3 - return a book")
		print("4 - exit")
		operation=int(input())
		if operation==1:
			self.search_book()
		if operation==2:
			self.issue_book(Member_id)
		if operation==3:
			self.return_book(Member_id)
		if operation==4:
			return operation

	#searches the book whether precent or not		
	def search_book(self):
		#case of no presence of books
		if len(self.books)==0:
			print("No books Available")
			return
		print("enter the book name to search") 
		flag=True
		search_name=input()
		# iterate with every book to search 
		for i in self.books:
			if i.Title==search_name:
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
				flag=False
		if flag:
			print("no match available") 

	#used to issue the book to the user		
	def issue_book(self,Member_id):
		print("enter the book id to issue")
		issue_id =int(input()) 
		for i,j in enumerate(self.books):
			if j.book_id==issue_id and self.valid_user(Member_id) and j.count>0:
				
				# reduces the count of the book when issued
				self.books[i].count-=1 

				# updates the hashmap with the given bookid and current date
				if Member_id in self.issue_map:
					self.issue_map[Member_id].append([j.book_id,datetime.date.today()])
				else:
					self.issue_map[Member_id]=[[j.book_id,datetime.date.today()]] 
				print('The book issued successfully')
				break
		else: 
			print("Book is not available")


	# to return back the book 
	def return_book(self,Member_id): 
		# Displays the list of books the user currently has
		self.print_books(Member_id)
		if Member_id not in self.issue_map:
			return  

		print("enter the book id to return")
		r_book=int(input()) 
		#removes book from dictionary
		for i in self.issue_map[Member_id]:
			if i[0]==r_book:

				self.issue_map[Member_id].remove(i)
				break
		

	# Displays the list of books the user currently has
	def print_books(self,Member_id): 
		print("the book you have")
		if Member_id not in self.issue_map:
			print("NO books available")
		
		if Member_id in self.issue_map and len(self.issue_map[Member_id]):
			for i in self.issue_map[Member_id]: 
				for j in self.books:
					if i[0]==j.book_id:
						print("book id",j.book_id)
						print("book name",j.Title) 
				print()


	# To check whether the user is allowed to issue the book
	def valid_user(self,Member_id): 
		if Member_id in self.issue_map:

			# checks if the user has already issued 5 books 
			if len(self.issue_map[Member_id])>=5:
				print("you have reached the limit of five books")
				return False  

			# checks the user whether not returned the issued book for a month
			for i in self.issue_map[Member_id]: 
				#gives the current day
				k=datetime.date.today() 

				#compares the date of issue and current day and if it is more than a month not eligible
				if (k-i[1]).days>=30: 

					print("currently not issued book longer than a month")
					return False
		return True







		
		