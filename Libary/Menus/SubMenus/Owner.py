'''
Shows all of the extra options that owner accounts have access to
This includes being about to gost into other accounts
Read messages etc.
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics


class Owner:
    '''
    Sotres the methods for the owners menu and the key varbales
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
