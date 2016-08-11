from hashlib import *
#import bounceball
def entry(database):
	action = input("Please enter LOGIN or SIGNUP \n")

	if action == "SIGNUP":
		signup(database)
		entry(database)

	if action == "LOGIN":
		login(database)
		exit = ""
		while exit != "EXIT":
			exit = input("\n")


def signup(database):
	username = input("Please choose a username \n")
	password = input("Please choose a password \n")


def login(database):
    username = input("Please enter your username \n")
    password = input("Please enter your password \n")
	if username not in (database):
	# 	print("Username is not found. Please sign up.")

database={}
entry(database)

passwordhash=sha256("password".encode('utf-8')).hexdigest()
# The above will give you a hash of MYSTRING
print(passwordhash)
database[username]=passwordhash
