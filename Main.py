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


class Main():
    '''
    The main program object which will load the login screen and then
    call the other classes
    '''

    def __init__(self, root):
        '''
        Crates the root and Mina_fr objects
        Then calls the Login screen GUI
        '''

        # Creats an instance of the tkinter_basics class
        self.tb = tkinter_basics.Basics()

        # Sets up the root
        self.root = root
        # Adds a title
        self.root.title("Login Access")
        # Adds an icon
        self.root.wm_iconbitmap("./Libary/Icons/MainIcon.ico")

        # Creats the main frame object for other frames to cramed into
        self.Main_fr = TK.Frame(self.root)
        self.Main_fr.pack(fill=TK.BOTH, expand=True)

        # Calls the Login screens GUI
        self.LoginScreen_GUI()

        return

    def LoginScreen_GUI(self):
        '''
        Loads the screen which allows you to Login or the other base options
        '''

        # Creats the Login_fr on top of the main_fr
        self.Login_fr = self.tb.AddFrame(self.Main_fr, Pack=True)

        # Creates a simple title label
        self.Title_lbl = self.tb.AddLabel_title(
            self.Login_fr, "Please Login...", Row=0, Column=0, CSpan=2)

        # Creats a help button to expalin what this program is and what to do if you forget your password
        self.Help_btn = self.tb.AddButton(
            self.Login_fr, "?", Row=0, Column=2)
        self.Help_btn.config(command=lambda: self.Login_Help())

        # Adds a space for estetics
        self.Space_lbl = self.tb.AddLabel_spacer(
            self.Login_fr, Row=1, Column=0, CSpan=3)

        # Adds a username label to show where to enter your username
        self.Username_lbl = self.tb.AddLabel(
            self.Login_fr, "Username:", Row=2, Column=0)

        # Adds a entry so the user can type in there username
        self.Username_ent = self.tb.AddEntry(
            self.Login_fr, Focus=True, Row=2, Column=1, CSpan=2)

        # Adds a password label to show where to enter your password
        self.Password_lbl = self.tb.AddLabel(
            self.Login_fr, "Password:", Row=3, Column=0)

        # Adds a entry so the user can type in there username
        self.Password_ent = self.tb.AddEntry(
            self.Login_fr, Show="•", Row=3, Column=1, CSpan=2)

        self.Space_lbl_1 = self.tb.AddLabel_spacer(
            self.Login_fr, Row=4, Column=0, CSpan=3)

        # Adds a quit button to close the program
        self.Quit_btn = self.tb.AddButton_negetive(
            self.Login_fr, "Quit", Row=5, Column=0)
        self.Quit_btn.config(command=lambda: self.root.destroy())

        # Adds a login button
        self.Login_btn = self.tb.AddButton_possitive(
            self.Login_fr, "Login", Row=5, Column=2)
        self.Login_btn.config(command=lambda: self.Login_command())

        # Adds a new account button
        self.NewAccount_btn = self.tb.AddButton(
            self.Login_fr, "New Account", Row=5, Column=1)
        self.NewAccount_btn.config(command=lambda: self.NewAccount_command())

        # Binds the enter key to run the login command
        self.Username_ent.bind("<Return>", lambda e: self.Login_command())
        self.Password_ent.bind("<Return>", lambda e: self.Login_command())
        self.Login_fr.bind("<Return>", lambda e: self.Login_command())

        return

    def Login_Help(self):
        self.tb.WorkInProgress()

        return

    def Login_command(self):
        self.tb.WorkInProgress()

        return

    def NewAccount_command(self):
        self.tb.WorkInProgress()

        return


if __name__ == "__main__":
    # Creats a root object
    root = TK.Tk()

    # Passes the root to the main class
    Main(root)

    # This does the function as root.mainloop() but split to allow for events
    while True:
        try:
            root.update()
            root.update_idletasks()
        # This will fail if the root has been closed
        except:
            break

    raise SystemExit
