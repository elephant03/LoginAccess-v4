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
            self.SetDefults()

            return

        # Tries to read the information from the database by the username
        with lite.connect("myDatabase.db") as self.Con:
            self.Cur = self.Con.cursor()

            # If a colours table doesn't exist this will make one and link Username to the users table
            self.Cur.execute("""CREATE TABLE IF NOT EXISTS Colours (
                Username TEXT NOT NULL PRIMARY KEY,
                Background TEXT NOT NULL DEFAULT '#7eccf7',
                Foreground TEXT NOT NULL DEFAULT 'Black',
                Btn_Background TEXT NOT NULL DEFAULT '#2db4ff',
                Btn_Active TEXT NOT NULL DEFAULT '#2da9ff',
                QuitBtn_Background TEXT NOT NULL DEFAULT '#ef2804',
                QuitBtn_Active TEXT NOT NULL DEFAULT '#f52804',
                PositiveBtn_Background TEXT NOT NULL DEFAULT '#1ece18',
                PositiveBtn_Active NUMERIC NOT NULL DEFAULT '#159b11',
                FontType TEXT NOT NULL DEFAULT 'Arial',
                FontSize INTEGER NOT NULL DEFAULT 14,
                TitleFontSize INTEGER NOT NULL DEFAULT 24,
                SubTitleSize INTEGER NOT NULL DEFAULT 18,
                FOREIGN KEY (Username) REFERENCES Users (Username) ON UPDATE CASCADE ON DELETE CASCADE
                );""")

            # Then selects everything in that table where the username is correct
            self.Cur.execute(
                "SELECT * FROM Colours WHERE Username = ?", (Username,))

            self.Colour_list = self.Cur.fetchall()

            # If the username doesn't exist the defults will be used
            # This can be cuased if a user hasn't changed their colour settings yet
            if not self.Colour_list:
                self.SetDefults()

                return

        self.Background = self.Colour_list[0][1]
        self.Foreground = self.Colour_list[0][2]
        self.Btn_Background = self.Colour_list[0][3]
        self.Btn_Active = self.Colour_list[0][4]
        self.QuitBtn_Background = self.Colour_list[0][5]
        self.QuitBtn_Active = self.Colour_list[0][6]
        self.PositiveBtn_Background = self.Colour_list[0][7]
        self.PositiveBtn_Active = self.Colour_list[0][8]
        self.Font = (self.Colour_list[0][9], self.Colour_list[0][10])
        self.TitleFont = (self.Colour_list[0][9], self.Colour_list[0][11])
        self.SubTitleFont = (self.Colour_list[0][9], self.Colour_list[0][12])

    def SetDefults(self):
        '''
        Sets all of the colour varables to their defult values.
        This is based off the colours in the Config.json file
        '''
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


# This is purely for debugging perpouses- this file is never ment to run from inside itself
if __name__ == "__main__":
    Test = Basics("Ambrose")

    print(Test.Background)
    print(Test.Font)
    print(Test.TitleFont)
