'''
Will load the GUI for creating a new user account and if the users
inputs are correct will add the user to the database
The first user to create an account will automatically be set to "owner" type
'''

# Imports the GUI handelers
import tkinter as TK
from Libary.Utility import tkinter_basics
# Import the databse handler
import sqlite3 as lite
# Imports the hashing libary
from Libary.Utility.Security import Hash as h
# Imports the email validation
from Libary.Utility import ValidateEmail as VE


class NewAccount:
    '''
    the main new account object
    '''

    def __init__(self, Main_fr, LoginSpacer, Login_ent):
        '''
        Loads the GUI processes for the new account screen
        '''

        self.Main_fr = Main_fr
        self.LoginSpacer = LoginSpacer
        self.Login_ent = Login_ent

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

        # Binds the enter key to create the account
        self.Username_ent.bind("<Return>", lambda e: self.Create())
        self.Password_ent.bind("<Return>", lambda e: self.Create())
        self.CheckPassword_ent.bind("<Return>", lambda e: self.Create())

    def Create(self):
        self.Space_lbl.config(text="")

        self.Username_ent_bu = self.Username_ent.get()

        if not self.Password_ent.get() or not self.Username_ent.get():
            # Clears all of the users inputs
            self.Username_ent.delete(0, "end")
            self.Password_ent.delete(0, "end")
            self.CheckPassword_ent.delete(0, "end")

            # Refocuses the mouse onto the Username
            self.Username_ent.focus()

            self.Space_lbl.config(
                text="Sorry one or more of your values was empty")
            return

        if self.Password_ent.get() != self.CheckPassword_ent.get():
            # Clears all of the users inputs
            self.Username_ent.delete(0, "end")
            self.Password_ent.delete(0, "end")
            self.CheckPassword_ent.delete(0, "end")

            # Refocuses the mouse onto the Username
            self.Username_ent.focus()

            self.Space_lbl.config(text="Sorry the passwords didn't match")
            return

        # Tests weather the username is already in user
        with lite.connect("MyDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()

            self.Cur.execute("SELECT EXISTS (SELECT * FROM Users WHERE Username = ?)",
                             (str(h.Hash(self.Username_ent.get(), Secure=False)),))

            if self.Cur.fetchall()[0][0] == 1:
                # Clears all of the users inputs
                self.Username_ent.delete(0, "end")
                self.Password_ent.delete(0, "end")
                self.CheckPassword_ent.delete(0, "end")

                # Refocuses the mouse onto the Username
                self.Username_ent.focus()

                self.Space_lbl.config(
                    text="Sorry, that username is already taken")
                return

            # If they pass then the new account will be created
            self.Cur.execute("INSERT INTO Users (Username, Password, AccountType) VALUES(?, ?, ?)", (str(h.Hash(
                self.Username_ent.get(), Secure=False)), str(h.Hash(self.Password_ent.get())), str(h.Hash("standered", Secure=False))))

            self.Cur.execute("SELECT * FROM Users")

            if len(self.Cur.fetchall()) == 1:
                self.Cur.execute("UPDATE Users SET AccountType = ? WHERE Username = ?", (
                    str(h.Hash("owner", Secure=False)),
                    str(h.Hash(self.Username_ent.get(), Secure=False))))

        self.NewAccount_fr.destroy()
        self.LoginSpacer.config(text="Account created")

        # Calls the optional e-mail adder page
        self.Add_email_GUI()
        return

    def Add_email_GUI(self):
        '''
        An optional extra to add an email account  to the users account
        This will allow them to reset their password if they forget it
        '''
        self.AddEmail_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.AddEmail_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Explaination_lbl = self.tb.AddLabel(
            self.AddEmail_fr, "(Optional)- Do you wish to link your email to this account?", Row=0, Column=0, CSpan=2)
        self.Explaination_lbl1 = self.tb.AddLabel(
            self.AddEmail_fr, "(this can always be changed in the settings)", Row=1, Column=0, CSpan=2)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.AddEmail_fr, Row=1, Column=0, CSpan=2)

        # Adds a email label to show where to enter your email if you choose to add it
        self.Email_lbl = self.tb.AddLabel(
            self.AddEmail_fr, "Email:", Row=2, Column=0)

        # Adds a entry so the user can type in there email
        self.Email_ent = self.tb.AddEntry(
            self.AddEmail_fr, Focus=True, Row=2, Column=1)

        self.Space_lbl_1 = self.tb.AddLabel_spacer(
            self.AddEmail_fr, Row=3, Column=0, CSpan=2)

        self.Back_btn = self.tb.AddButton(
            self.AddEmail_fr, "Skip", Row=4, Column=0)
        self.Back_btn.config(
            command=lambda: [self.AddEmail_fr.destroy(), self.Login_ent.focus()])

        self.Create_btn = self.tb.AddButton(
            self.AddEmail_fr, "Add Email", Row=4, Column=1)
        self.Create_btn.config(command=lambda: self.AddEmail())

        self.tb.Align_Grid(self.Main_fr)
        self.tb.Align_Grid(self.AddEmail_fr)

        # Binds the enter key to create the account
        self.Email_ent.bind("<Return>", lambda e: self.AddEmail())
        self.AddEmail_fr.bind("<Return>", lambda e: self.AddEmail())

        return

    def AddEmail(self):
        '''
        If the user supplies and email it will be hashed and then saved onto the database
        '''
        if not self.Email_ent.get():
            self.Space_lbl.config(text="Please enter an email or skip")
            return

        if not VE.ValidateEmail(self.Email_ent.get()):
            self.Space_lbl.config(text="This email is invalid")
            return

        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()

            self.Cur.execute("UPDATE Users SET Email = ? WHERE Username = ?",
                             (str(h.Hash(self.Email_ent.get(), Secure=False)),
                              str(h.Hash(self.Username_ent_bu, Secure=False))))

        self.AddEmail_fr.destroy()
        self.Login_ent.focus()

        return
