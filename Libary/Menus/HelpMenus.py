'''
This file will display the different help screens
These will include tutorials for games
Guides to what this program is and how to use it
Instructs for how to use the tools
'''

# Imports the GUI handelers
import tkinter as TK
from Libary.Utility import tkinter_basics

# Allows for passwords to be reset
from Libary.Menus import PasswordReset


class Login_Help:
    '''
    Displays the help screen for the main login screen
    This also isncluds running the reset password screen
    '''

    def __init__(self, Main_fr):
        '''
        Brings up the help screen for Logins
        '''

        self.tb = tkinter_basics.Basics()

        self.Main_fr = Main_fr

        self.LoginHelp_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.LoginHelp_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.LoginHelp_fr, "Login Help", Row=0, Column=0, CSpan=2)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.LoginHelp_fr, Row=2, Column=0, CSpan=2)

        self.Instructions = [
            "Welcome to the Login Access program",
            "To create an account please press \"back\" then \"new account\"",
            "If you need to reset your password please press the button below",
            "If you already have an account enter your information then press \"login\"",
            "If you need further assitance please look at the wiki or contact admin"
        ]

        for Line in self.Instructions:
            self.Line = self.tb.AddLabel(
                self.LoginHelp_fr, Line, Row=self.Instructions.index(Line)+3, Column=0, CSpan=2)

        self.Back_btn = self.tb.AddButton(
            self.LoginHelp_fr, "Back", Row=len(self.Instructions)+3, Column=0)
        self.Back_btn.config(command=lambda: self.LoginHelp_fr.destroy())

        self.Reset_btn = self.tb.AddButton(
            self.LoginHelp_fr, "Reset Password", Row=len(self.Instructions)+3, Column=1)
        self.Reset_btn.config(command=lambda: [
                              self.LoginHelp_fr.destroy(), PasswordReset.Reset(self.Main_fr)])

        self.tb.Align_Grid(self.LoginHelp_fr)

        return


class MainMenu_Help:
    '''
    Displays a help screen for the menu that you see when you login
    '''

    def __init__(self, Main_fr):
        '''
        Brings up the help screen for using the menu system
        '''

        self.tb = tkinter_basics.Basics()

        self.Main_fr = Main_fr

        self.MainMenuHelp_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.MainMenuHelp_fr.grid(
            row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.MainMenuHelp_fr, "Menu Help", Row=0, Column=0, CSpan=2)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.MainMenuHelp_fr, Row=2, Column=0, CSpan=2)

        self.Instructions = [
            "This is the main menu",
            "It allows you to access the functionality of the program",
            "To use it please click on one of the available sub-menus",
            "If you need more help please read the wiki",
            "Or contact an admin"
        ]

        for Line in self.Instructions:
            self.Line = self.tb.AddLabel(
                self.MainMenuHelp_fr, Line, Row=self.Instructions.index(Line)+3, Column=0)

        self.Back_btn = self.tb.AddButton(
            self.MainMenuHelp_fr, "Back", Row=len(self.Instructions)+3, Column=0)
        self.Back_btn.config(command=lambda: self.MainMenuHelp_fr.destroy())

        self.tb.Align_Grid(self.MainMenuHelp_fr)

        return
