from hashlib import *

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
