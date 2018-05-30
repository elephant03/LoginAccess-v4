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
# Imports the new account screen displayer
from Libary.Menus import NewAccount
# Imports to validate the users logins
from Libary.Utility import LoginChecks as LC
# Imports hashing libary
from Libary.Utility.Security import Hash as h


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

        # Sets up the database
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            self.Cur.execute("""
            CREATE TABLE IF NOT EXISTS Users (
            Username TEXT NOT NULL PRIMARY KEY,
            Password TEXT NOT NULL,
            AccountType INTEGER NOT NULL,
            Email INTEGER);""")

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
        self.Login_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.Login_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

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

        self.tb.Align_Grid(self.Login_fr)
        self.tb.Align_Grid(self.Main_fr)

        return

    def Login_Help(self):
        '''
        Calls the help screen
        '''
        HelpMenus.Login_Help(self.Main_fr)

        return

    def Login_command(self):
        '''
        Checks the users login details and logs them in if they are correct
        '''

        # Will return true if the users login is correct and false otherwise
        self.Passed = LC.Check(self.Username_ent, self.Password_ent)

        # Clears all of the users inputs
        self.Username_ent.delete(0, "end")
        self.Password_ent.delete(0, "end")

        # Refocuses the mouse onto the Username
        self.Username_ent.focus()

        if self.Passed:
            self.Space_lbl.config(text="")
            MainMenu.LoginMenu(
                str(h.Hash(self.Username_ent.get(), Secure=False)))
            return

        self.Space_lbl.config(text="Sorry, login failed")

        return

    def NewAccount_command(self):
        '''
        Loads the account creation screen
        '''
        NewAccount.NewAccount(self.Main_fr, self.Space_lbl, self.Username_ent)

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
