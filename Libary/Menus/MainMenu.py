'''
This file handels the menu menu that you see on logining in
It gives you access to all of the submenu's that you can access
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics
# For database handeling
import sqlite3 as lite
# Imports encyription system
from Libary.Utility.Security import Hash as h


class LoginMenu:
    '''
    Loads the main menu options screen
    This will display the base methods that you can do
    '''

    standered_hash = str(
        b'^E\xae\x03\xe4F]v-h\xa2\x85\xc9\xef\x7f\xfd\xa2\xd2V\x07\xac\xf1\x00\xce\xf3\xb3\xf1%C\t\x0e\x18')
    admin_hash = str(
        b'\x8civ\xe5\xb5A\x04\x15\xbd\xe9\x08\xbdM\xee\x15\xdf\xb1g\xa9\xc8s\xfcK\xb8\xa8\x1fo*\xb4H\xa9\x18')
    owner_hash = str(
        b'L\x10)i~\xe3Xq]:\x14\xa2\xad\xd8\x17\xc4\xb0\x16QD\r\xe8\x087\x1fx\x16Z\xc9\r\xc5\x81')
    teacher_hash = str(
        b'\x10W\xa9`N\x04\xb2t\xdaZM\xe0\xc8\xf4\xb4\x86\x8d\x9b#\t\x89\xf8\xc8\xc6\xa2\x82!\x14<\xc5\xa7U')
    student_hash = str(
        b'&L\x8c8\x1b\xf1l\x98*NY\xb0\xddLox\x08\xc5\x1a\x05\xf6L5\xdbB\xccx\xa2\xa7(u\xbb')

    def __init__(self, Main_fr, Username):
        '''
        Stores key verables and loads the menu GUI
        '''
        # Stores the main_fr
        self.Main_fr = Main_fr
        # Stores the username
        self.Username = Username

        # Gets the account type
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
            self.Cur.execute(
                "SELECT AccountType FROM Users WHERE Username = ?", (self.Username,))

            self.AccountType = self.Cur.fetchall()[0][0]

            self.Cur.execute("""CREATE TABLE IF NOT EXISTS Warnings (
                Username TEXT NOT NULL,
                Issued_by TEXT NOT NULL,
                Issued_for TEXT NOT NULL,
                Issued_on TEXT NOT NULL,
                FOREIGN KEY (Username) REFERENCES Users (Username) ON UPDATE CASCADE ON DELETE CASCADE
                );""")

            self.Cur.execute(
                "SELECT * FROM Warnings WHERE Username = ?", (self.Username,))

            try:
                self.Warnings_list = self.Cur.fetchall()
                self.Warnings_num = len(self.Warnings_list)
            except IndexError:
                self.Warnings_list = []
                self.Warnings_num = 0

        self.tb = tkinter_basics.Basics(Username=self.Username)

        if self.Warnings_num >= 3:
            print("Account deactivated")
            return

        self.Menu_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.Menu_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.Menu_fr, "Main Menu:", Row=0, Column=0)

        self.Options_btn = self.tb.AddButton(
            self.Menu_fr, "⚙", Row=0, Column=1)
        self.Options_btn.config(command=lambda: self.Options())

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.Menu_fr, Row=1, Column=0, CSpan=2)

        if self.Warnings_num != 0:
            self.Space_lbl.config(
                text="You have {} warings!".format(self.Warnings_num))

        self.Tools_btn = self.tb.AddButton(
            self.Menu_fr, "Tools", Row=2, Column=0, CSpan=2)
        self.Tools_btn.config(command=lambda: self.Tools_menu())

        # Increase this so that the buttons will easily align to the rest when other options are added
        self.Button_row = 3

        # if your account type allow it it will display the games menu
        if self.AccountType != self.student_hash:
            self.Button_row += 1

            self.Games_btn = self.tb.AddButton(
                self.Menu_fr, "Games", Row=self.Button_row-1, Column=0, CSpan=2)
            self.Games_btn.config(command=lambda: self.Games_menu())

        # Tests if the account is admin or owner
        if self.AccountType == self.admin_hash or self.AccountType == self.owner_hash:
            self.Button_row += 1

            self.Admin_btn = self.tb.AddButton(
                self.Menu_fr, "Admin", Row=self.Button_row-1, Column=0, CSpan=2)
            self.Admin_btn.config(command=lambda: self.Admin_menu())

        # Tests if the account is owner
        if self.AccountType == self.owner_hash:
            self.Button_row += 1

            self.Owner_btn = self.tb.AddButton(
                self.Menu_fr, "Owner", Row=self.Button_row-1, Column=0, CSpan=2)
            self.Owner_btn.config(command=lambda: self.Owner_menu())

        if self.AccountType == self.student_hash or self.AccountType == self.owner_hash:
            self.Button_row += 1

            self.Education_btn = self.tb.AddButton(
                self.Menu_fr, "Education", Row=self.Button_row-1, Column=0, CSpan=2)
            self.Education_btn.config(command=lambda: self.Education_menu())

        if self.AccountType == self.teacher_hash or self.AccountType == self.owner_hash:
            self.Button_row += 1

            self.Teacher_btn = self.tb.AddButton(
                self.Menu_fr, "Teacher Options", Row=self.Button_row-1, Column=0, CSpan=2)
            self.Teacher_btn.config(command=lambda: self.Teacher_menu())

        self.Back_btn = self.tb.AddButton(
            self.Menu_fr, "Logout", Row=self.Button_row, Column=0)
        self.Back_btn.config(command=lambda: self.Menu_fr.destroy())

        self.Reset_btn = self.tb.AddButton(
            self.Menu_fr, "Help", Row=self.Button_row, Column=1)
        self.Reset_btn.config(command=lambda: self.Help())

        self.tb.Align_Grid(self.Menu_fr)
        self.tb.Align_Grid(self.Main_fr)

    def Help(self):

        # Imports the help screen
        from Libary.Menus.HelpMenus import MainMenu_Help as Menu_help
        Menu_help(self.Main_fr)
        return

    def Options(self):
        self.tb.WorkInProgress()
        return

    def Tools_menu(self):
        from Libary.Menus.SubMenus import Tools
        Tools.Tools(self.Main_fr, self.Username)
        return

    def Games_menu(self):
        from Libary.Menus.SubMenus import Games
        Games.Games(self.Main_fr, self.Username)
        return

    def Admin_menu(self):
        self.tb.WorkInProgress()
        return

    def Owner_menu(self):
        self.tb.WorkInProgress()
        return

    def Education_menu(self):
        self.tb.WorkInProgress()
        return

    def Teacher_menu(self):
        self.tb.WorkInProgress()
        return
