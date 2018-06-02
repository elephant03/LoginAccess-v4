'''
Shows all of the different customisation options that the user can access
This includes changing the display colours, account details
From here the user can also apply to change their account type, errase data
or other account tasks
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics


class Options:
    '''
    Sotres the methods for the options system and the key varbales
    '''

    def __init__(self, Main_fr, Username):
        '''
        Sets up the menu's GUI and base varables
        '''
        # Creats a main_fr object
        self.Main_fr = Main_fr

        # Stores the username for the GUI colours and tracking
        self.Username = Username

        # Heps handle building the GUI
        self.tb = tkinter_basics.Basics()
