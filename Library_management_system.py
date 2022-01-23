from books import Book
from members import *
from admin import Admin

class Library:
	#List to store the book instances
	books=[]
	#book_id to provide unique id for the books
	book_id=1
	#List to  store the users instances
	member=[]
	#id to generate unique id
	Member_id=1
	def __init__(self): 
		# Login method will be called when the project is executing
		self.Login() 

	def Login(self): 
		while True:
			print("Choose The Option") 
			print("1 - Login as Admin")
			print("2 - Login as Member") 
			user_type = int(input()) 
			#checks for the type of user
			if user_type==1:
				self.getInfo_for_Login("Administrator") 
			else:
				self.getInfo_for_Login("Member")


	# gets the login information from the user and makes the call to authentication			
	def getInfo_for_Login(self,person):
		print("welcome ",person)
		print("Enter Your User Name")
		user_name=input()
		print("Enter Your Password")
		password=input()
		if person=="Administrator":
			self.Authenticate_admin(user_name,password) 
		else:
			self.Authenticate_member(user_name,password)



	#used to authenticate admin account
	#after successful login admin actions will be displayed
	def Authenticate_admin(self,user_name,password):
		if user_name=="" and password=="":
			print("Login Successful")
			print()
			admin=Admin()
			while True:
				current =admin.actions(self.Member_id,self.member,self.book_id,self.books)
				if current==1:
					self.book_id+=1
				if current==4:
					self.Member_id+=1
				if current==7:
					break
		else:
			print("Login Failed")
			print()
			self.getInfo_for_Login("Administrator")


	#used for authenticating members
	#if login was successful will display the member operations
	def Authenticate_member(self,user_name,password):
		for user in self.member:
			if user.user_name==user_name and user.password==password:
				print("Login Successful")  
				while True:
					operation=MemberOperations().get_info(self.books,self.Member_id)
					if operation==4:
						break
				break
		else:
			print("Try again")
			self.getInfo_for_Login("Member")

Library()

		
		