'''
If the user has provided their email adress and linked it then
they can reset their password through this method.
It will change their password to a random string of 5 numbers which
will be emailed to the user
'''

# For the GUI
import tkinter as TK
from Libary.Utility import tkinter_basics


class Reset:
    '''
    The main class to be called to bring up the password reset GUI
    '''

    def __init__(self, Main_fr):
        '''
        Creats and loads the password reset GUI
        '''
        self.tb = tkinter_basics.Basics()

        self.Main_fr = Main_fr

        self.ResetPassword_fr = self.tb.AddFrame(self.Main_fr, Row=0, Column=0)
        self.ResetPassword_fr.grid(
            row=0, column=0, sticky="nsew", columnspan=2, padx=0, pady=0)

        self.Title_lbl = self.tb.AddLabel_title(
            self.ResetPassword_fr, "Password Reset", Row=0, Column=0, CSpan=2)

        self.Space_lbl = self.tb.AddLabel_spacer(
            self.ResetPassword_fr, Row=1, Column=0, CSpan=2)

        self.Back_btn = self.tb.AddButton(
            self.ResetPassword_fr, "Back", Row=2, Column=0)
        self.Back_btn.config(command=lambda: self.ResetPassword_fr.destroy())

        self.Reset_btn = self.tb.AddButton(
            self.ResetPassword_fr, "Reset Password", Row=2, Column=1)
        self.Reset_btn.config(command=lambda: self.Reset())

        self.tb.WorkInProgress()

        self.tb.Align_Grid(self.Main_fr)
        self.tb.Align_Grid(self.ResetPassword_fr)

        return

    def Reset(self):
        return
