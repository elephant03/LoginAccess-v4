'''
Shows the different revison tools that studient account have access to
These features and the most resent and so will be the most buggy and need the most work
'''


class Education:
    '''
    Sotres the methods for the education system and the key varbales
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
