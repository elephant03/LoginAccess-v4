'''
Displays the extra options that teater accounts can access to
crete new students, track records, change studient privalage
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics


class Teacher:
    '''
    Sotres the methods for the techer menu system and the key varbales
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
