'''
Checks to see if an email is valid as best as it can
it will return true if it believes the email is valid

It will also- if set up send an email to the account
'''
# Imports the json handeler to check if the email is set up
import json


def ValidateEmail(Email):
    if "@" not in Email:
        return False

    if "." not in Email.split("@")[1]:
        return False

    with open("Config.json") as json_file:
        if json.load(json_file)["Email"]["Enabled"] == True:
            from Libary.Utility import EmailHandeler
            # Load the email handeler
            EmailHandeler.SendEmail("welcome")

    return True
