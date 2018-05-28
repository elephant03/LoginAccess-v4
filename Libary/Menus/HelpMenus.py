'''
This file will display the different help screens
These will include tutorials for games
Guides to what this program is and how to use it
Instructs for how to use the tools
'''

# Imports the GUI handelers
import tkinter as TK
from Libary.Utility import tkinter_basics


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
