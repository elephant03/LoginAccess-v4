# Imports the tkinter GUI libary
import tkinter as TK
# Imports json file handeler
import json
# Imports the database handeler
import sqlite3 as lite


class Basics:
    '''
    Will hold all of the basic tkinter funstions that I will used repetidally in the main
    program.
    '''

    # Stores the defult colours and fonts
    # Opens the json file to read defults
    with open('Config.json') as json_file:
        Colour_data = json.load(json_file)["Defults"]["Colours"]
        Defults = {
            "Background": Colour_data["Background"],
            "Foreground": Colour_data["Foreground"],
            "Btn_Background": Colour_data["Btn_Background"],
            "Btn_Active": Colour_data["Btn_Active"],
            "QuitBtn_Background": Colour_data["QuitBtn_Background"],
            "QuitBtn_Active": Colour_data["QuitBtn_Active"],
            "PositiveBtn_Background": Colour_data["PositiveBtn_Background"],
            "PositiveBtn_Active": Colour_data["PositiveBtn_Active"],
            "Font": (Colour_data["FontType"], Colour_data["FontSize"]),
            "TitleFont": (Colour_data["FontType"], Colour_data["TitleFontSize"], "bold"),
            "SubTitleFont": (Colour_data["FontType"], Colour_data["SubTitleFontSize"], "bold"),
        }

    def __init__(self, Username):
        '''
        Sets up the players colour varables based off what is stored in the database
        Set username to none to use the defults
        '''
        if not Username:
            # If no username is given set all of the defults
            # These can be edited in the Config.json file
            self.Background = self.Defults["Background"]
            self.Foreground = self.Defults["Foreground"]
            self.Btn_Background = self.Defults["Btn_Background"]
            self.Btn_Active = self.Defults["Btn_Active"]
            self.QuitBtn_Background = self.Defults["QuitBtn_Background"]
            self.QuitBtn_Active = self.Defults["QuitBtn_Active"]
            self.PositiveBtn_Background = self.Defults["PositiveBtn_Background"]
            self.PositiveBtn_Active = self.Defults["PositiveBtn_Active"]
            self.Font = self.Defults["Font"]
            self.TitleFont = self.Defults["TitleFont"]
            self.SubTitleFont = self.Defults["SubTitleFont"]

            return

        # Tries to read the information from the database by the username
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()
