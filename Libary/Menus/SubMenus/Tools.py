'''
Gives the user a list of the tool they have access to
These will be read direculy from the tools file and when clicked they will attempt
to call a "Run" method
'''

# Imports the needed libaries
# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics
# imoorts the glob libary
import glob


class Tools:
    '''
    Sotres the methods for the tools system and the key varbales
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

        # Creats an array to store the tools
        self.Tools_list = []

        print(__file__)

        '''
        # Finds the current dirrectory
        self.Tools_File = __file__
        # Removes the name of this file
        self.Tools_File = self.Tools_File[:-8]
        # Adds the path to the tools to the current dirrectory
        self.Tools_File += r"\Moduals\Tools\*.pyw"
        # Makes the file python readable
        self.Tools_File.replace("\\", "\\\\")

        # Uses glob to get all of the tools files
        self.Files = glob.glob(self.Tools_File)

        # Allows for the grid to work
        self.EndRow_Value = 2

        # Loops through all of the tools
        for i in range(len(self.Files)):

            # Imports the tool using the method at top of document
            self.directory, self.module_name = os.path.split(self.Files[i])
            self.module_name = os.path.splitext(self.module_name)[0]

            self.path = list(sys.path)
            sys.path.insert(0, self.directory)
            try:
                Tool = __import__(self.module_name)
                self.Tools_list.append(Tool)
            finally:
                sys.path[:] = self.path  # restore

            # Adds the button to run the tool
            self.Tools_btn = TK.Button(self.ToolsMenu_fr, bg=self.Btn_Background, activebackground=self.Btn_Active,
                                       foreground=self.Foreground, font=self.Font, text=self.module_name, command=lambda Num=i: self.RunTool(Num))
            self.Tools_btn.grid(row=i+2, column=0, pady=2,
                                padx=2, sticky="nsew")

            self.EndRow_Value += 1
        '''
