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

    def __init__(self, Username=None):
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

    '''
    The core of the program to simplify standered tkinter settings
    '''

    def AddFrame(self, Frame, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates a Frame for building the GUI on to
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        # Creats the frame object
        Frame = TK.Frame(Frame, bg=self.Background)

        # Packs the Frame into the given master
        if Pack:
            Frame.pack(fill=TK.BOTH, expand=True)
        # Puts the frame into the grid
        else:
            Frame.grid(row=Row, column=Column,
                       sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Frame

    def AddLabel(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates a Label for dispalaying text
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        # Creats the Label object
        Label = TK.Label(Frame, bg=self.Background,
                         fg=self.Foreground, font=self.Font, text=Text)

        # Packs the Label into the given master
        if Pack:
            Label.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Label.grid(row=Row, column=Column,
                       sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Label

    def AddLabel_spacer(self, Frame, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates a Label for GUI spacing
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        # Creats the Label object
        Space_Label = TK.Label(Frame, bg=self.Background,
                               fg=self.Foreground, font=self.Font)

        # Packs the Label into the given master
        if Pack:
            Space_Label.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Space_Label.grid(row=Row, column=Column,
                             sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Space_Label

    def AddLabel_title(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates a Label for dispalaying titles
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        # Creats the Label object
        Title_Label = TK.Label(Frame, bg=self.Background,
                               fg=self.Foreground, font=self.TitleFont, text=Text)

        # Packs the Label into the given master
        if Pack:
            Title_Label.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Title_Label.grid(row=Row, column=Column,
                             sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Title_Label

    def AddLabel_subtitle(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates a Label for dispalaying sub titles
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        # Creats the Label object
        SubTitle_Label = TK.Label(Frame, bg=self.Background,
                                  fg=self.Foreground, font=self.SubTitleFont, text=Text)

        # Packs the Label into the given master
        if Pack:
            SubTitle_Label.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            SubTitle_Label.grid(row=Row, column=Column,
                                sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return SubTitle_Label

    def AddButton(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Adds a simple button to the Given frame
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True

        **You must add your own command using the .config method**
        '''
        Button = TK.Button(Frame, bg=self.Btn_Background, activebackground=self.Btn_Active,
                           foreground=self.Foreground, font=self.Font, text=Text)

        # Packs the Label into the given master
        if Pack:
            Button.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Button.grid(row=Row, column=Column,
                        sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Button

    def AddButton_negetive(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Adds a simple button to the Given frame
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True

        **You must add your own command using the .config method**
        **this only changes colours not functionality**
        '''
        Button_negetive = TK.Button(Frame, bg=self.QuitBtn_Background, activebackground=self.QuitBtn_Active,
                                    foreground=self.Foreground, font=self.Font, text=Text)

        # Packs the Label into the given master
        if Pack:
            Button_negetive.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Button_negetive.grid(row=Row, column=Column,
                                 sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Button_negetive

    def AddButton_possitive(self, Frame, Text, Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Adds a simple button to the Given frame
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True

        **You must add your own command using the .config method**
        **this only changes colours not functionality of a normal button**
        '''
        Button_possitive = TK.Button(Frame, bg=self.PositiveBtn_Background, activebackground=self.PositiveBtn_Active,
                                     foreground=self.Foreground, font=self.Font, text=Text)

        # Packs the Label into the given master
        if Pack:
            Button_possitive.pack(fill=TK.BOTH, expand=True)
        # Puts the Label into the grid
        else:
            Button_possitive.grid(row=Row, column=Column,
                                  sticky="nsew", columnspan=CSpan, rowspan=RSpan, padx=2, pady=2)

        return Button_possitive

    def AddEntry(self, Frame, Focus=False, Show="", Pack=False, Row=None, Column=None, CSpan=1, RSpan=1):
        '''
        Creates an Entry object which lets the user enter text
        If pack is true then it will pack it into the given frame
        Row, Column etc. are not needed if packing is True
        '''
        Entry = TK.Entry(
            Frame, font=self.Font, foreground=self.Foreground)

        # If something else is ment to display not letters this will change
        if Show:
            Entry.config(show=Show)

        # Packs the Entry into the given master frame
        if Pack:
            Entry.pack(fill=TK.BOTH, expand=True)

        # Putes the entry into the grid
        else:
            Entry.grid(row=Row, column=Column, sticky="nsew",
                       padx=2, pady=2, columnspan=CSpan)

        # Focuses the users mouse onto the entry so they can just start typing
        if Focus:
            Entry.focus()

        return Entry

    # A method used in production to call when a feature isn't finished yet
    def WorkInProgress(self):
        self.WIP_tl = TK.Toplevel(bg=self.Background)
        self.WIP_lbl = TK.Label(self.WIP_tl, font=self.Font, foreground=self.Foreground, bg=self.Background,
                                text="This feature is currently a work in progress, we appologise fore any inconvinience")
        self.WIP_lbl.grid(row=0, column=0, sticky="nsew")

        self.Align_Grid(self.WIP_tl)

    def Align_Grid(self, Frame):
        '''
        Allows the grids to expand as their frame dose
        '''
        # Gets the nuber of rows and columns of the grid
        self.Grid_Size = Frame.grid_size()

        # Loops through every column
        for i in range(self.Grid_Size[0]):
            # Sets the weight to a non zero value so it can expand
            Frame.columnconfigure(i, weight=1)
        # Loops through every row
        for i in range(self.Grid_Size[1]):
            # Sets the weight to a non zero value so it can expand
            Frame.rowconfigure(i, weight=1)


# This is purely for debugging perpouses- this file is never ment to run from inside itself
if __name__ == "__main__":
    pass
