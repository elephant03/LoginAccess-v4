'''
Gives the user a list of the game they have access to
These will be read direculy from the games file and when clicked they will attempt
to call a "Run" method
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics
# imoorts the glob libary
import glob
# Imports sys and os libary to interact with the path
import sys
import os


class Games:
    '''
    Sotres the methods for the games system and the key varbales
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

        self.Games_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.Games_fr.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.Games_fr, "Games:", Row=0, Column=0)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.Games_fr, Row=1, Column=0)

        # Creats an array to store the games
        self.Games_list = []


        # Finds the current dirrectory
        self.Games_File = __file__
        # Removes the name of this file
        self.Games_File = self.Games_File[:-23]
        # Adds the path to the games to the current dirrectory
        self.Games_File += r"\Games\*py"
        # Makes the file python readable
        self.Games_File.replace("\\", "\\\\")

        # Uses glob to get all of the games files
        self.Files = glob.glob(self.Games_File)

        # Allows for the grid to work
        self.EndRow_Value = 2

        # Loops through all of the games
        for i in range(len(self.Files)):

            # Imports the game using a more veritile method as I don't know what will be in the file
            self.directory, self.module_name = os.path.split(self.Files[i])
            self.module_name = os.path.splitext(self.module_name)[0]

            self.path = list(sys.path)
            sys.path.insert(0, self.directory)
            try:
                game = __import__(self.module_name)
                self.Games_list.append(game)
            finally:
                sys.path[:] = self.path  # restore

            # Adds the button to run the game
            self.Games_btn = self.tb.AddButton(
                self.Games_fr, self.module_name, Row=self.EndRow_Value, Column=0)
            self.Games_btn.config(command=lambda Num=i: self.RunTool(Num))

            self.EndRow_Value += 1

        self.Space_lbl1 = self.tb.AddLabel_spacer(
            self.Games_fr, Row=self.EndRow_Value, Column=0)

        self.Back_btn = self.tb.AddButton(
            self.Games_fr, "Back", Row=self.EndRow_Value+1, Column=0)
        self.Back_btn.config(command=lambda: self.Games_fr.destroy())

        self.tb.Align_Grid(self.Games_fr)

    def RunTool(self, Num):
        '''
        Calls a Run method on the game when the button is pressed
        '''
        self.Games_list[Num].Run()
