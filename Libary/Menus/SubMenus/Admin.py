'''
Loads the admin menu and all of its options
This includes the ability to change users account type read messages
and give warnings
For more information please see the wiki
'''

# Imports all of the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics


class Admin_menu:
    '''
    Controls the GUI and redirects calls to the appropiate file
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
