'''
Checks the users login details agaist the ones in the database
If they are correct it will return True to the main system
If they are wrong it will return False
'''

# Imports the hashing system for usernames and passwords
from Libary.Utility.Security import Hash as h
# Imports database handeler
import sqlite3 as lite


def Check(Username_ent, Password_ent):
    '''
    The core of the checking system
    Passes the username & password entries to advoid storing the users details anywhere
    '''

    # Gets the usernames hash value- secure is false as you need to check it with no salt
    Username = str(h.Hash(Username_ent.get(), Secure=False))

    with lite.connect("myDatabase.db") as Con:
        Cur = Con.cursor()

        # Checks if the username is in the Users table
        Cur.execute(
            "SELECT EXISTS (SELECT * FROM Users WHERE Username = ?)", (Username, ))

        if Cur.fetchall()[0][0] == 0:
            return False

        Cur.execute(
            "SELECT Password FROM Users WHERE Username = ?", (Username, ))

        Pass = h.Verify(Password_ent.get(), Cur.fetchall()[0][0])

        return Pass
