'''
The main program that will call the other features of the LoginAccess system
This will bring up the main screen allowing the user to login or access other base feature
This includes the ability to reset your password
Create a new account
Or quit
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics
# imports for the Login System encryption
from Libary.Utility.Security import Hash
# Imports the databse handeler
import sqlite3 as lite
# Imports the Login screen to display on a successfull login
from Libary.Menus import MainMenu
# Imports the help screen to expalain what to do
from Libary.Menus import HelpMenus
# Imports the resent password screen displayer
from Libary.Menus import PasswordReset
# Imports the new account screen displayer
from Libary.Menus import NewAccount
