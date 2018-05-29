'''
Will load the GUI for creating a new user account and if the users
inputs are correct will add the user to the database
The first user to create an account will automatically be set to "owner" type
'''

# Imports the GUI handelers
import tkinter as TK
from Libary.Utility import tkinter_basics


class NewAccount:
    '''
    the main new account object
    '''

    def __init__(self, Main_fr):
        '''
        Loads the GUI processes for the new account screen
        '''

        self.Main_fr = Main_fr

        self.tb = tkinter_basics.Basics()

        self.NewAccount_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.NewAccount_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.NewAccount_fr, "New Account:", Row=0, Column=0, CSpan=2)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.NewAccount_fr, Row=1, Column=0, CSpan=2)

        # Adds a username label to show where to enter your username
        self.Username_lbl = self.tb.AddLabel(
            self.NewAccount_fr, "Username:", Row=2, Column=0)

        # Adds a entry so the user can type in there username
        self.Username_ent = self.tb.AddEntry(
            self.NewAccount_fr, Focus=True, Row=2, Column=1)

        # Adds a password label to show where to enter your password
        self.Password_lbl = self.tb.AddLabel(
            self.NewAccount_fr, "Password:", Row=3, Column=0)

        # Adds a entry so the user can type in there username
        self.Password_ent = self.tb.AddEntry(
            self.NewAccount_fr, Show="•", Row=3, Column=1)

        # Adds another password label to show where to enter your password
        self.CheckPassword_lbl = self.tb.AddLabel(
            self.NewAccount_fr, "Password (again):", Row=4, Column=0)

        # Adds another entry so the user can type in there username
        self.CheckPassword_ent = self.tb.AddEntry(
            self.NewAccount_fr, Show="•", Row=4, Column=1)

        self.Space_lbl_1 = self.tb.AddLabel_spacer(
            self.NewAccount_fr, Row=5, Column=0, CSpan=2)

        self.Back_btn = self.tb.AddButton(
            self.NewAccount_fr, "Back", Row=6, Column=0)
        self.Back_btn.config(command=lambda: self.NewAccount_fr.destroy())

        self.Create_btn = self.tb.AddButton(
            self.NewAccount_fr, "Create Account", Row=6, Column=1)
        self.Create_btn.config(command=lambda: self.Create())

        self.tb.Align_Grid(self.Main_fr)
        self.tb.Align_Grid(self.NewAccount_fr)

    def Create(self):
        return
